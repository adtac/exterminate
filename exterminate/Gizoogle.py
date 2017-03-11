import sys
from bs4 import BeautifulSoup
import requests
import random


def translate(text):
    """
    Takes string as input and returns the gizzoogled version of that string
    """
    url = 'http://www.gizoogle.net/textilizer.php'
    payload = {'translatetext': text}
    r = requests.post(url, payload)
    soup = BeautifulSoup(r.content, "html.parser")
    new = soup.find(id='search_box').get_text().strip()

    if new == text or "Click here to learn more about Gizoogle" in new:
        return ''.join(c for c in text if random.randint(0, 10) < 10)
    else:
        return new
