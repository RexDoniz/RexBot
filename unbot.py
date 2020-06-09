from tokens import cmc_token

import json

import requests

def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/lastest'
    params = {'symbol': crypto, 'convert': 'USD'}
    headers = {'X-CMC_PRO_API_KEY': cmc_token}

    r = requests.get(url, headers=headers, params=params).json()

    price = r['data'][crypto]['quote']['USD']['price']

    return price

def main():
    print (get_cmc_data('BTC'))

    # https://api.telegram.org/bot1128246059:AAH4PDhgzwiCVrJ2xkfw8dMKD-4hZ07ugWA/getMe

if __name__ == '__main__':
    main()