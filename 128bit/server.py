from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
   return render_template('main.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')

if __name__ == ("__main__"):
   app.run(debug=True)
 