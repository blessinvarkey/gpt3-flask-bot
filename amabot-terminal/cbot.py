import os
import openai
import apikey

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = apikey.API_KEY

input_text = input("Write your prompt here: ")
response = openai.Completion.create(
engine="text-davinci-002",
prompt= input_text,
temperature=0.7,
max_tokens=256,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)
print(response.choices[0].text)


