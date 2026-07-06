from memory import Memory


class SimpleAgent:
    def __init__(self):
        self.memory = Memory()

    def think(self, prompt: str) -> str:
        self.memory.add(prompt)
        return f"Agent received: {prompt}"


if __name__ == "__main__":
    agent = SimpleAgent()
    user_input = input("You: ")
    print("Agent:", agent.think(user_input))
