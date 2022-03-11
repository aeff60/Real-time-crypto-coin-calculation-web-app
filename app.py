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

    return render_template('index.html', coinname=data_api_json)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)    
    
    
