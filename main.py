import requests

from win10toast import ToastNotifier

import time

toaster = ToastNotifier()

while True:

    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    data = response.json()

    rate = data['bpi']['USD']['rate']

    toaster.show_toast("Bitcoin rate", f"Current rate is {rate}"

                       "\nPowered By CoinDesk", duration=10)

    # Для уведомления каждый час установим задержку
    time.sleep(3600)
