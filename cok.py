import re,requests,bs4,json
from bs4 import BeautifulSoup as parser
ses=requests.Session()
n,cok,cookie=0,[],[]

url = parser(ses.get("https://mbasic.facebook.com/100072216287842/posts/213375447746330/?app=fbl").text,"html.parser")
for z in url("span"):
	cok.append(z.text)
for x in "".join(cok).split("datr"):
	cok = f"datr{x}"
	if cok in cookie:
		pass
	else:
		if "Beranda" in cok:
			pass
		else:
			n+=1
			cookie.append(cok)
			print(f"{n}. {cok}\n")
		
ask = input(" masukan : ")
print(cookie[int(ask)-1])
