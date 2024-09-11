import requests as rq
import re
import json

class Fetcher:
    def __init__(self):
        self.session = None
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

    def init(self):
        self.session = rq.Session()
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
        resp = self.session.get(url, params=data, headers=self.headers)
        
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
https://torob.com/p/ca8acc86-9832-47cb-a34a-1557dc004925/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-835/
https://torob.com/p/307d8a07-2b6f-4bee-8e9a-8ecce182f1fe/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D8%AF%DB%8C%D9%BE%D9%88%DB%8C%D9%86%D8%AA-%D9%85%D8%AF%D9%84-max/
https://torob.com/p/74476fbc-d8fc-4627-82a5-3f12727e6b62/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%AC%D9%86%D8%B1%D8%A7%D9%84-%D9%BE%DB%8C%D9%86-27-%D9%81%D9%88%D8%AA-%D9%85%D8%AF%D9%84-rf-m22/
https://torob.com/p/9c91dd12-bc37-4282-8822-b34884598044/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%88-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%B7%D8%B1%D8%AD-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A7%DB%8C%DA%A9%D8%B3-%D9%88%DB%8C%DA%98%D9%86-%D9%85%D8%AF%D9%84-ts552-awd-%D8%B1%D9%86%DA%AF-%D8%B3%D9%81%DB%8C%D8%AF/
https://torob.com/p/1aa282d3-8e42-4d78-8e16-3fef5413429c/%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%AF%D9%88%D9%88-ds-3325mw-%D8%B3%D9%81%DB%8C%D8%AF-32-%D9%81%D9%88%D8%AA-%D8%B3%D8%B1%DB%8C-%D9%BE%D8%B1%D8%A7%DB%8C%D9%85-2-%D8%AF%D8%B1%D8%A8/
https://torob.com/p/31a43f04-d2ef-4a81-b4b9-363fc9538f18/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%DA%A9%D9%84%D9%88%D8%B1-%D9%85%D8%AF%D9%84-%D8%B1%D9%88%D8%B3%D9%88-%D9%BE%D9%84%D8%A7%D8%B3-%DB%8C%D8%AE%D8%B3%D8%A7%D8%B2-%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/
https://torob.com/p/91988a6e-286b-4c70-983c-e02d25117d14/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-919-150/
https://torob.com/p/f3bc4073-21ce-4de2-a3f6-512d06949987/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A8%D8%A7%D9%84%D8%A7-%D9%BE%D8%A7%DB%8C%DB%8C%D9%86-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-20-%D9%81%D9%88%D8%AA-_-bfn20d-m-tp-em46/
https://torob.com/p/d660ceff-8220-427c-90ae-10c6fe3a6901/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-tf11t/
https://torob.com/p/99e692a0-d1d6-4c60-960d-c161c4537289/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D9%87%DB%8C%D9%85%D8%A7%D9%84%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-%D9%BE%D8%A7%D9%86%D8%A7%D8%B1%D9%88%D9%85%D8%A7-%D9%BE%D9%84%D8%A7%D8%B3-_-%2Bnr440p%2B-nf280p/
https://torob.com/p/7dd9b180-9698-4c02-9cd8-b86e92c09a01/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-variety-sum-%D8%A7%D8%B1%D8%B3%D8%A7%D9%84-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86/
https://torob.com/p/ba2d7e53-5621-40b2-ad56-a9f6bb0b78a1/%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D9%84%DB%8C%D8%B3-%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7%DB%8C%DB%8C-%D9%88-%D8%B1%D8%A7%D9%86%D9%86%D8%AF%DA%AF%DB%8C-%DA%A9%D9%88%D8%AF%DA%A9/
https://torob.com/p/ee226513-d99f-434c-adc6-5445ba59914e/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%D8%A7-%DA%A9%D9%84%D8%A7%D8%B3-%D9%BE%D8%A7%D9%BE%DB%8C%D9%88%D9%86-%D8%AF%D8%A7%D8%B1/
https://torob.com/p/e4aa4f94-739a-4451-8f4c-ffab22a9c56f/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%88%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/3ec2166d-594d-4ae3-ba46-588a4d492be8/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%DA%86%DA%AF%D8%A7%D9%86%D9%87-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%88%D8%A7%D8%B1%D8%AF%D8%A7%D8%AA%DB%8C-%D8%A7%D9%88%D8%B1%D8%AC%DB%8C%D9%86%D8%A7%D9%84-1/
https://torob.com/p/8e182490-c8b2-4dda-b3fa-65baa171d80f/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%88%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/3deb2a4d-1fff-4ce9-94f7-e782f22fe8d2/%DA%A9%D8%AA-%D8%AE%D8%B2-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1-%D8%B4%DB%8C%DA%A9-%D9%88-%D8%B9%D8%A7%D9%84%DB%8C-%D8%AC%D9%86%D8%B3-%DA%A9%D8%A7%D8%B1-%D8%AE%D8%B2-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1-%D8%A8%D8%A7-%DA%A9%DB%8C%D9%81%DB%8C%D8%AA-%D9%87%D8%B3%D8%AA-%D8%A7%D8%B3%D8%AA%D8%B1%DA%A9%D8%B4%DB%8C-%D8%B4%D8%AF%D9%87-%D9%88-%D8%AC%D9%84%D9%88%DB%8C-%DA%A9%D8%A7%D8%B1-%D8%A8%D9%87-%D8%B3%D9%84%DB%8C%D9%82-%DB%8C-%D9%85%D8%B4%D8%AA%D8%B1%DB%8C-%D8%A7%D9%85%D8%A7%D8%AF%D9%87-%D9%85%DB%8C%D8%B4%D9%87/
https://torob.com/p/f3086e9c-5c48-4c3b-bb35-0c8971a22919/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/5676dfcd-0fe4-4f0a-9015-22b0fe56ecb0/%DA%A9%D8%AA-%D8%B7%D8%B1%D8%AD-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87/
https://torob.com/p/eb98721b-60c4-493b-b088-ccbc1b24010c/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%A7%D9%86%D8%AF%D8%A7/
https://torob.com/p/0c11ad88-5474-4588-ab08-8cd6efe3f43d/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%84%DB%8C-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%85%DB%8C%D9%86%DB%8C-%D9%85%D9%88%D8%B3-%D8%B6%D8%AE%DB%8C%D9%85-%DA%AF%D8%B1%D9%85-%D8%A8%D8%A7%D9%84%D8%A7-%D8%AA%D8%B1%DA%A9-4%D8%AA%D8%A710%D8%B3%D8%A7%D9%84-%D8%A8%D8%B1%D9%86%D8%AF-%D8%B2%D8%A7%D8%B1%D8%A7-9%D8%AA%D8%A710%D8%B3%D8%A7%D9%84/
https://torob.com/p/23c8e6ce-2178-4561-8086-0d1c93441819/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%DA%86%DA%AF%D8%A7%D9%86%D9%87-059-%D8%B3%D8%A7%DB%8C%D8%B2-110/
https://torob.com/p/3c01fa22-7c8d-4752-9861-360d287b7856/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D8%A7%D8%B3%D9%86%D9%88%D9%BE%DB%8C/
https://torob.com/p/15177424-fe9e-4cb3-a723-e6c6d262dce6/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-mtb/
https://torob.com/p/ca8acc86-9832-47cb-a34a-1557dc004925/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-835/
https://torob.com/p/307d8a07-2b6f-4bee-8e9a-8ecce182f1fe/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D8%AF%DB%8C%D9%BE%D9%88%DB%8C%D9%86%D8%AA-%D9%85%D8%AF%D9%84-max/
https://torob.com/p/74476fbc-d8fc-4627-82a5-3f12727e6b62/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%AC%D9%86%D8%B1%D8%A7%D9%84-%D9%BE%DB%8C%D9%86-27-%D9%81%D9%88%D8%AA-%D9%85%D8%AF%D9%84-rf-m22/
https://torob.com/p/9c91dd12-bc37-4282-8822-b34884598044/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%88-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%B7%D8%B1%D8%AD-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A7%DB%8C%DA%A9%D8%B3-%D9%88%DB%8C%DA%98%D9%86-%D9%85%D8%AF%D9%84-ts552-awd-%D8%B1%D9%86%DA%AF-%D8%B3%D9%81%DB%8C%D8%AF/
https://torob.com/p/1aa282d3-8e42-4d78-8e16-3fef5413429c/%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%AF%D9%88%D9%88-ds-3325mw-%D8%B3%D9%81%DB%8C%D8%AF-32-%D9%81%D9%88%D8%AA-%D8%B3%D8%B1%DB%8C-%D9%BE%D8%B1%D8%A7%DB%8C%D9%85-2-%D8%AF%D8%B1%D8%A8/
https://torob.com/p/31a43f04-d2ef-4a81-b4b9-363fc9538f18/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%DA%A9%D9%84%D9%88%D8%B1-%D9%85%D8%AF%D9%84-%D8%B1%D9%88%D8%B3%D9%88-%D9%BE%D9%84%D8%A7%D8%B3-%DB%8C%D8%AE%D8%B3%D8%A7%D8%B2-%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/
https://torob.com/p/91988a6e-286b-4c70-983c-e02d25117d14/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-919-150/
https://torob.com/p/f3bc4073-21ce-4de2-a3f6-512d06949987/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A8%D8%A7%D9%84%D8%A7-%D9%BE%D8%A7%DB%8C%DB%8C%D9%86-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-20-%D9%81%D9%88%D8%AA-_-bfn20d-m-tp-em46/
https://torob.com/p/d660ceff-8220-427c-90ae-10c6fe3a6901/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-tf11t/
https://torob.com/p/99e692a0-d1d6-4c60-960d-c161c4537289/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D9%87%DB%8C%D9%85%D8%A7%D9%84%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-%D9%BE%D8%A7%D9%86%D8%A7%D8%B1%D9%88%D9%85%D8%A7-%D9%BE%D9%84%D8%A7%D8%B3-_-%2Bnr440p%2B-nf280p/
https://torob.com/p/7dd9b180-9698-4c02-9cd8-b86e92c09a01/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-variety-sum-%D8%A7%D8%B1%D8%B3%D8%A7%D9%84-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86/
https://torob.com/p/ba2d7e53-5621-40b2-ad56-a9f6bb0b78a1/%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D9%84%DB%8C%D8%B3-%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7%DB%8C%DB%8C-%D9%88-%D8%B1%D8%A7%D9%86%D9%86%D8%AF%DA%AF%DB%8C-%DA%A9%D9%88%D8%AF%DA%A9/
https://torob.com/p/ee226513-d99f-434c-adc6-5445ba59914e/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%D8%A7-%DA%A9%D9%84%D8%A7%D8%B3-%D9%BE%D8%A7%D9%BE%DB%8C%D9%88%D9%86-%D8%AF%D8%A7%D8%B1/
https://torob.com/p/e4aa4f94-739a-4451-8f4c-ffab22a9c56f/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%88%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/3ec2166d-594d-4ae3-ba46-588a4d492be8/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%DA%86%DA%AF%D8%A7%D9%86%D9%87-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%88%D8%A7%D8%B1%D8%AF%D8%A7%D8%AA%DB%8C-%D8%A7%D9%88%D8%B1%D8%AC%DB%8C%D9%86%D8%A7%D9%84-1/
https://torob.com/p/8e182490-c8b2-4dda-b3fa-65baa171d80f/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%88%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/3deb2a4d-1fff-4ce9-94f7-e782f22fe8d2/%DA%A9%D8%AA-%D8%AE%D8%B2-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1-%D8%B4%DB%8C%DA%A9-%D9%88-%D8%B9%D8%A7%D9%84%DB%8C-%D8%AC%D9%86%D8%B3-%DA%A9%D8%A7%D8%B1-%D8%AE%D8%B2-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1-%D8%A8%D8%A7-%DA%A9%DB%8C%D9%81%DB%8C%D8%AA-%D9%87%D8%B3%D8%AA-%D8%A7%D8%B3%D8%AA%D8%B1%DA%A9%D8%B4%DB%8C-%D8%B4%D8%AF%D9%87-%D9%88-%D8%AC%D9%84%D9%88%DB%8C-%DA%A9%D8%A7%D8%B1-%D8%A8%D9%87-%D8%B3%D9%84%DB%8C%D9%82-%DB%8C-%D9%85%D8%B4%D8%AA%D8%B1%DB%8C-%D8%A7%D9%85%D8%A7%D8%AF%D9%87-%D9%85%DB%8C%D8%B4%D9%87/
https://torob.com/p/f3086e9c-5c48-4c3b-bb35-0c8971a22919/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/5676dfcd-0fe4-4f0a-9015-22b0fe56ecb0/%DA%A9%D8%AA-%D8%B7%D8%B1%D8%AD-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87/
https://torob.com/p/eb98721b-60c4-493b-b088-ccbc1b24010c/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%A7%D9%86%D8%AF%D8%A7/
https://torob.com/p/0c11ad88-5474-4588-ab08-8cd6efe3f43d/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%84%DB%8C-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%85%DB%8C%D9%86%DB%8C-%D9%85%D9%88%D8%B3-%D8%B6%D8%AE%DB%8C%D9%85-%DA%AF%D8%B1%D9%85-%D8%A8%D8%A7%D9%84%D8%A7-%D8%AA%D8%B1%DA%A9-4%D8%AA%D8%A710%D8%B3%D8%A7%D9%84-%D8%A8%D8%B1%D9%86%D8%AF-%D8%B2%D8%A7%D8%B1%D8%A7-9%D8%AA%D8%A710%D8%B3%D8%A7%D9%84/
https://torob.com/p/23c8e6ce-2178-4561-8086-0d1c93441819/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%DA%86%DA%AF%D8%A7%D9%86%D9%87-059-%D8%B3%D8%A7%DB%8C%D8%B2-110/
https://torob.com/p/3c01fa22-7c8d-4752-9861-360d287b7856/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D8%A7%D8%B3%D9%86%D9%88%D9%BE%DB%8C/
https://torob.com/p/15177424-fe9e-4cb3-a723-e6c6d262dce6/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-mtb/
https://torob.com/p/ca8acc86-9832-47cb-a34a-1557dc004925/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-835/
https://torob.com/p/307d8a07-2b6f-4bee-8e9a-8ecce182f1fe/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D8%AF%DB%8C%D9%BE%D9%88%DB%8C%D9%86%D8%AA-%D9%85%D8%AF%D9%84-max/
https://torob.com/p/74476fbc-d8fc-4627-82a5-3f12727e6b62/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%AC%D9%86%D8%B1%D8%A7%D9%84-%D9%BE%DB%8C%D9%86-27-%D9%81%D9%88%D8%AA-%D9%85%D8%AF%D9%84-rf-m22/
https://torob.com/p/9c91dd12-bc37-4282-8822-b34884598044/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%88-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%B7%D8%B1%D8%AD-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A7%DB%8C%DA%A9%D8%B3-%D9%88%DB%8C%DA%98%D9%86-%D9%85%D8%AF%D9%84-ts552-awd-%D8%B1%D9%86%DA%AF-%D8%B3%D9%81%DB%8C%D8%AF/
https://torob.com/p/1aa282d3-8e42-4d78-8e16-3fef5413429c/%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%AF%D9%88%D9%88-ds-3325mw-%D8%B3%D9%81%DB%8C%D8%AF-32-%D9%81%D9%88%D8%AA-%D8%B3%D8%B1%DB%8C-%D9%BE%D8%B1%D8%A7%DB%8C%D9%85-2-%D8%AF%D8%B1%D8%A8/
https://torob.com/p/31a43f04-d2ef-4a81-b4b9-363fc9538f18/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%DA%A9%D9%84%D9%88%D8%B1-%D9%85%D8%AF%D9%84-%D8%B1%D9%88%D8%B3%D9%88-%D9%BE%D9%84%D8%A7%D8%B3-%DB%8C%D8%AE%D8%B3%D8%A7%D8%B2-%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/
https://torob.com/p/91988a6e-286b-4c70-983c-e02d25117d14/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-919-150/
https://torob.com/p/f3bc4073-21ce-4de2-a3f6-512d06949987/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A8%D8%A7%D9%84%D8%A7-%D9%BE%D8%A7%DB%8C%DB%8C%D9%86-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-20-%D9%81%D9%88%D8%AA-_-bfn20d-m-tp-em46/
https://torob.com/p/d660ceff-8220-427c-90ae-10c6fe3a6901/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-tf11t/
https://torob.com/p/99e692a0-d1d6-4c60-960d-c161c4537289/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D9%87%DB%8C%D9%85%D8%A7%D9%84%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-%D9%BE%D8%A7%D9%86%D8%A7%D8%B1%D9%88%D9%85%D8%A7-%D9%BE%D9%84%D8%A7%D8%B3-_-%2Bnr440p%2B-nf280p/
https://torob.com/p/7dd9b180-9698-4c02-9cd8-b86e92c09a01/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-variety-sum-%D8%A7%D8%B1%D8%B3%D8%A7%D9%84-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86/
https://torob.com/p/ba2d7e53-5621-40b2-ad56-a9f6bb0b78a1/%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D9%84%DB%8C%D8%B3-%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7%DB%8C%DB%8C-%D9%88-%D8%B1%D8%A7%D9%86%D9%86%D8%AF%DA%AF%DB%8C-%DA%A9%D9%88%D8%AF%DA%A9/
https://torob.com/p/ee226513-d99f-434c-adc6-5445ba59914e/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%D8%A7-%DA%A9%D9%84%D8%A7%D8%B3-%D9%BE%D8%A7%D9%BE%DB%8C%D9%88%D9%86-%D8%AF%D8%A7%D8%B1/
https://torob.com/p/e4aa4f94-739a-4451-8f4c-ffab22a9c56f/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%88%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/3ec2166d-594d-4ae3-ba46-588a4d492be8/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%DA%86%DA%AF%D8%A7%D9%86%D9%87-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%88%D8%A7%D8%B1%D8%AF%D8%A7%D8%AA%DB%8C-%D8%A7%D9%88%D8%B1%D8%AC%DB%8C%D9%86%D8%A7%D9%84-1/
https://torob.com/p/8e182490-c8b2-4dda-b3fa-65baa171d80f/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%88%D8%AC%D9%84%DB%8C%D9%82%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/3deb2a4d-1fff-4ce9-94f7-e782f22fe8d2/%DA%A9%D8%AA-%D8%AE%D8%B2-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1-%D8%B4%DB%8C%DA%A9-%D9%88-%D8%B9%D8%A7%D9%84%DB%8C-%D8%AC%D9%86%D8%B3-%DA%A9%D8%A7%D8%B1-%D8%AE%D8%B2-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C-%D8%A8%D8%B3%DB%8C%D8%A7%D8%B1-%D8%A8%D8%A7-%DA%A9%DB%8C%D9%81%DB%8C%D8%AA-%D9%87%D8%B3%D8%AA-%D8%A7%D8%B3%D8%AA%D8%B1%DA%A9%D8%B4%DB%8C-%D8%B4%D8%AF%D9%87-%D9%88-%D8%AC%D9%84%D9%88%DB%8C-%DA%A9%D8%A7%D8%B1-%D8%A8%D9%87-%D8%B3%D9%84%DB%8C%D9%82-%DB%8C-%D9%85%D8%B4%D8%AA%D8%B1%DB%8C-%D8%A7%D9%85%D8%A7%D8%AF%D9%87-%D9%85%DB%8C%D8%B4%D9%87/
https://torob.com/p/f3086e9c-5c48-4c3b-bb35-0c8971a22919/%DA%A9%D8%AA-%D9%88%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%AE%D8%B4-%D8%B9%D9%85%D8%AF%D9%87/
https://torob.com/p/5676dfcd-0fe4-4f0a-9015-22b0fe56ecb0/%DA%A9%D8%AA-%D8%B7%D8%B1%D8%AD-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87/
https://torob.com/p/eb98721b-60c4-493b-b088-ccbc1b24010c/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%BE%D8%A7%D9%86%D8%AF%D8%A7/
https://torob.com/p/0c11ad88-5474-4588-ab08-8cd6efe3f43d/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%84%DB%8C-%D8%AF%D8%AE%D8%AA%D8%B1%D8%A7%D9%86%D9%87-%D9%85%DB%8C%D9%86%DB%8C-%D9%85%D9%88%D8%B3-%D8%B6%D8%AE%DB%8C%D9%85-%DA%AF%D8%B1%D9%85-%D8%A8%D8%A7%D9%84%D8%A7-%D8%AA%D8%B1%DA%A9-4%D8%AA%D8%A710%D8%B3%D8%A7%D9%84-%D8%A8%D8%B1%D9%86%D8%AF-%D8%B2%D8%A7%D8%B1%D8%A7-9%D8%AA%D8%A710%D8%B3%D8%A7%D9%84/
https://torob.com/p/23c8e6ce-2178-4561-8086-0d1c93441819/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D8%A8%DA%86%DA%AF%D8%A7%D9%86%D9%87-059-%D8%B3%D8%A7%DB%8C%D8%B2-110/
https://torob.com/p/3c01fa22-7c8d-4752-9861-360d287b7856/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-%D8%A7%D8%B3%D9%86%D9%88%D9%BE%DB%8C/
https://torob.com/p/15177424-fe9e-4cb3-a723-e6c6d262dce6/%DA%A9%D8%AA-%D8%AC%DB%8C%D9%86-%D9%BE%D8%B3%D8%B1%D8%A7%D9%86%D9%87-mtb/
...
'''

f = Fetcher()
f.init()

for prk, prname in re.findall(r'https://torob.com/p/(.+)/(.+)/', raw):
    try:
        result = f.get(prk, prname)
        if result is not None:
            f.update_file(result)
    except Exception as e:
        print(f'Error {e}')
