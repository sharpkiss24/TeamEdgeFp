from flask import Flask, render_template, current_app as app

app = Flask(__name__)

  
@app.route('Rainbow')
def Red():
    return render_template('index.html',
     color = Red)

@app.route('Orange')
def Orange():
    return render_template('index.html',
    color1 = Orange)

@app.route('Yellow')
def Yellow():
    return render_template('index.html',
    color2 = Yellow)

@app.route('Green')
def Green():
    return render_template('index,html',
    color3 = Green)

@app.route('Blue')
def Blue():
    return render_template('index.html',
    color4 = Blue)

@app.route('Indigo')
def Indigo():
    return render_template('index.html',
    color5 = Indigo)

@app.route('Violet')
def Violet():
    return render_template('index.html',
    color6 = Violet)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')