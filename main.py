import requests
from bs4 import BeautifulSoup

r =requests.get("http://www.espncricinfo.com/ci/engine/series/index.html?season=2014");
html_doc = BeautifulSoup(r.text);
print type(html_doc);
