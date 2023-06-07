import requests
from urllib.parse import urlencode

from inc.change_links import change_links
from inc.modify_text import modify_text

from flask import Flask, request
from bs4 import BeautifulSoup


URL = 'https://news.ycombinator.com/'
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def proxy(name=''):
    params = urlencode(request.args.to_dict())

    url_path = f"{URL+name+'?'+params}"
    if not params:
        url_path = f"{URL+name}"

    response = requests.get(url_path)
    page = BeautifulSoup(response.text, 'html.parser')

    page = change_links(page, URL)
    page = modify_text(page)

    return str(page)


app.run(port=8232)
