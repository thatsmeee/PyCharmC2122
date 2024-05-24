import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate


def get_usd_exchange_rate():
    url = "https://privatbank.ua/rates-archive"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    exchange_rate_div = soup.find("div", class_="purchase")
    exchange_rate = float(exchange_rate_div.text.replace(",", "."))
    return exchange_rate


def main():
    usd_exchange_rate = get_usd_exchange_rate()
    converter = CurrencyConverter(usd_exchange_rate)
    amount = float(input("Введіть суму у вашій валюті: "))
    usd_amount = converter.convert_to_usd(amount)
    print(f"Еквівалентна сума у доларах США: {usd_amount:.2f}")


if __name__ == "__main__":
    main()
