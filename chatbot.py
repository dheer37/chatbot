import google.generativeai as genai

# Configure with your Gemini API key
genai.configure(api_key="AIzaSyBg5J4TKUW_2gwAWBhcNHTmN6q7YpF1v6U")

# Choose the Gemini model (gemini-1.5-flash is fast & cheap)
model = genai.GenerativeModel("gemini-1.5-flash")

def chatbot():
    print("🤖 Gemini Chatbot (type 'exit' to quit)")
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye 👋")
            break

        response = chat.send_message(user_input)
        print("Chatbot:", response.text)

if __name__ == "__main__":
    chatbot()
