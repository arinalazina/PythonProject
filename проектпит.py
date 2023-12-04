from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def weather_recommendation():
    if request.method == 'POST':
        city_name = request.form['city']
        api_key = "79d1ca96933b0328e1c7e3e7a26cb347"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={api_key}'
        response = requests.get(url)
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        if temperature < 10:
            recommendation = "Сегодня холодно. Рекомендуется надеть теплую куртку, шапку и перчатки."
        elif temperature < 20:
            recommendation = "Сегодня прохладно. Рекомендуется надеть свитер или легкую куртку."
        else:
            recommendation = "Сегодня тепло. Рекомендуется надеть легкую одежду."

        return render_template('index.html', recommendation=recommendation, description=description)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()