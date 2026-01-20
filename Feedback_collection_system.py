feedback_list = []

def add_feedback():
    name = input("Enter your name: ")
    message = input("Enter feedback: ")
    feedback_list.append({"name": name, "message": message})
    print("Feedback submitted")

def view_feedback():
    if not feedback_list:
        print("No feedback available")
    else:
        for feedback in feedback_list:
            print(feedback["name"], "-", feedback["message"])

def main():
    while True:
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_feedback()
        elif choice == "2":
            view_feedback()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
