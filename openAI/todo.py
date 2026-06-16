from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(prompt):
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text

tasks = []

while True:
    print("\n--- TODO MENU ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("5. AI Suggest Tasks")
    print("6. Exit")

    choice = input("Enter choice: ")

    # Example placeholder list

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added:", task)

    elif choice == "2":
        print("\nTasks:")
        for i, t in enumerate(tasks, 1):
            print(i, t)

    elif choice == "3":
        index = int(input("Enter task number: ")) - 1
        if 0 <= index < len(tasks):
            print("Deleted:", tasks.pop(index))
        else:
            print("Invalid index")

    elif choice == "5":
        topic = input("What should AI help you with? ")

        result = ask_ai(
            f"Suggest a simple to-do list for: {topic}"
        )

        print("\nAI Suggestions:\n")
        print(result)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")