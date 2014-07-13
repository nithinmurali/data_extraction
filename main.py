import requests
from bs4 import BeautifulSoup

site= "http://www.espncricinfo.com";
r =requests.get("http://www.espncricinfo.com/ci/engine/series/index.html?season=2014");
html_doc = BeautifulSoup(r.text);
head = html_doc.find("p", text="One-Day Internationals");
while (head.find_next_sibling().name=="dl"):
	#dealy
	elem=head.find_next_sibling();
	if elem.dt.text=="Current series" or elem.dt.text == "Forthcoming series":
		head=elem;
		break;
	match_name = elem.a.text;
	link = site + elem.a["href"];
	#goijng to matches page
	r2=requests.get(link);
	html_doc_match = BeautifulSoup(r2.text);
	match_head = html_doc_match.find("div", text="Matches");


	head=elem;