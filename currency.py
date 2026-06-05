import requests
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
  currencies = ','.join(CURRENCIES)
  url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
  try:
    response = requests.get(url)
    data = response.json()
    return data["data"]
  except Exception as e:
    print(e)
    return None


while True:
  base = input("Enter the base currency (q for quit): ").upper()

  if base == "Q":
    break

  data = convert_currency(base)

  if not data:
    continue

  del data[base]
  for ticker, value in data.items():
    print(f"{ticker}: {value}")