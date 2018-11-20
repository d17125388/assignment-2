from flask import (
    Flask, render_template, make_response
)
import json
import csv_reader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def api():
    dict_data = csv_reader.get_count()
    json_data = json.dumps(dict_data)
    res = make_response(json_data)
    # res.headers.set('Access-Control-Allow-Origin', '*')
    return res

if __name__ == '__main__':
    app.run(debug=True)
