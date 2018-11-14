from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/home/api")
def api():
    mydict = csvdict.csvcleanse.py  # json
    return make_response(json.dumps(mydict))

if __name__ == '__main__':
    app.run(debug=True)
