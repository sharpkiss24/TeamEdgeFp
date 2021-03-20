from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@ app.route('/red')
def red():
    return '<h1>‘Welcome to Shariana’s Rainbow Project’</h1> '

@ app.route('/orange')
def orange():
    return 'welcome to orange'

@ app.route('/yellow')
def yellow():
    return 'sup, welcome to yellow'

@ app.route('/green')
def green():
    return 'heyo, welcome to the green lane'

@ app.route('/Blue')
def Blue():
    return 'welcome to the best color'

@ app.route('/indigo')
def indigo():
    return 'welcome to the color that people get confused'

@ app.route('/violet')
def Violet():
    return 'welcome to the purple'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


