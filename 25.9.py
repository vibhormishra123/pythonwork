# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data

def getdata(url):
	r=requests.get(url)
	return r.text

api = 'YOUR API KEY'


number = '9852638787'
country = 'IN'

htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)
