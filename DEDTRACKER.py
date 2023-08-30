  GNU nano 7.2                                                                                       dedtracker.py *                                                                                               
#!/usr/bin/env python3
#author Mute3very
import json
import requests
import time
#banner stuff
bred = "\033[1;31m"
purple = "\033[1;31m"


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

x = input("please supply the ip addr: " )

print ("scanning" ,x)
time.sleep(1)
#gathering the info
request_url = f'https://geolocation-db.com/jsonp/' + x
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
json_object = result

# storing the json output to an output file
json_object = json.dumps(result, indent=4)
with open('output.txt' , 'a') as outfile:
        outfile.write(json_object)
f = open("output.txt" , "r")
print(f.read())
