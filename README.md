# _personal_ai_assistant_kiko
This repository contains the code for personal ai assistant with the power of chatGPT openai API, other than that it can also tell the latest news and weather of any city at any day and remembers the chat.

 **** before the code on your system install all the required libraries in us enviornment
 
1. config.py - it is where we will store all of our api keys and later use them in our program
2. main.py- contains the main code which will be responsbile for the ai to response

#this program uses all the funcitons and modules which are compatiable with mac os for windows the modules will be little different

- for speechrecoginition install it in ur terminal using pip install speechrecognition
- for recognising the we are using recognize_google which can we used by both window or macos
- in mac for making our ai speak we use os.system or we can use  subprocess.call(["say", text]) -- os.system creates problems sometime so 
  better use the later

API's:
- first and most important we are using openai's free api with help of which we can generate texts and responsses like chatgpt and we can also have the responses saved on our system by creating a file
- since the knowledge of chatgpt is limited to 2021 we are using some other API's like weatherapi and newsapi in order to generate current news and weather of a city.

EXTRA's
-Since it is personal computer i have modified it according to my needs 
- i have made commands and call for opening all the apps that i use in my system and all the websites that i use for the ease.
- also our assistant can remember the chats and also we can ask it to reset the chat.
  
