import json
import requests
import flask


app = flask(__name__)

@app.route('/')



url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
usd_rate_dontuse = parsed["bpi"]["USD"]["rate"]
eur_rate_dontuse = parsed["bpi"]["EUR"]["rate"]

def usdConversion():
usd_rate = float(usd_rate_dontuse.replace(',', ''))
satoshiUSD = format(usd_rate*0.00000001, '.8f')

def eurConversion():
eur_rate = float(eur_rate_dontuse.replace(',', ''))
satoshiEUR = format(eur_rate*0.00000001, '.8f')


if __name__ = "__main__":
    app.run()
