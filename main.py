# Imports
from pytube import YouTube
import os
import sys
import time
import colorama
from colorama import Fore
import string

# Initialisation colorama / Colorama initialization
colorama.init(autoreset=True)

# Couleurs
RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE

# Message de bienvenue / Welcome message
welcome_msg = f"""{RED}
 _____      _____        _____     ____   ____      _____    _____      _____ 
|\    \    /    /|  ____|\    \   |    | |    | ___|\    \  |\    \    /    /|
| \    \  /    / | /     /\    \  |    | |    ||    |\    \ | \    \  /    / |
|  \____\/    /  //     /  \    \ |    | |    ||    | |    ||  \____\/    /  /
 \ |    /    /  /|     |    |    ||    | |    ||    |/____/| \ |    /    /  / 
  \|___/    /  / |     |    |    ||    | |    ||    ||    ||  \|___/    /  /  
      /    /  /  |\     \  /    /||    | |    ||    ||____|/      /    /  /   
     /____/  /   | \_____\/____/ ||\___\_|____||____|            /____/  /    
    |`    | /     \ |    ||    | /| |    |    ||    |           |`    | /     
    |_____|/       \|____||____|/  \|____|____||____|           |_____|/      
       )/             \(    )/        \(   )/    \(                )/         
       '               '    '          '   '      '                '          
                         -> {RED}By: Fsubject.xyz <-"""

functionality = f"""
{WHITE}[{RED}1{WHITE}] Get YouTube video informations
{WHITE}[{RED}2{WHITE}] Download YouTube video
"""

# Initialisation du programme / Program initialization
def initialization():
    clear(welcome_msg)

    check_modules(modules=["pytube","os","sys","time","colorama","string"])
    wait(2)
    clear(welcome_msg)

    print(functionality)

    while True:
        choice = input(f"{WHITE}Your choice {RED}-> {WHITE}")

        if choice == str(1):
            clear("")
            get_vid_info()
        elif choice == str(2):
            clear("")
            video_downloader()
        elif choice == "reprint":
            print(f"{WHITE}[{RED}WARNING{WHITE}] Please wait {RED}2 seconds {WHITE}.")
            clear(welcome_msg)
            print(functionality)
        elif choice == "exit":
            clear("")
            print(f"{WHITE}[{RED}WARNING{WHITE}] Closing...")
            wait(1)
            sys.exit()
        else:
            print(f"{WHITE}[{RED}WARNING{WHITE}] Please enter a {RED}correct {WHITE}number.")

# Fonction de récupération d'information / Get video informations function
def get_vid_info():
    clear(welcome_msg)
    print("\n")

    vid_link = input(f"{WHITE}Please enter the video link {RED}-> {WHITE}")
    yt = YouTube(vid_link)

    info = f"""
    {WHITE}Title {RED}-> {WHITE}{yt.title}.
    {WHITE}Views {RED}-> {WHITE}{yt.views}.
    {WHITE}Length {RED}-> {WHITE}{yt.length} seconds.
    {WHITE}Publish date {RED}-> {WHITE}{yt.publish_date}.
    {WHITE}Author {RED}-> {WHITE}{yt.author}.
    {WHITE}Age restricted {RED}-> {WHITE}{yt.age_restricted}.
    """

    print(info)
    print(f"{WHITE}[{RED}WARNING{WHITE}] Please wait {RED}10 seconds {WHITE}.")
    wait(10)
    clear(welcome_msg)
    print(functionality)

# Fonction de téléchargement de video / Download video function
def video_downloader():
    clear(welcome_msg)
    print("\n")

    vid_link = input(f"{WHITE}Please enter the video link {RED}-> {WHITE}")
    yt = YouTube(vid_link)

    ys = yt.streams.get_highest_resolution()

    download_folder = input(f"{WHITE}Where do you want to download the video (Enter for default folder) {RED}-> {WHITE}")
    if len(download_folder) > 1:
        clear(welcome_msg)
        print(f"\n{WHITE}[{RED}WARNING{WHITE}] Downloading...")
        ys.download(download_folder)
    else:
        clear(welcome_msg)
        print(f"\n{WHITE}[{RED}WARNING{WHITE}] Downloading...")
        ys.download("Video")

    print(f"{WHITE}[{RED}WARNING{WHITE}] Download completed!")
    wait(2)

    clear(welcome_msg)
    print(f"\n{WHITE}[{RED}WARNING{WHITE}] Please wait {RED}5 seconds {WHITE}.")

    wait(5)
    clear(welcome_msg)
    print(functionality)

# Fonction d'attente / Waiting function
def wait(timer: float) -> float:
    time.sleep(timer)

# Fonction de clear / Clear terminal function
def clear(args: string) -> string:
    if len(args) > 1:
        os.system("cls || clear")
        wait(0.1)
        print(args)
    else:
        os.system("cls || clear")

# Fonction de vérification des imports / Check modules function
def check_modules(modules: list) -> list:
    print("\n")
    for i in modules:
        if i in sys.modules:
            wait(0.3)
            print(f"{WHITE}[{GREEN}OK{WHITE}] " + string.capwords(i) + " module has been initialized.")
        else:
            wait(0.3)
            print(f"{WHITE}[{RED}ERROR{WHITE}] " + string.capwords(i) + " module cannot been initialized.")
            sys.exit()

initialization()