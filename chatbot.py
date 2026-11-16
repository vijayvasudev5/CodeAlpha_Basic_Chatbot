
def chatbot():
    print("================================")
    print("       WELCOME TO CHATBOT")
    print("================================")
    print("Type 'hello', 'how are you', 'what is your name' or 'bye'")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Bot: I am a Basic Python Chatbot.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start chatbot
chatbot()
