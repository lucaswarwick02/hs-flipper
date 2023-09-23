import os
from dotenv import load_dotenv
import requests
import json


PRODUCT_IDS_PATH = './product_ids.json'


def get_bazaar_ids():
    
    if not os.path.exists(PRODUCT_IDS_PATH):
        # File doesn't exist so we need to get the product IDs for the Bazaar items 
        api_key = os.getenv("api_key")
        response = requests.get(f'https://api.hypixel.net/skyblock/bazaar?key={api_key}')
        print(f'Bazaar Product IDs Status: {response.status_code}')
    
        # Save response to file
        with open(PRODUCT_IDS_PATH, 'w') as f:
            json.dump(response.json(), f)
            print(f'Bazaar product IDs successfully saved to {PRODUCT_IDS_PATH}')


if __name__ == '__main__':
    load_dotenv()
    
    get_bazaar_ids()