print("Welcome! This is the Survey Bot.")
print("It's designed to help gather valuable feedback and insights.")
print("Whether you need to improve products, understand customer satisfaction, or collect opinions, Survey Bot is here to assist.")

name = input("What is your name? ")

try:
    age = int(input("How old are you? "))
except ValueError:
    print("Please enter a valid age.")
    age = int(input("How old are you? "))

question = input("How can it help you today? ")

print("\nHere are some options to continue:")
print("1. Take a product feedback survey")
print("2. Provide customer satisfaction feedback")
print("3. Exit")

while True:
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        print("You chose the product feedback survey. (Placeholder response)")
    elif choice == "2":
        print("You chose customer satisfaction feedback. (Placeholder response)")
    elif choice == "3":
        print("Thank you for using the Survey Bot. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")