import requests
from bs4 import BeautifulSoup
import pprint
import csv
from .scrape import (
  get_kurslink
)


def scrape_page_metadata(url):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    pp = pprint.PrettyPrinter(indent=4)
    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    metadata = {
        'https://www.ecampus.fh-potsdam.de/course/view.php?id=' +str(get_kurslink(html)),
        }
    return metadata
