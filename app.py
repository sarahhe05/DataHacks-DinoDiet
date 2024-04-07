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
        if result == "herbivorous":
            safety = "You're safe!"
        elif result == "omnivorous":
            safety = "Feed the dinosaur some plants or you will become the food!"
        else:
            safety = "RUN!"

        # Call your function with the dropdown values
        return render_template("index.html", display_result = result, display_safety = safety)
    
# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
