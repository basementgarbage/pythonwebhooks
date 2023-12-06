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
     Type anything to spam to your webhook
      If you are getting a error whilst sending please configure your webhook in cfg.py
""")
sleep(2)

os.system('cls')

print(""" 
 ________  ___    ___ _________  ___  ___  ________  ________           ________  ________  ________  _____ ______   _____ ______   _______   ________     
|\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \        |\   ____\|\   __  \|\   __  \|\   _ \  _   \|\   _ \  _   \|\  ___ \ |\   __  \    
\ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \       \ \  \___|\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \   __/|\ \  \|\  \   
 \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \       \ \_____  \ \   ____\ \   __  \ \  \\|__| \  \ \  \\|__| \  \ \  \_|/_\ \   _  _\  
  \ \  \___|\/  /  /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \       \|____|\  \ \  \___|\ \  \ \  \ \  \    \ \  \ \  \    \ \  \ \  \_|\ \ \  \\  \| 
   \ \__\ __/  / /          \ \__\ \ \__\ \__\ \_______\ \__\\ \__\        ____\_\  \ \__\    \ \__\ \__\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ _\ 
    \|__||\___/ /            \|__|  \|__|\|__|\|_______|\|__| \|__|       |\_________\|__|     \|__|\|__|\|__|     \|__|\|__|     \|__|\|_______|\|__|\|__|
         \|___|/                                                          \|_________|                                                                     
                                                                                                                                                           
                                                                                                                                                           """)

message = input(">")
count = 0
while True == True:
    discord.post(
        content=message,
        username=username,
        avatar_url=pfp
    )
    count = count + 1
    print("Sent! |", count + 1)
