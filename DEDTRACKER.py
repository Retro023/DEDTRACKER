import json
import requests
import time
from tqdm import tqdm
# kown mal IPs
def gather_known_ips():
    return [
    '103.251.167.20',
    '108.77.13.78',
    '109.70.100.6',
    '109.70.100.67',
    '109.70.100.70',
    '109.70.100.71',
    '136.34.129.71',
    '185.220.101.24',
    '185.243.218.202',
    '192.42.116.173',
    '192.42.116.179',
    '192.42.116.184',
    '192.42.116.185',
    '192.42.116.187',
    '192.42.116.188', 
    '192.42.116.192',
    '192.42.116.198',
    '192.42.116.200',
    '198.251.88.70',
    '199.172.47.13',
    '23.137.251.61',
    '2a0b:f4c2:1::1',
    '38.97.116.244',
    '47.185.81.143',
    '47.196.190.73',
    '50.203.7.250',
    '50.225.7.154',
    '50.232.69.26',
    '68.185.212.57',
    '69.162.231.243',
    '69.245.177.224',
    '70.23.242.94',
    '71.207.162.163',
    '71.230.25.169',
    '72.204.184.234',
    '76.8.187.168',
    '98.53.226.84',
    '99.9.223.72',
    '103.43.141.36',
    '45.117.142.107',
    '27.86.5.221',
    '45.116.226.78',
    '141.237.186.217',
    '103.240.252.215',
    '157.245.201.168',
    '45.116.226.76',
    '18.209.138.149',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    '203.138.203.5',
    '27.86.5.217',
    '42.84.66.224',
    '203.138.203.195',
    '45.116.226.73',
    '188.127.251.131',
    '45.116.226.72',
    '42.6.176.47',
    '103.43.140.27',
    '103.43.140.24',
    '103.240.252.209',
    '149.28.44.107',
    '119.115.98.144',
    '209.85.160.60',
    '103.43.140.160'
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
# gathering geo data
def gather_ip():
    return input("Please supply the IP: ")

def fetch_geolocation_data(ip):
    request_url = f'https://geolocation-db.com/jsonp/' + ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    return result

# saving data to file
def save_to_output_file(json_object):
    json_string = json.dumps(json_object, indent=4)
    with open('output.txt', 'a') as outfile:
        outfile.write(json_string)

def read_output_file():
    with open('output.txt', 'r') as f:
        return f.read()
# checking ip against mal ip list
def check_ip_maliciousness(ip, known_ips):
    if ip in known_ips:
        print(f"{ip} is a known malicious IP.")
    else:
        print(f"{ip} is not known to be malicious. Consider adding it to the list.")

        new_ip = input("Please add the IP to the list (write the IP) or press enter to skip: ")
        if new_ip:
            known_ips.append(new_ip)
# checking if user ahs virus total api key
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
# running script
def main():
    display_banner()
    known_ips = gather_known_ips()
    ip = gather_ip()
    # loading bar
    print(f"Scanning {ip}")
    for _ in tqdm(range(5)):
        time.sleep(0.5)
    
    check_ip_maliciousness(ip, known_ips)
    use_virustotal_api(ip)

if __name__ == "__main__":
    main()
