from flask import Flask, render_template, request

# uses https://purecss.io/

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    weight = ''
    # height = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        # height = float(request.form.get('height'))
        bmi = calc_bmi(weight)

    return render_template("index.html", bmi=bmi)

def calc_bmi(weight):
    return round(weight * 0.6 / 158, 3)

app.run()

