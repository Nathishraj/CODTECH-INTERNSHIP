import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"what is your name?", ["I am a chatbot!", "You can call me ChatBot."]),
    (r"how are you?", ["I'm just a bot, but I'm doing great!"]),
    (r"what can you do?", ["I can chat with you and answer simple questions."]),
    (r"who created you?", ["I was created as a project using Python and NLTK."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]),
    (r"(.*)", ["I'm not sure I understand. Can you rephrase?"])  # Default response
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()  # Remove extra spaces
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day! 😊")
            break
        response = chatbot.respond(user_input)
        if response:  # Ensure the response is not empty
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm not sure I understand. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
