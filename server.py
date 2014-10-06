from flask import Flask
from flask import render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/priscilla")
def priscilla():
    return render_template('pretty-girl.html')
    
@app.route("/map")
def map():
    return render_template('map.html')
    




if __name__ == "__main__":
    app.run()