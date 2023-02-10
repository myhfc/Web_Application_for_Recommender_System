import requests
from flask import (Flask, render_template ,request)#, url_for, send_from_directory)

app = Flask(__name__)

# Home Page
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=="POST":
        userid = request.form["user_id"]
        print(userid)
        article_score = requests.get("https://oc-09-function-02.azurewebsites.net/api/HttpTrigger1", params={"userid":userid})
        recommended_articles = str(article_score.content)[2:-2]
        list_recommended_articles = recommended_articles.split(sep=",")
        
        return render_template('index.html', predict=True, userId=userid, recommended_articles=list_recommended_articles)
    else:
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
