#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author Mute3very
import json
import requests
import time
from tqdm import tqdm
#banner stuff
bred = "\033[1;31m"
banner = f""" {bred}

▓█████▄ ▓█████ ▓█████▄ ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██▀ ██▌▓█   ▀ ▒██▀ ██▌▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒███   ░██   █▌▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░▒████▒░▒████▓   ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒     ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░    ░    ░ ░  ░   ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
   ░       ░  ░   ░                ░           ░  ░░ ░      ░  ░      ░  ░   ░     
 ░              ░                                  ░                               
"""

print (banner)
# gathering ip
x = input ("Please supply the ip:   ")

print(f"scanning", x )
# loading bar
for i in tqdm(range(5)):
    time.sleep(0.5)
# fetching geo data
def get_geolocation_data(x):
    request_url = f'https://geolocation-db.com/jsonp/' + x
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    return result

# saving the data to json file
def save_to_output_file(json_object):
    json_string = json.dumps(json_object, indent=4)
    with open('output.txt', 'a') as outfile:
        outfile.write(json_string)
# printing the file out
def read_output_file():
    with open('output.txt', 'r') as f:
        return f.read()
     
