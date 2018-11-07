
from flask import Flask, render_template, json, make_response
import csvdict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    mydict = {"0-2 years": "10", "3-5 years": "4", "6-8 years": "15"}
    return make_response(json.dumps(mydict))

if __name__ == '__main__':
    app.run(debug=True)