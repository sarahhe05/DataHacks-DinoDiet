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
        period = request.form['geological_period']
        location = request.form['country']
        dino_type = request.form['dinosaur_type']
        length = request.form['length']
        result = predict_one(period, location, dino_type, length)
        # Call your function with the dropdown values
        return result
    
# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
