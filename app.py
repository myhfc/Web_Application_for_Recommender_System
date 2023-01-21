import os
import pandas as pd
#import azure.functions as func
from flask import (Flask, render_template ,request)

app = Flask(__name__)

STATIC_FOLDER ='static/'
MODEL_FOLDER = STATIC_FOLDER + 'models/'
DATA_FOLDER = STATIC_FOLDER + 'data/'

@app.before_first_request
def load__data():
    """
    Load predicted data
    :return: model (global variable)
    """
    print('[INFO] Predicted data Loading ........')
    global data
    data = pd.read_pickle(os.path.join(os.curdir, 'static\\data\\prediction_content_based.pickle'))

def predict(user_id, rs_type="content_based"):
    # Prediction:
    result_pred = list(data[data["user_id"]==str(user_id)]["article_id"]) 
    return result_pred

# Home Page
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        user_id = request.form["user_id"]
        print( user_id)
        #rs_type = request.form["rs_type"]
        result_pred = predict(user_id)
        print(result_pred)

        return render_template('index.html', data=data, userId=user_id, result_pred=result_pred, predict=True)
    else:
        return render_template('index.html', data=data, predict=False)

# Hello Page
@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

if __name__ == '__main__':

    app.run(debug=True)
    """port = int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    """
