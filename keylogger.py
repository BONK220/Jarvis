import os, pyfiglet

baner = pyfiglet.figlet_format("Keylogger V 1.0")
subbaner = pyfiglet.figlet_format("Autor: BONK")

Login = "stary"
Haslo = "ButlaZG@zem69"
def logowanie():
    os.system("cls")
    print("~" * 50)
    print("\n")
    print("\n")
    login1 = input("Login: ")
    haslo1 = input("Hasło: ")
    if login1 != Login:
        print("Podano zly login")
        os.system("cls")
        logowanie()
    else:
        print("Dobry login!")
        os.system("cls")

    if haslo1 != Haslo:
        print("Podano zle haslo")
        os.system("cls")
        logowanie()

    else:
        print("Dobre Hasło!")
        os.system("cls")
print(baner)
print(subbaner)
print("Aby uzyskać dostęp do programu proszę wprowadzić poprawny login i hasło")
print("\n" * 2)
logowanie()
os.system("python jarvis.py")


