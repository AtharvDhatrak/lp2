import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    # Greeting responses
    if re.search(r'\bhi\b|\bhello\b|\bhey\b', user_input):
        return "Hello! How can I help you today?"
    # Store hours response
    elif re.search(r'when are you open\b|store hours\b|opening times\b', user_input):
        return "We are open from 9 AM to 9 PM, Monday to Saturday."
    # Location response
    elif re.search(r'where are you located\b|store location\b|address\b', user_input):
        return "We are located at 123 Python Drive, Codeville."
    # Help response
    elif re.search(r'help\b|\bassist\b', user_input):
        return "What do you need help with? You can ask me about store hours, locations, or general inquiries."
    # Default response for unrecognized inputs
    else:
        return "I'm not sure how to help with that. Can you try asking something else?"

def main():
    print("Welcome to our customer service chat! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot_response(user_input)
        print("Bot: " + response)

if __name__ == "__main__":
    main()
