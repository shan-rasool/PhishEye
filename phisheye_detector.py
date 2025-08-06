
# ========================================
# 🔐 PhishEye Detector
# ========================================
# A Python-based CLI tool to detect phishing URLs using pattern analysis.
#
# 👨‍💻 Developed by: SR Cyber Solutions
# ========================================

import re
import requests
import os
import time
from urllib.parse import urlparse
from termcolor import colored
from pyfiglet import figlet_format

# -----------------------------
# Stylish Header
# -----------------------------
def print_banner():
    os.system('clear')  # Clears the terminal screen (Linux)
    print(colored(figlet_format("PhishEye", font="slant"), "cyan"))
    print(colored("🔍 A phishing URL detection tool", "yellow"))
    print(colored("Developed by SR Cyber SolutionsT\n", "green"))
    print(colored("============================================\n", "magenta"))

# -----------------------------
# Keyword-based Pattern Detection
# -----------------------------
PHISHING_KEYWORDS = [
    'login', 'verify', 'update', 'secure', 'account', 'banking', 'confirm', 'ebayisapi',
    'webscr', 'signin', 'paypal', 'security', 'alert', 'appleid', 'support', 'billing'
]

def is_phishing_by_keywords(url):
    for keyword in PHISHING_KEYWORDS:
        if keyword.lower() in url.lower():
            return True, keyword
    return False, None

# -----------------------------
# URL Analysis Function
# -----------------------------
def check_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    suspicious, keyword = is_phishing_by_keywords(url)

    print(colored("[+] Analyzing URL:", 'cyan'), url)
    print("[-] Domain:", domain)

    if suspicious:
        print(colored(f"[!] Suspicious keyword found: '{keyword}'", 'red'))
        print(colored("[!] This URL is likely a phishing attempt!", 'red', attrs=['bold']))
    else:
        print(colored("[+] No obvious phishing patterns found.", 'green'))

# -----------------------------
# Main Entry Point
# -----------------------------
def main():
    print_banner()
    url = input(colored("Enter a URL to scan: ", "cyan")).strip()

    if not re.match(r'^https?://', url):
        print(colored("[!] Please enter a valid URL starting with http:// or https://", 'yellow'))
        return

    check_url(url)

if __name__ == '__main__':
    try:
        from pyfiglet import figlet_format
    except ImportError:
        print(colored("[!] Missing dependency: pyfiglet", 'red'))
        print("Install it using: pip install pyfiglet")
        exit()

    main()
