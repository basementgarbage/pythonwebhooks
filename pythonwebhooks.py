from cfg import *
import os
from time import sleep
try:
    import discordwebhook
except ImportError:
    print('whoops. the required packages arent installed. please install from requirements.txt')
    
from discordwebhook import Discord

discord = Discord(url=wh)

print("""

    Created by website37 <3
     Type anything to send to your webhook
      If you are getting a error whilst sending please configure your webhook in cfg.py
""")
sleep(2)

os.system('cls')

print("""
 ________  ___    ___ _________  ___  ___  ________  ________           ___       __   _______   ________  ___  ___  ________  ________  ___  __    ________      
|\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \        |\  \     |\  \|\  ___ \ |\   __  \|\  \|\  \|\   __  \|\   __  \|\  \|\  \ |\   ____\     
\ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \       \ \  \    \ \  \ \   __/|\ \  \|\ /\ \  \\\  \ \  \|\  \ \  \|\  \ \  \/  /|\ \  \___|_    
 \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \       \ \  \  __\ \  \ \  \_|/_\ \   __  \ \   __  \ \  \\\  \ \  \\\  \ \   ___  \ \_____  \   
  \ \  \___|\/  /  /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \       \ \  \|\__\_\  \ \  \_|\ \ \  \|\  \ \  \ \  \ \  \\\  \ \  \\\  \ \  \\ \  \|____|\  \  
   \ \__\ __/  / /          \ \__\ \ \__\ \__\ \_______\ \__\\ \__\       \ \____________\ \_______\ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\____\_\  \ 
    \|__||\___/ /            \|__|  \|__|\|__|\|_______|\|__| \|__|        \|____________|\|_______|\|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\_________\
         \|___|/                                                                                                                                      \|_________|
""")

message = input(">")

discord.post(
    content=message,
    username=username,
    avatar_url=pfp
)
