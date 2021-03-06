from flask import *
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    img = "<img src=" + response['icon_url'] + " alt='Chucks Image'>"
    return img + "</br>" + "</br>" + '<strong>Chuck Norris Joke:</strong>' + response['value']