import os
import openai

openai.api_key = "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"


while True:
    orig = input("You: ")
    if orig == "quit" or orig == "q":
        break
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )
    print("ChatGpt: " + completion.choices[0].message)