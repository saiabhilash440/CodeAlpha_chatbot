def get_bot_response(user_message):
    message = user_message.lower().strip()
    
    # Rule-based pattern matching
    if message in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif "how are you" in message:
        return "I'm doing great, thank you! How are you?"
    elif "your name" in message or "who are you" in message:
        return "I am a simple rule-based Python chatbot."
    elif "what can you do" in message or "help" in message:
        return "I can answer basic greetings and simple questions. Try asking 'how are you' or say 'bye'!"
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a productive day ahead!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you rephrase?"

def run_chatbot():
    print("=" * 40)
    print("       RULE-BASED PYTHON CHATBOT")
    print("=" * 40)
    print("Chatbot: Hello! Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()