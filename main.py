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