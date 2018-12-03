import json
import requests
from flask import Flask


app = flask(__name__)

@app.route('/')
def index():
    return "Index!"

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
usd_rate_dontuse = parsed["bpi"]["USD"]["rate"]
eur_rate_dontuse = parsed["bpi"]["EUR"]["rate"]


@app.route('/usdconversion')
def usdConversion():
    usd_rate = float(usd_rate_dontuse.replace(',', ''))
    satoshiUSD = format(usd_rate*0.00000001, '.8f')


@app.route('eurconversion')
def eurConversion():
    eur_rate = float(eur_rate_dontuse.replace(',', ''))
    satoshiEUR = format(eur_rate*0.00000001, '.8f')


if __name__ == "__main__":
    app.run()
