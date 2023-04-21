import os
import openai

# Get the API key from Environment Variables
openai.api_key = os.getenv("OPENAI_API_KEY")

print("If you want to quit the chat press 'q' or 'quit'")
print("Enter 'chat' to chat and 'image' to generate image")
print("By default you are in chat mode")

def GenerateImage():
    userInput = input("Give a description of the desired image : ")
    # Verify the input
    if userInput == "quit" or userInput == "q":
        return 0
    if userInput == "chat":
        return Chat()
    # Do the api call to get img
    img = openai.Image.create(
        prompt=userInput,
        n=2,
        size="1024x1024"
    )
    # Print the url of the img
    print("url : ", img.data[0].url)
    return GenerateImage()

def Chat():
    userInput = input("You : ")
    # Verify the input
    if userInput == "quit" or userInput == "q":
        return 0
    if userInput == "image":
        return GenerateImage()
    # Do the api call to chat
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userInput}
        ]
    )    
    # Print the answer
    print("ChatGpt: ", completion.choices[0].message.content)
    return Chat()

# Start the program
Chat()
