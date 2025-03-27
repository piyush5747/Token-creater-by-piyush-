import requests
import json

def get_fb_token(cookies):
    headers = {
        "Cookie": cookies,
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"
    }
    url = "https://business.facebook.com/business_locations"
    
    response = requests.get(url, headers=headers)
    
    if "EAAG" in response.text:
        token = response.text.split('EAAG')[1].split('"')[0]
        return f"EAAG{token}"
    else:
        return "Token Fetch Failed! Invalid Cookies."

if __name__ == "__main__":
    print("⚡ CREAT BY PIYUSH  Facebook Token Extractor ⚡")
    cookies = input("🔑 Enter Facebook JSON Cookies: ")
    
    token = get_fb_token(cookies)
    
    if "EAAG" in token:
        print(f"\n✅ Your Facebook Token: {token}\n")
    else:
        print("\n❌ Failed to Fetch Token. Check your cookies!\n")