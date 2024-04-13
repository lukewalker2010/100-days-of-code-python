from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/potato')
# def welcome():
#     return 'This is my first Flask app! Yay!'

@app.route('/', methods=['GET', 'POST'])
def rootpage():
    name = ''
    food = ''
    if request.method == "POST" and 'username' in request.form:
        name = request.form.get('username')
        food = request.form.get('userfood')
    return render_template("index.html", name=name, food=food)

# @app.route('/bob')
# def bobpage():
#     return 'Hi bob!'
    
    
# @app.route('/method', methods=['GET', 'POST'])
# def method():
#     if request.method == 'POST':
#         return "You've used a POST request!"
#     else:
#         return "I reckon you're probably using a GET request."

app.run()