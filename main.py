from bs4.dammit import encoding_res
import requests
import json
import sys

from requests.models import Response

response = requests.get("https://www.myntra.com/gateway/v2/search/women-shrugs?rows=50&o=0&plaEnabled=false")
response.text
detail = json.loads(response)
totalCount = detail['totalCount']
page_no = int(totalCount/50)
