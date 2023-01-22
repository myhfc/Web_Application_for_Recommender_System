import os
import pandas as pd
#import azure.functions as func
from flask import (Flask, render_template ,request, url_for, send_from_directory)

app = Flask(__name__)

# Home Page
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html', predict=False)

# Hello Page
@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

if __name__ == '__main__':

    app.run(debug=True)
    """port = int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    """
