from src.agents import ask_rag, is_exit_command


def run_chatbot():
    print("=" * 90)
    print("🌍 TOURISM RAG ASSISTANT")
    print("=" * 90)
    print("Ask questions about the supplied tourism knowledge base.")
    print("Type 'exit' to stop.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot stopped.")
            break

        if is_exit_command(question):
            print("Chatbot stopped. 👋")
            break

        if not question:
            print("Assistant: Please enter a question.\n")
            continue

        try:
            answer, retrieved_docs = ask_rag(question)

            print("\nAssistant:")
            print(answer)

            if retrieved_docs:
                print(
                    f"\n[retrieved {len(retrieved_docs)} relevant knowledge chunks]"
                )

        except Exception as exc:
            print(
                "\nAssistant: I could not process that request right now. "
                "Please try again."
            )
            print("Internal error:", type(exc).__name__, str(exc))


if __name__ == "__main__":
    run_chatbot()
