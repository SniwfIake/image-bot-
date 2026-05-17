import requests
from config import API_URL

def generate_image(prompt):

    r = requests.get(API_URL, params={"prompt": prompt})

    if r.status_code != 200:
        raise Exception("API request failed")

    return r.content
