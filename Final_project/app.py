from flask import flask, render_template, current_app as app

app = flask(__name__)

@app.route('/name')
def Home():
    return '<h1>homepage</h1>'

if __name__ = '__main__':
    app.run(debug= true,host= '0.0.0.0')