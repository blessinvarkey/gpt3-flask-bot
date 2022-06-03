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


# General Ape was a great leader and a brave warrior. He was loved by his people and was respected by other leaders. He was a fair and just leader, and was always looking out for the best interests of his people. One day, a rival leader challenged him to a duel. General Ape accepted, and the two leaders fought a fierce battle. In the end, General Ape was victorious, and the other leader was killed.