import os

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

def cell():
    while True:
        print("\nDu är i cellen. Vad vill du göra?")
        print("1- Öppna dörren")
        print("2- Kolla runt i cellen")

        user_input = input("Skriv numret av ett av valen: ")

        if user_input == "1":
            print("Dörren är låst. Hitta nyckeln.")
        elif user_input == "2":
            print("Du kollar runt och hittar en nyckel. Du använder nyckeln för att öppna dörren.")
            rum1()
            break
        else:
            print("Ogiltigt val! Försök igen.")

def rum1():
    while True:
        print("\nDu hamnar i rum 1 och är i korridoren. Vad vill du göra?")
        print("1- Gå till höger")
        print("2- Gå till vänster")

        user_input = input("Skriv numret av ett av valen: ")

        if user_input == "1":
            print("Du går till höger och hittar en vakt.")
            print("Vill du:")
            print("1- Slå vakten")
            print("2- Vända dig om och gå andra hållet")

            action = input("Skriv numret av ett av valen: ")

            if action == "1":
                print("Du försöker slå vakten men han slår dig till marken.")
                print("Han lägger dig i handbojor och tar dig tillbaka till cellen.")
                cell()  # Restart the game
                break
            elif action == "2":
                print("Du vänder dig om och går andra hållet.")
                print("Du går till vänster och hittar ett lås.")
                print("Koden till låset är svaret till en matteekvation. Ekvationen står på tavlan bredvid dig.")
                print("Du måste skynda dig för att om 1 minut så kommer larmet att slås på och vakterna kommer att veta vart du är.")
                print("Ekvationen är: 5(2+1)^2.")

                answer = input("Skriv in svaret på ekvationen: ")

                if answer == "45":
                    print("Du låser upp låset och går vidare.")
                    break
                else:
                    print("Fel svar! Försök igen.")
            else:
                print("Ogiltigt val! Försök igen.")
        elif user_input == "2":
            print("Du går till vänster och hittar ett lås.")
            print("Koden till låset är svaret till en matteekvation. Ekvationen står på tavlan bredvid dig.")
            print("Du måste skynda dig för att om 1 minut så kommer larmet att slås på och vakterna kommer att veta vart du är.")
            print("Ekvationen är: 5(2+1)^2.")

            answer = input("Skriv in svaret på ekvationen: ")

            if answer == "45":
                print("Du låser upp låset och går vidare.")
                break
            else:
                print("Fel svar! Försök igen.")
        else:
            print("Ogiltigt val! Försök igen.")

# Start the game
cell()