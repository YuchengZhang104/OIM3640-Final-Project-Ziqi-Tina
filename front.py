from flask import Flask, render_template, request, escape
from back import get_daily_cal
from back import all_category

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=["GET", "POST"])
def features():
    """
    If inputs properly inputed, return the result page of html, else, return the input page.
    """
    if request.method == "POST":
        age = request.form["Age"]
        gender = request.form["Gender"]
        height = request.form["Height"]
        weight = request.form["Weight"]
        activitylevel = request.form["Activity Level"]
        goal = request.form["Goal"]
        cal = float(get_daily_cal(age, gender, height, weight, activitylevel, goal))

        res = all_category(cal)
        result = str(escape(res)).replace('\n', '<br/>')
        return render_template("results.html", response = result) 
    else:      
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
