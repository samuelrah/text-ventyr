import os
os.system

# Define the menu options
menu = ("1", "2", "3")

# Start the menu loop
while True:
    print("\nMENY\n")
    print("1- Starta spelet")
    print("2- Regler")
    print("3- Credits")

    # Prompt user input
    user_input = input("Skriv numret av ett av valen: ")

    # Check if the input is valid
    if user_input in menu:
        if user_input == "1":
            break  # Exit the menu loop
        elif user_input == "2":
            print("\nRegler: Följ instruktionerna för att spela spelet.")
        elif user_input == "3":
            print("\nCredits: Samuel Rahsepar.")
    else:
        print("Ogiltigt val! Försök igen.")





print("Du är fast i en fängelsecell och måste fly från fängelset. Du måste vara försiktig för att inte bli upptäckt av vakterna.")
print("Du kollar runt i cellen, du det en nyckel på golvet och fälgelse dörren är olåst.")

