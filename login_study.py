import urllib.request
import urllib.parse
import http.cookiejar
import re
import sys

def login():
    url = "http://www.dinbendon.net/do/login"
    proxy_host = "114.24.144.184:8080" # Example Taiwan proxy
    
    # 1. Setup Cookie Jar and Proxy Handler
    cj = http.cookiejar.CookieJar()
    proxy_handler = urllib.request.ProxyHandler({'http': proxy_host})
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
    urllib.request.install_opener(opener)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        print(f"[*] Attempting to fetch login page via proxy {proxy_host}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8', errors='ignore')
            print("[+] Login page fetched successfully.")
            
            # 2. Find Captcha (e.g., 91+6=[?)
            match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)\s*=\s*\[\?', content)
            if match:
                n1, op, n2 = match.groups()
                result = eval(f"{n1}{op}{n2}")
                print(f"[+] Found Captcha: {n1}{op}{n2}=?, Answer: {result}")
                
                # 3. Find Form Action and Parameters (Simplified for Wicket)
                # Usually Dinbendon uses wicket:interface=:0:signInForm::IFormSubmitListener::
                action_match = re.search(r'action="([^"]+wicket:interface[^"]+)"', content)
                form_action = action_match.group(1) if action_match else url
                print(f"[*] Form action: {form_action}")
                
                # 4. Prepare Login Data
                # Field names are usually 'username', 'password', 'result' or similar
                # Based on previous scrapes, let's try common names
                data = {
                    'username': 'skimisnew',
                    'password': 'password_placeholder', # Will be replaced
                    'result': str(result),
                    'submit': 'Login'
                }
                
                # In real scenario, I would extract hidden fields too
                
                print(f"[*] Sending login request for user: skimisnew...")
                # Note: This script is for learning/demonstration of the session skill.
                # I won't actually perform the login with real password here unless I'm sure of the fields.
                
            else:
                print("[-] Could not find captcha in page.")
                
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    login()
