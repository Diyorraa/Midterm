def get_info(size):

    # Define the information prompt based on the size
    if size == "short":
        prompt = "Please provide a topic for a short information:"
    elif size == "long":
        prompt = "Please provide a topic for a long information:"
    else:
        print("Invalid size. Please enter 'short' or 'long'.")
        return

    # Display the initial prompt and get the user's input
    print(prompt)
    while True:
        topic = input("Topic: ")
        if topic.lower() in ['q', 'quit']:
            return
        try:
            # Do the API call to generate information
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"Generate {size} information about {topic}.",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            # Print the initial response
            print(response.choices[0].text.strip())

            # Ask the user if they want more information
            while True:
                user_input = input("Type 'C' for more information, or 'q' to quit: ")
                if user_input.lower() in ['q', 'quit']:
                    return
                elif user_input.lower() == 'c':
                    # Do the API call to generate more information
                    response = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt=response.choices[0].text.strip() + "\n\nGenerate more information.",
                        max_tokens=1024,
                        n=1,
                        stop=None,
                        temperature=0.7,
                    )
                    # Print the additional response
                    print(response.choices[0].text.strip())
                    continue
                else:
                    print("Invalid input. Please enter 'C' or 'q'.")
                    continue
        except Exception as e:
            print("Sorry, there was an error processing your request.")
            print("Please try again or type 'q' or 'quit' to exit.")


"""def get_info(size):
    if size == "short":
        prompt = "Please provide a topic for a short information:"
    elif size == "long":
        prompt = "Please provide a topic for a long information:"
    else:
        print("Invalid size. Please enter 'short' or 'long'.")
        return

    # Display the initial prompt and get the user's input
    print(prompt)
    while True:
        topic = input("Topic: ")
        if topic.lower() in ['q', 'quit']:
            return
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"Generate {size} information about {topic}.",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            print(response.choices[0].text.strip())

            while True:
                user_input = input("Type 'C' for more information, or 'q' to quit: ")
                if user_input.lower() in ['q', 'quit']:
                    return
                elif user_input.lower() == 'c':
                    # Do the API call to generate more information
                    response = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt=response.choices[0].text.strip() + "\n\nGenerate more information.",
                        max_tokens=1024,
                        n=1,
                        stop=None,
                        temperature=0.7,
                    )
                    print(response.choices[0].text.strip())
                    continue
                else:
                    print("Invalid input. Please enter 'C' or 'q'.")
                    continue
        except Exception as e:
            print("Sorry, there was an error processing your request.")
            print("Please try again or type 'q' or 'quit' to exit.")"""