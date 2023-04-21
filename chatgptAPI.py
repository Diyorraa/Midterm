import os
import openai

# Get the API key from Environment Variables
openai.api_key = os.getenv("OPENAI_API_KEY")

print("If you want to quit the chat press 'q' or 'quit'")

while True:
    orig = input("You: ")
    if orig == "quit" or orig == "q":
        break
    # Do the api call
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": orig}
        ]
    )
    # Print the answer
    print("ChatGpt: ", completion.choices[0].message.content)