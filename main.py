import requests
import os
from dotenv import load_dotenv
import json

# Load the API key from .env file
load_dotenv()


# API endpoint and get API key from .env file
chat_url = "https://api.openai.com/v1/chat/completions"
image_url = "https://api.openai.com/v1/images/generations"

api_key = os.getenv('API_KEY')

# Because we're using REST API, we need to set the headers for authentication
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}


# History array to store the conversation context
history = []


def chat_api_call(content, history):

    # JSON data to send to the API
    data = {
        "model": "gpt-3.5-turbo",
        #Append history to the message to send to the API for context
        "messages": history + [
            {
                "role": "user",
                "content": content
            }
        ]
    }

    # Make the API call
    try:
        response = requests.post(chat_url, headers=headers, json=data)
        response_json = response.json()
        
        # Print the response from the API
        for choice in response_json["choices"]:
            print("\nChatGPT: " + choice["message"]["content"] + "\n")
            history.append({"role": "assistant", "content": choice["message"]["content"]})

    except Exception as e:
        print(f"Error: {e}")


def generate_images(prompt):
    data = {
        "prompt": prompt,
        "n": 2,
        "size": "1024x1024"
    }
    response = requests.post(image_url, headers=headers, data=json.dumps(data))
    response_data = response.json()["data"]
    urls = [d["url"] for d in response_data]
    
    print("There is " + str(len(urls)) + " images generated:\n") if len(urls) == 1 else print("There are " + str(len(urls)) + " image generated:\n")    

    for i in range(len(urls)):
        print(urls[i] + "\n")


#Make a user's choice as a variable with the default value of null

# Keep asking for user input until they type "quit"
while True:

    #User choose to generate images or chat
    user_input = input("Do you want to generate images or chat? (type 'images' or 'chat'), Type quit to exit\nYou: ")

    if user_input.lower() == "quit" or user_input.lower() == "exit" or user_input.lower() == "q":
        break

    elif user_input.lower() == "images":
        #loop through the user's input until they type "change"
        while True:
            print("Type 'change' to change your choice")
            user_input = input("You: ")
            if user_input.lower() == "change":
                break
            generate_images(user_input)

    elif user_input.lower() == "chat":
        while True:
            print("Type 'change' to change your choice")
            user_input = input("You: ")
            if user_input.lower() == "change":
                break
            chat_api_call(user_input, history)

    else:
        print("Please type 'images' or 'chat'")

print("\nBye!")