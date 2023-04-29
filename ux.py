import os
import openai

# Get the API key from Environment Variables
openai.api_key = "OPENAI_API_KEY"

print("Welcome to the OpenAI GPT-3.5 chatbot!")
print("You can chat with the bot or ask it to generate an image based on a description.")
print("To exit the program at any time, type 'q' or 'quit'.")


def generate_image():
    print("Please describe the image you'd like to generate.")
    print("For best results, keep your description short and specific.")
    while True:
        description = input("Description: ")
        if description.lower() in ['q', 'quit']:
            return
        if description.lower() in ['chat', 'talk']:
            chat()
            return
        try:
            # Do the API call to generate image
            img = openai.Image.create(
                prompt=description,
                n=1,
                size="512x512"
            )
            # Print the URL of the image
            print("Image generated! URL:", img.data[0].url)
        except Exception as e:
            print("Sorry, there was an error generating the image.")
            print("Please try again or type 'q' or 'quit' to exit.")

def chat():
    print("You can now chat with the bot.")
    print("Type 'q' or 'quit' to exit and 'image' to generate an image.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['q', 'quit']:
            return
        if user_input.lower() in ['image', 'pic', 'picture']:
            generate_image()
            return
        try:
            # Do the API call to chat
            completion = openai.Completion.create(
                engine="text-davinci-002",
                prompt=user_input,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            # Print the response
            print("Bot:", completion.choices[0].text)
        except Exception as e:
            print("Sorry, there was an error processing your request.")
            print("Please try again or type 'q' or 'quit' to exit.")

# Start the program
chat()
