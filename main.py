from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

API_KEY = '713b3bc42e0347908266ccda992ab44a'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = send_request()
        return show_result(result)
    else:
        return show_form()

def send_request():
    name = request.form.get('name')
    street = request.form.get('street')
    city = request.form.get('city')

    params = {
        'q': f'{city}',
        'key': API_KEY
    }

    response = requests.get('https://api.opencagedata.com/geocode/v1/json', params=params)
    result = json.loads(response.content)

    return result

def show_form():
    return render_template('form.html')

def show_result(result):
    result = result['results'] if 'results' in result else []
    return render_template('result.html', result=result)


if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0', port=8080)