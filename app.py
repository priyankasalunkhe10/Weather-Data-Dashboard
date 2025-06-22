from flask import Flask,request,render_template,redirect,url_for,jsonify
import pandas as pd
from datetime import datetime
import requests 
import os
import random

app = Flask(__name__)
API_KEY = '4ddfcb18434453f426bb52715e6dfab4'

def generate_location_id(name):
    df = pd.read_excel('Data/Data.xlsx') if os.path.exists('Data/Data.xlsx') else pd.DataFrame()
    count = len(df) + 1
    return f"LOC{count:03d}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add_location():
    if request.method=='POST':
        df = pd.read_excel('Data/Data.xlsx')
        new_entry = {
            'Location ID': random.randint(1000,9999),
            'Location Name': request.form['city'],
            'Temperature': float(request.form['temperature']),
            'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        df = pd.concat([df,pd.DataFrame([new_entry])],ignore_index=True)
        df.to_excel('Data/Data.xlsx',index=False)
        return redirect(url_for('index'))
    return render_template('add_location.html')

@app.route('/get-weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()

    if response.get("main"):
        temperature = response["main"]["temp"]
        return render_template("index.html", city=city.title(), temperature=temperature)
    else:
        return render_template("index.html", error="City not found!")

@app.route('/save',methods=['POST'])
def save():
    weather_data = {
        'Location Id':generate_location_id('city'),
        'Location Name':request.form['city'],
        'Temperature': float(request.form['temperature']),
        'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     }
    df = pd.read_excel('Data/Data.xlsx')
    df = pd.concat([df,pd.DataFrame([weather_data])],ignore_index=True)
    df.to_excel('Data/Data.xlsx',index=False)
    return redirect(url_for('weather_history'))

@app.route('/chart-data')
def chart_data():
    if os.path.exists('Data/Data.xlsx'):
        df = pd.read_excel('Data/Data.xlsx')
        grouped = df.groupby("Location Name").agg({'Temperature': 'last'}).reset_index()
        return jsonify({
            "labels": grouped["Location Name"].tolist(),
            "temps": grouped["Temperature"].tolist()
        })
    return jsonify({"labels": [], "temps": []})

@app.route('/history',methods=['GET','POST'])
def weather_history():
    df = pd.read_excel('Data/Data.xlsx')
    
    return render_template('history.html',tables = [df.to_html(classes='table table-striped',index=False)])

if __name__ == '__main__':
    app.run(debug=True)