import requests
import certifi
import time
import hashlib
import hmac

api_key = "your_api_key"
api_secret = "your_api_secret"
timestamp = int(time.time() * 1000)
ads_no = "your_20_digit_ads_no"
query_string = f"adsNo={ads_no}&timestamp={timestamp}"
signature = hmac.new(api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

url = f"https://api.binance.com/sapi/v1/c2c/ads/getDetailByNo?{query_string}&signature={signature}"
headers = {
    'X-MBX-APIKEY': api_key
}
response = requests.post(url, headers=headers, verify=certifi.where())
print(response.json())
