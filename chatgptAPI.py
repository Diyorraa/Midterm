import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


while True:
    orig = input("You: ")
    if orig == "quit" or orig == "q":
        break
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": orig}
        ]
    )
    print("ChatGpt: ", completion.choices[0].message.content)