import os
import sys
import configparser

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Setup Wizard")

banner()

config_file                 = 'config.ini'

nansen_info                 = configparser.RawConfigParser()
nansen_info.add_section('info')

xtoken                      = input("[+] Enter Nansen API Token: ")
nansen_info.set('info', 'nansen_token', xtoken)

with open(config_file, 'w') as setup:
    nansen_info.write(setup)

print("[+] Setup completed successfully")