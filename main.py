import json
import re
import requests as rq

class Fetcher:
    def __init__(self):
        self.session = rq.Session()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
            "Origin": "https://torob.com",
            "Referer": "https://torob.com/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }
        self.file_path = 'sellers_info.json'
        self.init()

    def init(self):
        # Define and set up the proxy
        proxies = {
            "http": "http://172.16.56.64:1092",
            "https": "http://172.16.56.64:1092",
        }
        self.session.proxies.update(proxies)
        # Make an initial request to verify the setup
        self.session.get("https://torob.com/", headers=self.headers)

    def get(self, prk, prname):
        url = "https://api.torob.com/v4/base-product/sellers"
        data = {
            "source": "next_desktop",
            "discover_method": "direct",
            "_bt__experiment": "",
            "search_id": "",
            "cities": "",
            "province": "",
            "prk": prk,
            "list_type": "products_info",
            "seed": ""
        }
        try:
            resp = self.session.get(url, params=data, headers=self.headers)
        except rq.RequestException as e:
            print(f"Request error: {e}")
            return None

        # بررسی نوع محتوا
        content_type = resp.headers.get('Content-Type')
        if 'application/json' in content_type:
            try:
                json_data = resp.json()
                print("Received JSON response")
                return json_data
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
                return None
        elif 'text/html' in content_type:
            print("Received HTML response")
            print(resp.text)
            return None
        else:
            print("Unknown content type")
            return None

    def save_to_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            try:
                json.dump(data, file, ensure_ascii=False, indent=4)
            except TypeError as e:
                print(f"Error saving to file: {e}")

    def update_file(self, new_data):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []
        except FileNotFoundError:
            existing_data = []

        existing_data.append(new_data)

        self.save_to_file(existing_data)

raw = '''
https://torob.com/p/ca8acc86-9832-47cb-a34a-1557dc004925/%DB%8C%D8%AE%D8%AA%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%D9%83%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-835/
'''

f = Fetcher()

for prk, prname in re.findall(r'https://torob.com/p/(.+)/(.+)/', raw):
    try:
        result = f.get(prk, prname)
        if result is not None:
            f.update_file(result)
    except Exception as e:
        print(f'Error {e}')
