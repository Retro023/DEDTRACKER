import json
import requests
import time
from tqdm import tqdm

def gather_known_ips():
    return [
        # Your list of known malicious IPs
    ]

def display_banner():
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
 ░              ░      
"""


    
    print(banner)

def gather_ip():
    return input("Please supply the IP: ")

def fetch_geolocation_data(ip):
    request_url = f'https://geolocation-db.com/jsonp/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    return result

def save_to_output_file(json_object):
    json_string = json.dumps(json_object, indent=4)
    with open('output.txt', 'a') as outfile:
        outfile.write(json_string)

def read_output_file():
    with open('output.txt', 'r') as f:
        return f.read()

def check_ip_maliciousness(ip, known_ips):
    if ip in known_ips:
        print(f"{ip} is a known malicious IP.")
    else:
        print(f"{ip} is not known to be malicious. Consider adding it to the list.")

        new_ip = input("Please add the IP to the list (write the IP) or press enter to skip: ")
        if new_ip:
            known_ips.append(new_ip)

def use_virustotal_api(ip):
    api_key = None

    while True:
        api_check = input("Do you have a VirusTotal API key? (Y/N): ")

        if api_check == 'Y':
            api_key = input("Please supply the API key: ")
            break
        elif api_check == 'N':
            print("This script is greatly improved if you have a VirusTotal API key.")
            break
        else:
            print("Error: unknown input. Please use Y or N.")

    if api_key:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
        headers = {
            "accept": "application/json",
            "x-apikey": api_key
        }
        response = requests.get(url, headers=headers)

        with open('virustotal_result.txt', 'a') as f:
            f.write(response.text)
        print("VirusTotal result has been added to virustotal_result.txt")

def main():
    display_banner()
    known_ips = gather_known_ips()
    ip = gather_ip()
    
    print(f"Scanning {ip}")
    for _ in tqdm(range(5)):
        time.sleep(0.5)
    
    check_ip_maliciousness(ip, known_ips)
    use_virustotal_api(ip)

if __name__ == "__main__":
    main()
