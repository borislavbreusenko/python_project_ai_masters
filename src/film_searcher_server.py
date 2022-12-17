import json

from flask import Flask
import requests
from waitress import serve

from film import Film
from private_consts import KINOPOISK_TOKEN


app = Flask(__name__)


@app.route("/touch")
def touch() -> str:
    return "You are talking to flask server!"


def make_headers() -> dict[str, str]:
    headers = {"X-API-KEY": KINOPOISK_TOKEN,
               "Content-Type": "application/json"}
    return headers


def make_request(headers: dict[str, str], name: str) -> requests.Response:
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}&page=1"
    response = requests.get(url, headers=headers)
    return response


def get_answer(response: requests.Response) -> str:
    if response.status_code != 200:
        return "Bad request!"
    try:
        data = response.json()["films"][0]
        film = Film(**data)
        my_resp = {'info': str(film), 'poster': film.get_poster()}
        return json.dumps(my_resp)
    except Exception:
        return "Bad request!"


@app.route("/search/<string:film_name>")
def search_film(film_name: str) -> str:
    print('New request: ', film_name)
    headers = make_headers()
    response = make_request(headers, film_name)
    print('Status:', response.status_code)
    my_answer = get_answer(response)
    return my_answer


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=port)
    host = '127.0.0.1'
    port = 5000
    serve(app, host=host, port=port)
