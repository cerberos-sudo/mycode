import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL =" https://www.facebook.com/marketplace/111059502252148" 
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

listings = []

table = soup.find('div', attrs = {'id':'all_listings'})
