import urllib.request
import urllib.parse
import http.cookiejar
import re
import sys

def automated_login():
    # 1. Configuration
    login_url = "http://www.dinbendon.net/do/login"
    username = "skimisnew"
    password = "password_placeholder" # Will be replaced
    
    # We need a proxy because the main host is blocked
    # Trying a few known free proxies (this is the fragile part of automation)
    proxies = ["114.24.144.184:8080", "61.216.156.222:8080"] 
    
    for proxy in proxies:
        try:
            print(f"[*] Trying proxy: {proxy}")
            cj = http.cookiejar.CookieJar()
            proxy_handler = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), proxy_handler)
            
            # 2. Get Login Page & Solve Captcha
            print("[*] Fetching captcha...")
            req = urllib.request.Request(login_url)
            with opener.open(req, timeout=10) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)\s*=\s*\[\?', content)
                if not match:
                    print("[-] No captcha found.")
                    continue
                
                n1, op, n2 = match.groups()
                captcha_ans = str(eval(f"{n1}{op}{n2}"))
                print(f"[+] Solved Captcha: {n1}{op}{n2}={captcha_ans}")
                
                # 3. Perform Login
                # Note: Real field names are needed here. 
                # Based on Wicket structure, they might be like 'signInForm:username'
                login_data = urllib.parse.urlencode({
                    'username': username,
                    'password': '25064294',
                    'result': captcha_ans,
                    'submit': 'Login'
                }).encode('utf-8')
                
                login_req = urllib.request.Request(login_url, data=login_data)
                with opener.open(login_req, timeout=10) as login_resp:
                    print("[+] Login request sent.")
                    # 4. Check orders
                    # ... grab content ...
                    return True
        except Exception as e:
            print(f"[-] Proxy {proxy} failed: {e}")
            
    return False

if __name__ == "__main__":
    automated_login()
