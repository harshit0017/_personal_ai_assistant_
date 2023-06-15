import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
import requests
from config import apikey, weather_api, news_api
from datetime import date, timedelta

def get_news(topic,news_api):
   # print(news_api)
   # to_date = date.today()
   # from_date = to_date - timedelta(days=365 * 5)
   # from_date_str = from_date.strftime("%Y-%m-%d")
   # to_date_str = to_date.strftime("%Y-%m-%d")
    current_date = date.today().strftime("%Y-%m-%d")

    url = f"https://newsdata.io/api/1/news?apikey={news_api}&q={topic}&language=en&from_date={current_date}&to_date={current_date}"
    response = requests.get(url)
   # print(response)
    data = response.json()
    # print(data)
    if "results" in data:
        articles = data["results"][:2]
        return articles

    else:
        return []




wapi_key= weather_api
def get_weather(wapi_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={wapi_key}&q={city}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return temperature, condition
    else:
        return None, None

chatStr = ""

def chat(query):
    global chatStr

    openai.api_key = apikey
    chatStr += f"Harshit: {query}\n Kiko: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    print(chatStr)
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for Prompt: {prompt} \n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response['choices'][0]['text'])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

import subprocess
def say(text):
    subprocess.call(["say", text])


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = None
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            pass

        if audio is not None:
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"Harshit said: {query}")
                return query
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error occurred during speech recognition: {e}")

    # If no audio was detected or an error occurred, prompt if the person is still there
    print("Are you there? I smell some problem")
    query = input()
    return query



if __name__ == '__main__':
    n_api =news_api
    print('Hello this is Kiko the artificial dog ')
    say("hello i am Kiko the artificial dog")

    while True:

        query = takeCommand()

        # making a list of list for opening sites
        sites = [["youtube", "https://www.youtube.com/"], ["spotify", "https://open.spotify.com"],
                 ["leetcode", "https://leetcode.com/problemset/all/"], ["github", "https://github.com/"],
                 ["netflix", "https://www.netflix.com/"], ["gmail", "https://mail.google.com/mail/u/0/"],
                 ["facebook", "https://www.facebook.com/"], ["twitter", "https://twitter.com/login"],
                 ["whatsapp", "https://web.whatsapp.com/"], ["instagram", "https://www.instagram.com/"]]



        # opening sites with command
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        import subprocess

        apps = [["facetime", "/System/Applications/FaceTime.app"],
                ["chrome", "/Applications/Google Chrome.app"],
                ["ms word", "/Applications/Microsoft Word.app"],
                ["ms excel", "/Applications/Microsoft Excel.app"],
                ["ms powerpoint", "/Applications/Microsoft PowerPoint.app"],
                ["vs code", "/Applications/Visual Studio Code.app"],
                ["camera", "/System/Applications/Image Capture.app"],
                ["safari", "/System/Applications/Safari.app"],
                ["calculator", "/System/Applications/Calculator.app"]]

        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]}...")
                subprocess.Popen(["open", app[1]])

        if "the time" in query:
            value = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {value}")



        elif "weather".lower() in query.lower():
            say("What city do you want the weather for?")
            print("What city do you want the weather for?")
            city = takeCommand()

            temperature, condition = get_weather(wapi_key, city)  # Replace "New York" with the desired cityikey, city)  # Replace "New York" with the desired city
            if temperature and condition:
                say(f"The temperature in {city} is {temperature} degrees Celsius and the weather condition is {condition}.")
            else:
                say("Sorry, I couldn't retrieve the weather information.")

        elif "news".lower() in query.lower():
            say("What topic do you want to know about?")
            topic = takeCommand()
            print(topic)
            articles = get_news(topic.lower(), n_api)

            if not articles:
                say("Sorry, I couldn't retrieve the news information.")
            else:
                for article in articles:
                    say(article["title"])
                    print(article["title"])
                    print("-------------------- \n")
                    description = article["description"]
                    if len(description) > 100:
                        description = description[:100] + "..."  # Truncate the description to 100 characters

                    say(description)
                    print(description)



        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)


       
        elif "bark".lower() in query.lower():
            musicPath = "/Users/harshitsingh/Downloads/dog-barking-70772.mp3"
            subprocess.Popen(["open", musicPath])


        elif "exit".lower() in query.lower():
            say("Bye sir")
            exit()
        elif "sleep".lower() in query.lower():
            say("Bye sir")
            exit()
        elif "bye".lower() in query.lower():
            say("Bye sir")
            exit()

        elif "chat reset".lower() in query.lower():
            chatStr = ""
        else:
            chat(query)

