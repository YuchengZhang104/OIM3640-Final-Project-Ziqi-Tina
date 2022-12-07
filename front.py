from flask import Flask, render_template, request
from back import get_daily_cal
from back import all_category

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=["GET", "POST"])
def features():
    while request.method == "POST"
    if request.method == "POST":
        age = request.form["Age"]
        gender = request.form["Gender"]
        height = request.form["Height"]
        weight = request.form["Weight"]
        activitylevel = request.form["Activity Level"]
        goal = request.form["Goal"]
        cal = float(get_daily_cal(age, gender, height, weight, activitylevel, goal))

        res = all_category(cal)
        return render_template("results.html", response = res) 
    else:      
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
