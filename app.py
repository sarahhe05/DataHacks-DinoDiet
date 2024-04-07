# Importing required libs
from flask import Flask, render_template, request
from model import predict_one

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        period = request.form['dropdown1']
        location = request.form['dropdown2']
        type = request.form['dropdown3']
        length = request.form['dropdown4']
        result = predict_one(period, location, type, length)
        # Call your function with the dropdown values
        print(result)

# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
