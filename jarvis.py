import speech_recognition as sr
import pyttsx3 as tts
import os, sys, time, subprocess, pyfiglet, time, pyglet

#sciezka
def pathFinder():
	pathfrag1 = os.path.dirname(sys.argv[0])
	path1 = os.path.abspath(pathfrag)


pathfrag = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathfrag)
pathvaild = path + "\\"

#baner
baner = pyfiglet.figlet_format("Jarvis V 1.03")
baner1 = pyfiglet.figlet_format("Uwaga: Niektóre funkcje moga byc niestabilne.")
baner2 = pyfiglet.figlet_format("Czekaj na kolejne patche")

# Obiekty
r = sr.Recognizer()
engine = tts.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)

#sciezka
chrome= 'C:\\"Program Files"\\"Google"\\"Chrome"\\"Application"\\chrome.exe'

#sciezki do programow
eksplorator_plikow= 'explorer.exe'
steam= 'C:\\"Program Files (x86)"\\"Steam"\\steam.exe'
epic= 'C:\\"Program Files (x86)"\\"Epic Games"\\"Launcher"\\"Portal"\\"Binaries"\\"Win32"\\EpicGamesLauncher.exe'
minecraft= 'C:\\"Program Files (x86)"\\"Minecraft Launcher"\\MinecraftLauncher.exe'
cmd='C:\\"Windows"\\"System32"\\cmd.exe'

#repozytoria muzyki
muzyka_szukaj= path + '\\repozytorium_muzyki_jarvisa'

#skaner portow
SkanerPortow = "SkanerPortow.py 192.168.0.1"

#skaner urzadzen
SkanerUrzadzen = "SkanerPodsieci.py"


def speak(text):
	engine.say(text)
	engine.runAndWait()

def getText():
	try:
		with sr.Microphone() as source:
			print("...", end='\r')
			audio = r.listen(source)
			text = r.recognize_google(audio, language="pl-PL")
			if text == "":
				return "None"
			else:
				return text
	except:
		return "None"

def czy_zawiera(string, slowa):
	return [element for element in slowa if element in string.lower()]

#	for element in slowa:
#		if element in string.lower():
#			lista.append(element)
# return lista

# Stałe listy funkcji
WYBORY_POZYTYWNE = ['Tak', 'tak']
WYBORY_NEGATYWNE = ['Nie', 'nie']
WYKRYJ = ['jarvis','bot', 'robot', 'robocie']
DOWIDZENIA = ['do widzenia', 'do widzenia', 'pa', 'wyłącz się']
SZUKAJ = ['wyszukaj', 'szukaj', 'przeglądarka', 'google']
YOUTUBE = ['youtube']
URUCHOM = ['Uruchom', 'włącz']
STEAM = ['steam', 'steama']
EPIC = ['Epic Games', 'Epic']
MINECRAFT = ['MC', 'Minecraft', 'Minecrafta']
SKANERPORTOW = ['skanuj otwarte porty']
SKANERURZADZEN = ['skanuj aktywne urządzenia']
CMD = ['cmd']
ZAPISZ_DO_PLIKU = ['zapisz']
WCZYTAJ_Z_PLIKU = ['wczytaj']
USUN_PLIK = ['usuń', 'usuń plik', 'usuń plik dziennika']
ODPAL_MUZYKĘ = ['puść muzykę', 'muzyka']
WITAJ = ['Witaj', 'jak mija Ci dzień']
DODAWANIE = ['dodaj', 'dodaj liczby', 'wykonaj działanie dodawania']
ODEJMOWANIE = ['odejmij', 'wykonaj działanie odejmowania', 'odejmij liczby']
MNOZENIE = ['pomnóż', 'pomnóż liczby', 'wykonaj działanie mnożenia']
DZIELENIE = ['podziel', 'podziel liczby', 'wykonaj działanie mnożenia']
POTEGOWANIE = ['potęguj']
WYLACZANIE = ['wyłącz komputer', 'wyłącz']
ANULUJ = ['anuluj wyłączanie komputera', 'anuluj']
RESTART_FUNKCJI_RECOGNIZERA = ['restart', 'restartuj się', 'restart funkcji']
PRZEJDZ_DO_SCIEZKI = ['twój folder', 'folder']
HOOJ_CI_W_DUPE = ['chuj ci w dupe', 'huj ci w dupe']

os.system("cls")
pathFinder()
print(baner)
print(baner1)
print(baner2)
print("Aby wyjść powiedz 'do widzenia'")
while True:
	time.sleep(0.5)
	cur = getText()
	print(cur)
	print(" "*50, end="\r")
	if cur != None:
		if len(czy_zawiera(cur, WYKRYJ)):
			if len(czy_zawiera(cur, DOWIDZENIA)):
				speak("Żegnaj.")
				os.system("cls")
				exit(0)
				os.system("exit")
				break
			elif len(czy_zawiera(cur, SZUKAJ)):
				linczek = cur.lower().split(' ' + czy_zawiera(cur, SZUKAJ)[0] + ' ')[1]
				speak("szukam")
				url = "https://www.google.com/search?q=" + linczek.replace(" ", "+").replace("?", "%3F")
				os.system(chrome + " " + url)
				os.system("python jarvis.py")
				exit(0)

			elif len(czy_zawiera(cur, YOUTUBE)):
				linczekY = cur.lower().split(' ' + czy_zawiera(cur, YOUTUBE)[0] + ' ')[0]
				speak("odpalam")
				urlY = "https://www.youtube.com"
				os.system(chrome + " " + urlY)
#uruchamianie steam
			elif len(czy_zawiera(cur, STEAM)):
				os.system(steam)

			elif len(czy_zawiera(cur, EPIC)):
				os.system(epic)

			elif len(czy_zawiera(cur, MINECRAFT)):
				os.system(minecraft)

#skaner portow
			elif len(czy_zawiera(cur, SKANERPORTOW)):
				os.system("python" + " " + SkanerPortow)

			elif len(czy_zawiera(cur, SKANERURZADZEN)):
				os.system("python" + " " + SkanerUrzadzen)

			elif len(czy_zawiera(cur, CMD)):
				os.system(cmd)

#Zapisywanie pliku
			elif len(czy_zawiera(cur, ZAPISZ_DO_PLIKU)):
				speak("Podaj nazwępliku do którego chcesz coś dopisać, lub stworzyć.")
				speak("podaj nazwę pliku:")
				nazwa = getText()
				nazwa_wlasciwa3 = nazwa + ".txt"
				f = open(nazwa_wlasciwa3, mode="a+")
				speak("podaj treść:")
				tresc = getText()
				f.write(tresc)
				speak("zapisano")
				f.close()

#Wczytywanie pliku
			elif len(czy_zawiera(cur, WCZYTAJ_Z_PLIKU)):
				speak("Podaj Nazwę pliku z którego wczytać")
				nazwa1 = getText()
				nazwa_wlasciwa1 = nazwa1 + ".txt"
				f = open(nazwa_wlasciwa1, mode="r")
				speak(f.readlines())
				f.close()

#usuwanie pliku
			elif len(czy_zawiera(cur, USUN_PLIK)):
				speak("podaj nazwę pliku, który chcesz usunąć")
				nazwa2 = getText()
				nazwa_wlasciwa2 = nazwa2 + ".txt"
				os.system("del" + " " + nazwa_wlasciwa2)

#puszczanie muzyki
			elif len(czy_zawiera(cur, ODPAL_MUZYKĘ)):
				speak("podaj folder z którego chcesz wziąć muzykę")
				folder = getText()
				speak("podaj tytuł piosenki")
				muzyka = getText()
				muzyka_tytuł = muzyka + ".mp3"
				print(muzyka_szukaj + "\\" + folder + "\\" + muzyka_tytuł)
				os.system(muzyka_szukaj + '\\'  + '"' + folder + '"' +'\\' + '"' + muzyka_tytuł + '"')
				os.system("python jarvis.py")
				exit(0)


#witanie
			elif len(czy_zawiera(cur, WITAJ)):
				speak("Witaj, jak mija Ci dzień")

#dodawanie
			elif len(czy_zawiera(cur, DODAWANIE)):
				speak("podaj pierwszą liczbę")
				a = int(input("liczba: "))
				b = int(input("liczba: "))
				c = a + b
				print("Wynik = ", c)

			elif len(czy_zawiera(cur, ODEJMOWANIE)):
				speak("podaj pierwszą liczbę")
				a = int(input("liczba: "))
				b = int(input("liczba: "))
				c = a - b
				print("Wynik = ", c)

			elif len(czy_zawiera(cur, MNOZENIE)):
				speak("podaj pierwszą liczbę")
				a = int(input("liczba: "))
				b = int(input("liczba: "))
				c = a * b
				print("Wynik = ", c)

			elif len(czy_zawiera(cur, DZIELENIE)):
				speak("podaj pierwszą liczbę")
				a = int(input("liczba: "))
				b = int(input("liczba: "))
				c = a / b
				print("Wynik = ", c)

			elif len(czy_zawiera(cur, POTEGOWANIE)):
				speak("podaj pierwszą liczbę")
				a = int(input("liczba: "))
				speak("przez ile spotęgować")
				b = int(input("liczba: "))
				c = a ** b
				print("Wynik = ", c)

			elif len(czy_zawiera(cur, WYLACZANIE)):
				speak("rozpoczynam wyłączanie komputera")
				os.system("shutdown /s -t 60")

			elif len(czy_zawiera(cur, ANULUJ)):
				speak("anuluje zaplanowane wyłączenie")
				os.system("shutdown /a")

			elif len(czy_zawiera(cur, RESTART_FUNKCJI_RECOGNIZERA)):
				speak("Wykryto błąd! Restart Za trzy")
				time.sleep(0.1)
				speak("dwa")
				time.sleep(0.1)
				speak("jeden")
				time.sleep(0.1)
				os.system("python jarvis.py")

			elif len(czy_zawiera(cur, PRZEJDZ_DO_SCIEZKI)):
				os.system("explorer.exe " + path)
			
			
			elif len(czy_zawiera(cur, HOOJ_CI_W_DUPE)):
				speak("Nawzajem")




	else:
		KeyboardInterrupt















