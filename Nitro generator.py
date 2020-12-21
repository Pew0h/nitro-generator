import random, string
from colorama import init, Fore
import webbrowser
import time
import requests

print("%s ******* Nitro generator and checker By Pewoh ********%s" % (Fore.CYAN, Fore.WHITE))

num=input('%sHow many codes do you want ? ' % (Fore.WHITE))

f=open("generated_codes.txt","w", encoding='utf-8')
valid = open("valid.txt", "a")

################# GENERATED CODES #######################
for n in range(int(num)):
   code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
   f.write('https://discord.gift/')
   f.write(code)
   f.write("\n")
f.close()


################# CHECKER #######################
with open("generated_codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
        r = requests.get(url)
        if r.status_code == 200:
            print(" %Valid | {} ".format(line.strip("\n")) % (Fore.GREEN))
            valid.write(line.strip("\n") + '\n')
            break
        else:
            print("%sNot valid | {} ".format(line.strip("\n")) % (Fore.RED))

input("%sProgram shutdown ! [Enter] to quit !" % (Fore.YELLOW))