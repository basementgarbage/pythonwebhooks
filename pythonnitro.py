import random
import string
from cfg import *
import os
from time import sleep
try:
    import discordwebhook
except ImportError:
    print('whoops. the required packages arent installed. please install from requirements.txt')
    
from discordwebhook import Discord

discord = Discord(url=wh)
dscrdlink = "http://discord.gift/"
print("""

    Created by website37 <3
     it should auto generate to your webhook
      If you are getting a error whilst sending please configure your webhook in cfg.py
""")
sleep(2)

os.system('cls')

print(""" 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢹⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠄⢠⣴⣾⣵⣶⣶⣾⣿⣦⡄⠄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⢀⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⡄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⢸⣿⣿⣧⣀⣼⣿⣄⣠⣿⣿⣿⠄⠄⢸⣿⣿⣿  PYTHON NIRO GEN
⣿⣿⣿⡇⠄⠄⠘⠻⢷⡯⠛⠛⠛⠛⢫⣿⠟⠛⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿   STARTING NOW!
⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢡⣀⠄⠄⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⣸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                                                                                                           """)

count = 0
while True == True:
    discord.post(
        content= dscrdlink + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16)),
        username=username,
        avatar_url=pfp
    )
    count = count + 1
    print("Sent! |", count + 1)
print(dscrdlink + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16)))

