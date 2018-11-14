from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("index.html") # Is the index.html file supposed to sit in the home directory?

@app.route("/home/api")
def api():
    mydict = csvdict.csvcleanse.py  # We've tried to put the csvcleanse.py file into an api directory
                                       # which is also inside the home directory, but when running it, it still gives us "URL Not found"
    return make_response(json.dumps(mydict))

if __name__ == '__main__':
    app.run(debug=True)
