import os
import sys
import time
import requests
import re
import random
import string
import base64
from urllib.parse import urlparse

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"; MAGENTA="\033[95m"

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
    {RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
    {RED}⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
    {RED}⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
    {RED}⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
    {RED}⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
    {RED}⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
    {RED}⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛{RESET}
    {MAGENTA}{BOLD}         [ W E B   H A C K E R   P R O ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} NAME: {WHITE}ROMAN HACKER {GREEN}| BIO: {WHITE}Ethical Hacker & Dev{RESET}
    {GREEN} WA:   {WHITE}923037224620 {GREEN}| TG:  {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def hacker_loading(msg, duration=1.5):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{YELLOW}{BOLD}  [{frames[i % 4]}] {msg}...{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r{GREEN}{BOLD}  [✓] {msg} DONE!{RESET}          \n")

def fake_scraping_animation():
    print(f"\n{RED}{BOLD}  [!] INITIATING DEEP WEB SCAN...{RESET}\n")
    for i in range(1, 16):
        fake_ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
        hex_code = ''.join(random.choices(string.hexdigits, k=16))
        print(f"\033[91m  [FETCH] 0x{hex_code} | Routing via {fake_ip} | Buffer {i*10}%... OK\033[0m")
        time.sleep(0.1)
    print("")

def extract_source():
    clear()
    show_banner()
    
    url = input(f"{GREEN}{BOLD}  ► Enter Target URL (e.g., example.com): {RESET}").strip()
    if not url:
        return
        
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
        
    print(f"\n{YELLOW}{BOLD}  [!] TARGET ACQUIRED: {WHITE}{url}{RESET}")
    time.sleep(0.5)
    
    # Advanced Hacker Animations
    hacker_loading("Resolving Target IP Address", 1.2)
    hacker_loading("Bypassing WAF & Cloudflare", 1.5)
    fake_scraping_animation()
    hacker_loading("Extracting Raw DOM Tree", 1.5)
    hacker_loading("Decrypting Source Payload", 1.2)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            source_code = response.text
            
            # Progress Bar
            print(f"\n{CYAN}{BOLD}  [~] Finalizing Extraction...{RESET}")
            for i in range(101):
                sys.stdout.write(f"\r  \033[96m[{'█' * int(i/5)}{'░' * (20 - int(i/5))}] {i}%\033[0m")
                sys.stdout.flush()
                time.sleep(0.02)
            print("\n")
            
            # Copy to clipboard
            print(f"{YELLOW}  [~] Injecting Code to Clipboard...{RESET}")
            b64_code = base64.b64encode(source_code.encode('utf-8')).decode('utf-8')
            os.system(f"echo '{b64_code}' | base64 -d | termux-clipboard-set")
            time.sleep(1)
            
            # VIP Success Box (Dangerous Attitude)
            clear()
            show_banner()
            print(f"\n{GREEN}{BOLD}")
            print("  ╔══════════════════════════════════════════════════╗")
            print("  ║            💀 SOURCE CODE HIJACKED 💀            ║")
            print("  ╠══════════════════════════════════════════════════╣")
            print(f"  ║  {YELLOW}TARGET : {WHITE}{url[:38]:<38} {GREEN}║")
            print(f"  ║  {YELLOW}SIZE   : {WHITE}{len(source_code)} characters{' '*(26-len(str(len(source_code))))} {GREEN}║")
            print(f"  ║  {YELLOW}STATUS : {RED}PAYLOAD IN CLIPBOARD{' '*21} {GREEN}║")
            print("  ╠══════════════════════════════════════════════════╣")
            print(f"  ║  {RED}{BOLD}► SECURITY BREACHED. DATA COMPROMISED.{RESET}       {GREEN}║")
            print(f"  ║  {RED}{BOLD}► PAYLOAD STORED IN CLIPBOARD. {RESET}              {GREEN}║")
            print(f"  ║  {CYAN}{BOLD}► LEAVE NO EVIDENCE. ROMAN OWNS THE DOM.{RESET}      {GREEN}║")
            print("  ╚══════════════════════════════════════════════════╝")
            print(f"{RESET}")
            
        else:
            print(f"\n{RED}  [!] Failed to extract. HTTP Status: {response.status_code}{RESET}")
            
    except requests.exceptions.Timeout:
        print(f"\n{RED}  [!] Error: Connection Timed Out. Target is taking too long.{RESET}")
    except requests.exceptions.ConnectionError:
        print(f"\n{RED}  [!] Error: Invalid URL or No Internet Connection.{RESET}")
    except Exception as e:
        print(f"\n{RED}  [!] Error: {e}{RESET}")
        
    input(f"\n{CYAN}  Press ENTER to return...{RESET}")

def main():
    while True:
        try:
            clear()
            show_banner()
            print(f"""{BLUE}{BOLD}
    ┌──────────────────────────────────────────────────┐
    │             WEB SOURCE EXTRACTOR                 │
    ├──────────────────────────────────────────────────┤
    │  {WHITE}[1]{GREEN} Extract & Hack Source Code                │
    │  {WHITE}[2]{BLUE} Exit System                               │
    └──────────────────────────────────────────────────┘
{RESET}""")
            
            choice = input(f"{GREEN}{BOLD}  └──► Select Option [1-2]: {RESET}").strip()
            
            if choice == "1":
                extract_source()
            elif choice == "2":
                print(f"\n{RED} Exiting System...{RESET}")
                time.sleep(1)
                break
            else:
                time.sleep(0.5)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
EOF
