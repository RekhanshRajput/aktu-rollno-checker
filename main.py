import requests
from bs4 import BeautifulSoup
import time
import sys
from datetime import datetime

BASE_URL = "https://erp.aktu.ac.in/WebPages/OneView/OneView.aspx"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://erp.aktu.ac.in",
    "Referer": BASE_URL,
}

CORRECT_LENGTH = 18948
TIMEOUT = 15
DELAY = 0.25

def print_banner():
    print("\033[96m" + "="*60)
    print("          AKTU OneView Roll Number Validator")
    print("\033[91m          Created by REKHANSH RAJPUT\033[0m")  
    print("          " + datetime.now().strftime("%Y-%m-%d"))
    print("="*60 + "\033[0m\n")

def get_viewstate(session):
    try:
        r = session.get(BASE_URL, timeout=TIMEOUT)
        soup = BeautifulSoup(r.text, "html.parser")
        vs = soup.find("input", {"name": "__VIEWSTATE"})
        return vs["value"] if vs else None
    except:
        return None

def check_roll(session, roll, viewstate):
    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": "309C3D50",
        "txtRollNo": roll,
        "btnProceed": "आगे बढ़े",
        "hidForModel": ""
    }
    try:
        r = session.post(BASE_URL, data=payload, timeout=TIMEOUT)
        length = len(r.content)
        return "VALID" if length == CORRECT_LENGTH else "INVALID"
    except Exception as e:
        return f"ERROR"

def main():
    print_banner()
    s = requests.Session()
    s.headers.update(HEADERS)

    while True:
        print("  1. Single Roll Check")
        print("  2. Range Check")
        print("  3. Exit")
        print("-"*50)
        ch = input("Choice: ").strip()

        if ch == "3":
            print("\nExiting...\n")
            break

        if ch not in ("1", "2"):
            print("Invalid choice\n")
            continue

        viewstate = get_viewstate(s)
        if not viewstate:
            print("Failed to get VIEWSTATE. Try later.\n")
            continue

        if ch == "1":
            roll = input("Roll No: ").strip()
            if not roll: continue
            status = check_roll(s, roll, viewstate)
            print(f"\n{roll} → {status}\n")
            if status == "VALID":
                with open("valid.txt", "a") as f:
                    f.write(f"{roll} | {datetime.now():%Y-%m-%d %H:%M}\n")

        elif ch == "2":
            try:
                start = int(input("From: "))
                end = int(input("To: "))
            except:
                print("Enter numbers only\n")
                continue

            if start > end:
                print("Start should be <= End\n")
                continue

            print(f"\nChecking {start} → {end} ...\n")
            count = 0
            for r in range(start, end + 1):
                roll = str(r)
                status = check_roll(s, roll, viewstate)
                mark = "✓" if status == "VALID" else "✗"
                print(f"{roll:>10} {mark} {status}")
                if status == "VALID":
                    count += 1
                    with open("valid.txt", "a") as f:
                        f.write(f"{roll} | {datetime.now():%Y-%m-%d %H:%M}\n")
                time.sleep(DELAY)
            print(f"\nDone. Valid: {count}/{end-start+1}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.\n")
    except Exception as e:
        print(f"Error: {e}\n")
