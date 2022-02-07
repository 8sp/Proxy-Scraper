try:
    import requests
    import os
    import time
    from os import system, path
    import json
    import threading
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    system("title " + "Programmed By Lynch - Proxy Tool")

except Exception as m:
    print(m)
    input("Press Any Key To Exit...\n")
    exit()

a = requests.Session()


def mode():
    print(f"""
 {Fore.CYAN} _                     _      {Fore.RESET}
 {Fore.CYAN}| |   _   _ _ __   ___| |__   {Fore.RESET}
 {Fore.CYAN}| |  | | | | '_ \ / __| '_ \  {Fore.RESET}
 {Fore.CYAN}| |__| |_| | | | | (__| | | | {Fore.RESET}
 {Fore.CYAN}|_____\__, |_| |_|\___|_| |_| {Fore.RESET}
 {Fore.CYAN}      |___/                   {Fore.RESET}
 """)
    print(f"{Fore.RED}Made w Love By Lynch, [i]: @l7up{Fore.RESET}")
    noe = int(input(f"""[{Fore.MAGENTA}1{Fore.RESET}] HTTP/S Proxy
[{Fore.MAGENTA}2{Fore.RESET}] Socks4 Proxy
[{Fore.MAGENTA}3{Fore.RESET}] Socks5 Proxy
[{Fore.MAGENTA}4{Fore.RESET}] Proxy Checker
[{Fore.MAGENTA}99{Fore.RESET}] Exit\n>> """))
    if noe == 1:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        res = a.get(url)
        cou = res.text.count(":")
        ress = res.text.replace("\n", "")
        print(f"[{Fore.GREEN}+{Fore.RESET}] Grabbed & Saved {cou} HTTP/S Proxy")
        with open("HTTPS.txt", "a") as Proxyy:
            Proxyy.write(ress)
            input(f"[{Fore.CYAN}${Fore.RESET}] Press Any Key To Exit...\n")

    elif noe == 2:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
        res = a.get(url)
        cou = res.text.count(":")
        ress = res.text.replace("\n", "")
        print(f"[{Fore.GREEN}+{Fore.RESET}] Grabbed & Saved {cou} Socks4 Proxy")
        with open("SOCKS4.txt", "a") as Proxyy:
            Proxyy.write(ress)
            Proxyy.close()
            input(f"[{Fore.CYAN}${Fore.RESET}] Press Any Key To Exit...\n")

    elif noe == 3:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
        res = a.get(url)
        cou = res.text.count(":")
        ress = res.text.replace("\n", "")
        print(f"[{Fore.GREEN}+{Fore.RESET}] Grabbed & Saved {cou} Socks5 Proxy")
        with open("SOCKS5.txt", "a") as Proxyy:
            Proxyy.write(ress)
            input(f"[{Fore.CYAN}${Fore.RESET}] Press Any Key To Exit...\n")

    elif noe == 4:
        if path.exists("proxy.txt"):
            threadn = int(input(f"[{Fore.CYAN}?{Fore.RESET}] Enter Your Threads: "))
            threadlist = []
            for t in range(threadn + 1):
                i = threading.Thread(target=chkp)
                i.start()
                threadlist.append(i)
            for i in threadlist:
                i.join()
        else:
            print(f"[{Fore.RED}!{Fore.RESET}] Make a [proxy.txt] File & Try again")
            time.sleep(3)
            os.system("cls")
            mode()

    elif noe == 99:
        print(f"[{Fore.RED}-{Fore.RESET}] Add @l7up on IG, & Cya Loser")
        time.sleep(2)
        exit()

    else:
        print(f"[{Fore.GREEN}-{Fore.RESET}] Error, No Mode Found")
        time.sleep(3)
        os.system("cls")
        mode()


def chkp():
    while 1:
        good = 0
        bad = 0
        checked = 0
        proxx = open("proxy.txt", "r")
        for prox in proxx:
            ip = prox.split(":")[0]
            port = prox.split(":")[1]
            url = "https://onlinechecker.proxyscrape.com/index.php"
            head = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "origin": "https://proxyscrape.com",
                "referer": "https://proxyscrape.com/",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
            }
            data = {
                "ip_addr": ip,
                "port": port
            }
            chk = a.post(url, data=data, headers=head)
            if chk.text.find('working" : true') >= 0:
                good += 1
                checked += 1
                print(f"[{Fore.GREEN}+{Fore.RESET}] {ip}:{port}")

                if chk.text.find('type" : "HTTP/S') >= 0:
                    with open(f"[{Fore.GREEN}+{Fore.RESET}] Checked-HTTP.txt", "a") as resu:
                        resu.write(f"[{Fore.GREEN}+{Fore.RESET}] {ip}:{port}")
                        resu.close()
                elif chk.text.find('type" : "SOCKS4') >= 0:
                    with open(f"[{Fore.GREEN}+{Fore.RESET}] Checked-SOCKS4.txt", "a") as resu:
                        resu.write(f"[{Fore.GREEN}+{Fore.RESET}] {ip}:{port}")
                        resu.close()
                elif chk.text.find('type" : "SOCKS5') >= 0:
                    with open(f"[{Fore.GREEN}+{Fore.RESET}] Checked-SOCKS5.txt", "a") as resu:
                        resu.write(f"[{Fore.GREEN}+{Fore.RESET}] {ip}:{port}")
                        resu.close()
                else:
                    with open(f"[{Fore.GREEN}+{Fore.RESET}] Checked-Unknown.txt", "a") as resu:
                        resu.write(f"[{Fore.GREEN}+{Fore.RESET}] {ip}:{port}")
                        resu.close()
            else:
                bad += 1
                checked += 1
                print(f"[{Fore.RED}-{Fore.RESET}] {ip}:{port}")


mode()
