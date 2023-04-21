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
    history = []
    userInput = input("You : ")
    # Verify the input
    if userInput.lower() == "quit" or userInput == "q":
        return 0
    if userInput.lower() == "image":
        return GenerateImage()
    if userInput.lower() == "tokens":
        return display_token_count(history)
    if userInput.lower() == "reset":
        history = []
        print("\nHistory has been wiped.\n")
    history.append({"role": "user", "content": userInput})
    # Do the api call to chat
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= history +[
            {"role": "user", "content": userInput}
        ]
    )    
    # Print the answer
    print("ChatGpt: ", completion.choices[0].message.content)
    display_token_count(history)
    return Chat()


#counting tokens function
def count_tokens(message):
    return len(message.split())

def display_token_count(history):
    user_tokens = sum(count_tokens(message["content"]) for message in history if message["role"] == "user")
    assistant_tokens = sum(count_tokens(message["content"]) for message in history if message["role"] == "assistant")
    print(f"\nUser tokens: {user_tokens}, Assistant tokens: {assistant_tokens}\n")

# Start the program
Chat()
