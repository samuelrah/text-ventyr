import os
import random

# Define the menu options
menu = ("1", "2", "3")

# Start the menu loop
while True:
    print("\nMENY\n")
    print("1- Starta spelet")
    print("2- Regler")
    print("3- avsluta spelet")

    # Prompt user input
    user_input = input("Skriv numret av ett av valen: ")

    # Check if the input is valid
    if user_input in menu:
        if user_input == "1":
            break  # Exit the menu loop
        elif user_input == "2":
            file = open("README.txt", "r", encoding="utf-8")
            print(file.read())
        elif user_input == "3":
            print("Spelet avslutas.")
            os._exit(0)  # Exit the program
    else:
        print("Ogiltigt val! Försök igen.")

print("\nDu är fast i en fängelsecell och måste fly från fängelset. Du måste vara försiktig för att inte bli upptäckt av vakterna.")
def cell():
    while True:
        print("\nDu är i cellen. Vad vill du göra?")
        print("1- Öppna dörren")
        print("2- Kolla runt i cellen")

        user_input = input("\nSkriv numret av ett av valen: ")

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

        user_input = input("\nSkriv numret av ett av valen: ")

        if user_input == "1":
            print("\nDu går till höger och hittar en vakt.")
            print("Vill du:")
            print("1- Slå vakten")
            print("2- Vända dig om och gå andra hållet")

            action = input("\nSkriv numret av ett av valen: ")

            if action == "1":
                print("\nDu försöker slå vakten men han slår dig till marken.")
                print("Han lägger dig i handbojor och tar dig tillbaka till cellen.")
                cell()  # Restart the game
                break
            elif action == "2":
                print("\nDu vänder dig om och går andra hållet.")
                print("Du går till vänster och hittar ett lås.")
                print("Koden till låset är svaret till en matteekvation. Ekvationen står på tavlan bredvid dig.")
                print("Du måste skynda dig för att om 1 minut så kommer larmet att slås på och vakterna kommer att veta vart du är.")
                print("Ekvationen är: 5(2+1)^2.")
            
            answer = input("\nSkriv svaret på ekvationen: ")
            
            if answer == "45":
                print("Du skrev korrekt svar och går vidare.")
                break
            else:
                print("Fel svar! Försök igen.")
                continue

        elif user_input == "2":
            print("\nDu går till vänster och hittar ett lås.")
            print("Koden till låset är svaret till en matteekvation. Ekvationen står på tavlan bredvid dig.")
            print("Du måste skynda dig för att om 1 minut så kommer larmet att slås på och vakterna kommer att veta vart du är.")
            print("Ekvationen är: 5(2+1)^2.")
            
            answer = input("\nSkriv svaret på ekvationen: ")
            
            if answer == "45":
                print("Du skrev korrekt svar och går vidare.")
                break
            else:
                print("Fel svar! Försök igen.")
                continue

        else:
            print("Ogiltigt val! Försök igen.")

# Start the game
cell()

print("\nDu är nu i rum 2. ")
print("För att fortsätta måste du skriva lösenordet till en dörr.")
print("Lösenordet är en gåta. gåtan står på väggen framför dig.")
print("det står: USA:s 22:a och 24:e presidenter hade samma föräldrar men var inte bröder. Hur kan detta vara möjligt?")


def rum2():
    while True:

        answer = input("\nSkriv in svaret på gåtan: ")

        if answer == "samma person" or answer == "det är samma person" or answer == "det var samma person":
            print("du skrev korekt svar och går vidare.")
            break
        else:
            print("Fel svar! Försök igen.")


rum2()

import random
print("\nDu är nu i rum 3. ")
print("Du är ett steg från att fly från fängelset.")
print("Men det finns en vakt framför dörren.")
print("Det är för sent att vända sig om, ditt enda val är att slåss mot vakten.")
print("Vakten ser dig och förbereder sig för en fight.")

def validate_attack_input():
    while True:
        attack = input("Välj din attack (1 för slag, 2 för spark): ")
        if attack in ["1", "2"]:
            return attack
        else:
            print("Ogiltigt val! Försök igen.")

def rum3():
    ### VARIABLES FOR HEALTH ###
    player_health = 100
    enemy_health = 100

    ### VARIABLES FOR THE ATTACKS ###
    player_fist_damage = 15
    enemy_fist_damage = 15
    player_kick_damage = 20
    enemy_kick_damage = 20

    # Hit chances
    player_fist_hit_chance = 90  # 90% chance to hit
    enemy_fist_hit_chance = 85   # 85% chance to hit
    player_kick_hit_chance = 70  # 70% chance to hit
    enemy_kick_hit_chance = 65   # 65% chance to hit

    while player_health > 0 and enemy_health > 0:
        print(f"\nDin hälsa: {player_health}")
        print(f"Vaktens hälsa: {enemy_health}")

        ### SPELAREN ATTACKERAR ###
        spelarens_attack = validate_attack_input()  # Use the validation function

        if spelarens_attack == "1":
            print("Du gjorde ett slag.")
            random_number = random.randint(1, 100)

            if random_number > player_fist_hit_chance:
                print("Du missade.")
            else:
                print("Du träffade.")
                enemy_health -= player_fist_damage
                print(f"Vakten har nu {enemy_health} hälsa.")

        elif spelarens_attack == "2":
            print("Du gjorde en spark.")
            random_number = random.randint(1, 100)

            if random_number > player_kick_hit_chance:
                print("Du missade.")
            else:
                print("Du träffade.")
                enemy_health -= player_kick_damage
                print(f"Vakten har nu {enemy_health} hälsa.")

        ### MOTSTÅNDAREN ATTACKERAR ###
        if enemy_health > 0:  # Only attack if the enemy is still alive
            print("\nDet är vaktens tur att attackera.")
            motståndaren_attack = random.choice([1, 2])
            slump_tal = random.randint(1, 100)

            if motståndaren_attack == 1:
                print("Vakten försöker slå dig.")
                if slump_tal <= enemy_fist_hit_chance:
                    print("Och träffar!")
                    player_health -= enemy_fist_damage
                    print(f"Du tar {enemy_fist_damage} i skada och har {player_health} hälsopoäng kvar.")
                else:
                    print("Och missar.")

            elif motståndaren_attack == 2:
                print("Vakten försöker sparka dig.")
                if slump_tal <= enemy_kick_hit_chance:
                    print("Och träffar!")
                    player_health -= enemy_kick_damage
                    print(f"Du tar {enemy_kick_damage} i skada och har {player_health} hälsopoäng kvar.")
                else:
                    print("Och missar.")

    ### GAME OVER LOGIC ###
    if player_health <= 0 and enemy_health <= 0:
        print("\nDet blev oavgjort. Båda förlorade.")
        cell()
    elif player_health <= 0:
        print("\nVakten vann. Du förlorade.")
        cell()
    elif enemy_health <= 0:
        print("\nDU VANN! Du besegrade vakten och är fri.")

rum3()