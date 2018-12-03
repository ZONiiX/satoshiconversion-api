import json
import requests
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
        usd_rate = float(usd_rate_dontuse.replace(',', ''))
        satoshiUSD = format(usd_rate*0.00000001, '.8f')

        eur_rate = float(eur_rate_dontuse.replace(',', ''))
        satoshiEUR = format(eur_rate*0.00000001, '.8f')


        returnthis = print("$:", satoshiUSD, "€:", satoshiEUR )

        return returnthis
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
    return satoshiUSD

@app.route('/eurconversion')
def eurConversion():
    eur_rate = float(eur_rate_dontuse.replace(',', ''))
    satoshiEUR = format(eur_rate*0.00000001, '.8f')
    return satoshiEUR


if __name__ == "__main__":
    app.run(debug=True)
