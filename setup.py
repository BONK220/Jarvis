import os, sys

pathfrag = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathfrag)
pathvaild = path + '\\'


os.system(pathvaild + "PythonInterpreterInstall.exe")
os.system("pip install pyinstaller")
os.system("pip install " + pathvaild + "PyAudio-0.2.11-cp39-cp39-win_amd64.whl")
os.system("pip install pyttsx3")
os.system("md repozytorium_muzyki_jarvisa")
f = open("repozytorium_muzyki_jarvisa/README IMPORTANT.txt", mode="a+")
f.write("Jak Będziesz dodawał muzykę, musisz posegregować ją w foldery. Foldery te mogą normalnie zawierać spacje. Ale muzyka \nmusi być ponazywana tylko tytułami, bo jarvis jej nie znajdzie (np. California.mp3) \nMuzyka musi mieć rozszerzenie .mp3.")
os.system('pyinstaller --onefile "gui.py" -i jarvis.ico')
os.system("move " + pathvaild + "dist\gui.exe" + " " + pathvaild)
os.system("ren gui.exe jarvis.exe")
os.system("rmdir /Q /S " + pathvaild + "__pycache__")
os.system("rmdir /Q /S " + pathvaild + "build")
os.system("rmdir /Q /S " + pathvaild + "dist")
os.system("del gui.spec")
os.system("pip install tkinter")
os.system("pip install speech_recognition")
os.system("pip install speechrecognition")
os.system("pip install pyfiglet")
os.system("pip install pyaudio")
os.system("mklink Jarvis " + pathvaild + "jarvis.exe")
os.system("move jarvis.symlink %userprofile%\Desktop")
exit(0)