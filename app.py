from flask import *  
import os
import json
from urllib.request import urlopen

app  = Flask(__name__)

@app.route('/') 

def home():
    url_api = "https://api.binance.com/api/v1/ticker/price"
    response = urlopen(url_api)
    
    data_api_json = json.loads(response.read())
    data_USDT_lsit = []

    for i in range(len(data_api_json)):
        coinname_all = data_api_json[i]['symbol']
        find_USDT = coinname_all.find("USDT")
        if find_USDT != -1:
            data_USDT_lsit.append(data_api_json[i])
        else:
            pass
        
    coinname_USDT_list = []
    for j in range(len(data_USDT_lsit)):
        coinname_USDT = data_USDT_lsit[j]['symbol']
        coinname_USDT_list.append(coinname_USDT)
    print(coinname_USDT_list)
    print(type(coinname_USDT_list))
    return render_template('index.html', coinname=coinname_USDT_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)    
    
    
