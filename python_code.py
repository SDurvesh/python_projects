from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if city:
        api_key = 'API_KEY'      // Generate your api key from openweatherMap
        base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            temperature_kelvin = data['main']['temp']
            temperature_celsius = temperature_kelvin - 273.15
            description = data['weather'][0]['description']
            return render_template('index.html', city=city, temperature=round(temperature_celsius, 2), description=description)
        else:
            error = "City not found. Please try again."
            return render_template('index.html', error=error)
    else:
        error = "Please enter a city name."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
