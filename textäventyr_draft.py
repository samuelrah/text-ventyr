meny = ("1")

while True:
    print("Meny")
    print("1- starta spelet")

    meny_input = input("skriv ett nummer:")

    if meny_input in meny:
        meny_input == "1"
        print("starta spel.")

    else:
        print ("ogiltigt vall försök igen.")



def rum_1():
    print ("Du har ")