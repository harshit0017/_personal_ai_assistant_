import os
import openai
from config import apikey


openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a letter to the hr of a company for job as software developer \n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)