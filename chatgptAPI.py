import os
import requests
import json

# Get the API key from Environment Variables
api_key = os.getenv("OPENAI_API_KEY")

print("If you want to quit the chat press 'q' or 'quit'")
print("Enter 'chat' to chat and 'image' to generate image")
print("Enter 'size' to change the size of the answer")
print("By default you are in chat mode")

# Because we're using REST API, we need to set the headers for authentication
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# History array to store the conversation context
history = []

# API endpoint and get API key from .env file
chat_url = "https://api.openai.com/v1/chat/completions"
image_url = "https://api.openai.com/v1/images/generations"

# The max number of tokens that the API can use to answer
max_tokens = 100

def SetSize():
    global max_tokens
    userInput = input("\nDo you want a 'short' or a 'long' answer : ")
    while True:
        if userInput == "short":
            max_tokens = 100
            return
        elif userInput == "long":
            max_tokens = 1024
            return
        else:
            userInput = input("\nInvalid size. Please enter 'short' or 'long' : ")

def GenerateImage():
    userInput = input("Give a description of the desired image : ")
    # Verify the input
    if userInput == "quit" or userInput == "q":
        return 0
    if userInput == "size":
        SetSize()
        return GenerateImage()
    if userInput == "chat":
        return Chat()

    # JSON data to send to the API
    data = {
        "prompt": userInput,
        "n": 1,
        "size": "1024x1024"
    }

    # Make the API call
    try:
        response = requests.post(image_url, headers=headers, data=json.dumps(data))
        response_data = response.json()["data"]
        url = response_data[0]["url"]
        print(url + "\n")

    except Exception as e:
        print(f"Error: {e}")
    return GenerateImage()

def Chat():
    userInput = input("You : ")

    # Verify the input
    if userInput == "quit" or userInput == "q":
        return 0
    if userInput == "size":
        SetSize()
        return Chat()
    if userInput == "image":
        return GenerateImage()

    # JSON data to send to the API
    data = {
        "model": "gpt-3.5-turbo",
        #Append history to the message to send to the API for context
        "messages": history + [
            {
                "role": "user",
                "content": userInput
            }
        ],
        "max_tokens": max_tokens
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

    return Chat()

# Start the program
SetSize()
Chat()
