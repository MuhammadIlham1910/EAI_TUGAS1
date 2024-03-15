from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def root():
    return 'Selamat datang di laliga!'

@app.route('/laliga')
def laliga():
    url = "https://laliga-standings.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": "755ea1304fmsh6f50cb91b003db9p123f93jsn64eaa8799086",
        "X-RapidAPI-Host": "laliga-standings.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    klasmen = response.json()   

    return render_template('laliga.html', data=klasmen)

if __name__ == '__main__':
    app.run(debug=True)