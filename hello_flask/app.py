from  flask import Flask, render_template
from datetime import date
import requests


app = Flask(__name__)

@ app.route('/')
def index():
    return render_template('index.html')

@ app.route('/about')
def about():
    return  '<h1>about< /h1><p1> some other content< /p> '

@app.route('/Space')
def show_Nasa_pic():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('Nasa.html',date=data)

if __name__ ==  '__main__':
	app.run(debug= True,host= '0.0.0.0')