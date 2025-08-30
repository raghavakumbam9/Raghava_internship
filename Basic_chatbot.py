08.30 10:44 AM
import random
import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot assistant. Type 'help' for options or 'bye' to exit.\n")

    jokes = [
        "Why don’t programmers like nature? Because it has too many bugs! ",
        "Why did the computer go to the doctor? Because it caught a virus! ",
        "Why don’t robots get hungry? Because they are already stuffed! 🤖"
    ]

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("🤖 Chatbot: Goodbye! Have a wonderful day ")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello there! How can I help you today?")
        elif "good morning" in user_input:
            print("🤖 Chatbot: Good morning! Hope you have a productive day ")
        elif "good night" in user_input:
            print("🤖 Chatbot: Good night! Sweet dreams ")

        # Personal
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm your chatbot assistant. You can call me Bot!")
        elif "who made you" in user_input:
            print("🤖 Chatbot: I was created by a Python programmer ‍")

        # Date and Time
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: The current time is {now}")
        elif "date" in user_input or "day" in user_input:
            today = datetime.date.today().strftime("%A, %d %B %Y")
            print(f"🤖 Chatbot: Today's date is {today}")

        # Fun
        elif "joke" in user_input:
            print("🤖 Chatbot:", random.choice(jokes))
        elif "weather" in user_input:
            print("🤖 Chatbot: I can't check live weather ️, but I hope it's nice where you are!")

        # Help / Menu
        elif "help" in user_input or "options" in user_input or "menu" in user_input:
            print("🤖 Chatbot: You can ask me things like:")
            print("- Greetings: hello, hi, good morning, good night")
            print("- Personal: your name, how are you, who made you")
            print("- Info: time, date, weather")
            print("- Fun: tell me a joke")
            print("- Type 'bye' to exit")

        # Fallback
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Try typing 'help' to see what I can do.")

# Run chatbot
chatbot()
