import json, requests
from flask import Flask, jsonify


app = Flask(__name__)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
usd_rate_dontuse = parsed["bpi"]["USD"]["rate"]
eur_rate_dontuse = parsed["bpi"]["EUR"]["rate"]
usd_rate = float(usd_rate_dontuse.replace(',', ''))
satoshiUSD = format(usd_rate*0.00000001, '.8f')

eur_rate = float(eur_rate_dontuse.replace(',', ''))
satoshiEUR = format(eur_rate*0.00000001, '.8f')



@app.route('/', methods=['GET'])
def apiInformation():
    return jsonify({'USD': satoshiUSD}, {'EUR': satoshiEUR})


    return

if __name__ == "__main__":
    app.run()
