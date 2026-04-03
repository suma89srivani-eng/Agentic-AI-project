from memory.chat_memory import ChatMemory
from agents.agent_router import AgentRouter

def main():
    print("=== Agentic AI Assistant ===")
    print("Type 'exit' to quit.\n")

    memory = ChatMemory()
    router = AgentRouter(memory)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting Agentic AI Assistant...")
            break

        response = router.route(user_input)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    main()
