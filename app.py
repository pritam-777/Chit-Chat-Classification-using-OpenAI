import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

text = input("Input your text   : ")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt = f"You will be provided with a statement, and your task is to check whether the statement is an informal conversation or not, If it's an  informal  conversation return it's a chit-chat else return it's not a chit chat\n{text}",
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
print(f"The answer is: {response['choices'][0]['text']}")
print("")