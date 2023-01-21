from  package.web_app_flask import app
import os

if __name__ == '__main__':
    app.run()
    #port = int(os.environ.get('PORT',5000))
    #app.run(host="0.0.0.0", port=port, debug=True)
    #app.run(host="20.50.2.60", port=port, debug=True)
    
