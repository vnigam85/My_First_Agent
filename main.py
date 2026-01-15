from google import genai
import os

class GeminiAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def respond(self, message: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return response.text

def run_agent():
    agent = GeminiAgent()
    print("Gemini Agent active. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Agent: Goodbye!")
            break
        print(f"Agent: {agent.respond(user_input)}")

if __name__ == "__main__":
    run_agent()