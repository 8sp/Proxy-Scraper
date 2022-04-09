import requests
import colorama
import os 
import time
import random
from colorama import Fore
from os import system
from os import system
colorama.init(autoreset=True)
system("title " + "Proxy-Scraper - By Null")



# FILES

https_file = open("https.txt","a") 
socks4_file = open("socks4.txt", "a")
http_file = open("http.txt", "a")
socks5_file = open("socks5.txt", "a")


# REQUEST API

rhttps = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rhttp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')
rs4 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4')
rs5 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5')


# HTTPS

https = []
https = rhttps.text
https = https.split()
lines = len(https)


# HTTP

http = []
http = rhttp.text
http = http.split()
hlines = len(http)


# SOCKS 4

socks4 = []
socks4 = rs4.text
socks4 = socks4.split()
slines = len(socks4)

# SOCKS 5

socks5 = []
socks5 = rs5.text
socks5 = socks5.split()
sslines = len(socks5)


number = random.randint(1, 5)

def getsocks4():
    for i in range(number):
        print("[HTTPS] " + https[number])
        time.sleep(0.1)




def getsocks5():
    for b in range(number):
        print("[SOCKS5] " + socks5[number])
        time.sleep(0.1)



def main():
    print(f"""
{Fore.CYAN} _                     _          {Fore.RESET}   
{Fore.CYAN}| |   _   _ _ __   ___| |__       {Fore.RESET}  
{Fore.CYAN}| |  | | | | '_ \ / __| '_ \      {Fore.RESET} 
{Fore.CYAN}| |__| |_| | | | | (__| | | |     {Fore.RESET}
{Fore.CYAN}|_____\__, |_| |_|\___|_| |_|     {Fore.RESET}
{Fore.CYAN}      |___/                       {Fore.RESET}
""")
    print(f"[{Fore.MAGENTA}1{Fore.RESET}] " + "HTTPS")
    print(f"[{Fore.MAGENTA}2{Fore.RESET}] " + "HTTP")
    print(f"[{Fore.MAGENTA}3{Fore.RESET}] " + "SOCKS4")
    print(f"[{Fore.MAGENTA}4{Fore.RESET}] " + "SOCKS5")
    print(f"[{Fore.MAGENTA}5{Fore.RESET}] " + "ABOUT")
    Type = input(">> ")
    if(Type == "1"):
        for n in range(lines):
            print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Found HTTPS >> " + https[n])
            https_file.write('\n' + https[n])
            time.sleep(0.1)
    elif(Type == "2"):
        for a in range(hlines):
            print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Found HTTP >> " + http[a])
            http_file.write('\n' + http[a])
            time.sleep(0.1)
    elif(Type == "3"):
        for v in range(slines):
            print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Found SOCKS4 >> " + socks4[v])
            socks4_file.write('\n' + socks4[v])
            time.sleep(0.1)
    elif(Type == "4"):
        for i in range(sslines):
            print(f"[{Fore.GREEN}+{Fore.RESET}] Successfully Found SOCKS5 >> " + socks5[i])
            socks5_file.write('\n' + socks5[i])
            time.sleep(0.1)
    elif(Type == "5"):
            print(f"[{Fore.CYAN}i{Fore.RESET}] Fully Written By Lynch, Known As @l7up")
            exit()  
            time.sleep(0.1)    
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] Error, No Mode Found")
        exit()


    



if __name__ == "__main__":

    main()
    print(f"[{Fore.CYAN}i{Fore.RESET}] All Proxy's Successfully Grabbed & Saved")
