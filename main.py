from datetime import datetime

name = input("Enter your name: ")
print("Hello", name, "! Welcome to Smart Student Assistant")

while True:
    print("\n1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Study Tip: Study for 25 minutes and take a 5-minute break.")

    elif choice == "2":
        print("Motivation Quote: Success comes from consistent effort.")

    elif choice == "3":
        print("Current Date & Time:", datetime.now())

    elif choice == "4":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid choice")