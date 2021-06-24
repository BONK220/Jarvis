import pyfiglet, sys, socket, os
from datetime import datetime as dt
def nl():
    print('\n')


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    nl()
    print("Zle zdefiniowany parametr wejścia")
    print("Syntax --> python3 portscanner.py <IP Address>")
    nl()

#Baner
baner = pyfiglet.figlet_format("Skaner portów V 1.0")
print(baner)

#koneic baneru

nl()
print("~" * 50)
print("Czas startu: {}" .format(dt.now()))
print("~" * 50)
nl()

try:
    for port in range (18,255):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print("<--Port {} jest otwarty i niefiltrowany-->".format(port))
            s.close
except KeyboardInterrupt:
    print("<~Przerwany skan~>")
    print("~" * 100)
    print("Czy chcesz powrócić do Jarvisa?")
    p = input("Tak lub nie")
    if p == "Tak" or "tak":
        os.system("cls")
        print("Przywracam Jarvisa")
        os.system("cls")
        os.system("python jarvis.py")
    if p == "Nie" or "nie":
        exit(0)
except socket.gaierror:
    print("<~!Niepoprawna nazwa hosta~>!")
    print("~" * 100)
    print("Czy chcesz powrócić do Jarvisa?")
    p = input("Tak lub nie")
    if p == "Tak" or "tak":
        os.system("cls")
        print("Przywracam Jarvisa")
        os.system("cls")
        os.system("python jarvis.py")
    if p == "Nie" or "nie":
        exit(0)

except socket.gaierror:
    print("<~!Błąd połączenia!~>")
    print("~" * 100)
    print("Czy chcesz powrócić do Jarvisa?")
    p = input("Tak lub nie")
    if p == "Tak" or "tak":
        os.system("cls")
        print("Przywracam Jarvisa")
        os.system("cls")
        os.system("python jarvis.py")
    if p == "Nie" or "nie":
        exit(0)






















