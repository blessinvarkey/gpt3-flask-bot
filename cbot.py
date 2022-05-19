import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "api-key-comes-here"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Player 1: “The river is full of fish.”\nPlayer 2: “Yes, and one of them is enormous.”\nPlayer 1: “Yes, and he’s swimming toward us.”\nPlayer 2: “Yes, and he looks hungry.”\nPlayer 1: “Yes, and we are trapped in this boat.”\nPlayer 2: “Yes, and he looks more like a whale than a fish.”\nPlayer 1: “Yes, and now the motor won’t start.”\nPlayer 2: “Yes, and he’s about to swallow us.”\nPlayer 1: “Yes and I just remembered that this boat is also a plane.”\nPlayer 2: “Yes and lucky for you I just got my pilot’s license.”\nPlayer 1: \"Yes and we're about to take off.\"\nPlayer 2: \"Yes and  the whale is following us.\"\nPlayer 1:  \"Yes and he's gaining on us.\"\nPlayer 2: \"Yes, and we're about to crash into a mountain.\"\nPlayer 1:  \"Yes, but I see a cave we can fly into.\"\nPlayer 2: \"Yes, and the whale is right behind us.\"\nPlayer 1:  \"Yes, and he's about to eat us.\"\nPlayer 2: \"Yes, but I see a light at the end of the cave.\"\nPlayer 1:  \"Yes, and it's a giant cooking pot.\"\nPlayer 2: \"Yes, and the whale is swimming right into it.\"",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
