import requests
from bs4 import BeautifulSoup
from time import sleep

site= "http://www.espncricinfo.com";
r =requests.get("http://www.espncricinfo.com/ci/engine/series/index.html?season=2014");
html_doc = BeautifulSoup(r.text);
head = html_doc.find("p", text="One-Day Internationals");
while (head.find_next_sibling().name=="dl"):
	sleep(0.005);
	elem=head.find_next_sibling();
	if elem.dt.text=="Current series" or elem.dt.text == "Forthcoming series":
		head=elem;
		break;
	match_name = elem.a.text;
	link = site + elem.a["href"];
	#going to matches page
	r2=requests.get(link);
	html_doc_match = BeautifulSoup(r2.text);
	match_head = html_doc_match.find("div", text=" Matches");
	#print r2.text;
	datas= match_head.find_next_siblings("p");
	int count =1;
	for data in datas:
		print (data);
		if count == 1:
			match_name = match_name + data.text.split(":")[0].strip("\n");
			team1 = data.span.text.split(" v ")[0].strip("\n\t");
			team2 = data.span.text.split(" v ")[1].split(" at ")[0].strip("\n\t");
			venue = data.span.text.split(" v ")[1].split(" at ")[1].strip("\n\t");
			date = data.text.split("-")[1];
			pass
		else if count == 2:
			pass
		else if count ==3:
			pass
		else if count ==4:
			pass
		else if count == 5:
			pass
		else if count ==6:
			pass
		
		#counting part
		count++;
		if count == 7:
			break;
			#count =1
	#
	break;#debugging
	head=elem;