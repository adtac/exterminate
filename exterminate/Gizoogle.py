import sys
from bs4 import BeautifulSoup
import requests


def translate(text):
    """
    Takes string as input and returns the gizzoogled version of that string
    """
    url = 'http://www.gizoogle.net/textilizer.php'
    payload = {'translatetext': text}
    r = requests.post(url, payload)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup.find(id='search_box').get_text().strip()
