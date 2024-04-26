import requests
from bs4 import BeautifulSoup
import urllib.request
import csv
from datetime import datetime
import threading
from time import sleep
id_counter = 0
threads = []
results = []
def threaded_function(url):
    global id_counter
    zival = requests.get(url)
    zival.encoding = 'utf-8'
    soup = BeautifulSoup(zival.text, 'html.parser', from_encoding="utf-8")
    titles = soup.find_all("span", {"class": "titleorange"})
    if(len(titles) > 0):
        zival_dict = {}
        if('pes' in link['href']):
            zival_dict['tip'] = 'pes'
        elif('muc' in link['href']):
            zival_dict['tip'] = 'muc'
        zival_dict['id'] = id_counter
        veterinarska = {}
        veterinarska['id'] = id_counter
        veterinarska['cipirana'] = 0
        veterinarska['sterilizirana_kastrirana'] = 0
        veterinarska['cepljena'] = 0
        ime = titles[0].text
        zival_dict['ime'] = "".join(ime.split())
        parent_element = titles[0].find_parent('p')
        if(parent_element):
            opisi = parent_element.find_all("span", {"class": "opis"})
            if(len(opisi) == 0):
                opisi = parent_element.find_all("span", {"class": "noga1"})
            for opis in opisi:
                next_sibling_content = opis.find_next_sibling(string=True).strip()
                if(opis.text == 'datum sprejema:'):
                    next_sibling_content = next_sibling_content.replace(" ", "")
                    try:
                        datetime_object = datetime.strptime(next_sibling_content, '%d.%m.%Y')
                        datetime_object = datetime_object.strftime("%d/%m/%Y")
                        zival_dict['datum_sprejema'] = datetime_object
                    except:
                            datetime_object = ''
                elif(opis.text == 'status:'):
                    if('oddan' in next_sibling_content.lower()):
                        date_oddaje = next_sibling_content.split(" ",1)[1]
                        date_oddaje = date_oddaje.replace(" ", "")
                        while(True):
                            if(date_oddaje[-1] == '.'):
                                date_oddaje = date_oddaje[:-1]
                            else:
                                break
                        try:
                            datetime_object = datetime.strptime(date_oddaje, '%d.%m.%Y')
                            zival_dict['datum_oddaje'] = datetime_object.strftime("%d/%m/%Y")
                        except:
                            zival_dict['datum_oddaje'] = 'x'
                        
                    else:
                        zival_dict['datum_oddaje'] = 'x'
                elif(opis.text == 'spol:'):
                    zival_dict['spol'] = next_sibling_content
                elif(opis.text == 'FeLV+FIV:'):
                    zival_dict['felvfiv'] = next_sibling_content
                elif(opis.text == 'starost ob sprejemu:'):
                    #zival_dict['starost'] = next_sibling_content
                    pass
                if('veterinarska oskrba:' in opis.text):
                    things_done = next_sibling_content.split(', ')
                    for thing in things_done:
                        if("čipiran" in thing.lower()):
                            veterinarska['cipirana'] = 1
                        if("steriliziran" in thing.lower() or "kastriran" in thing.lower()):
                            veterinarska['sterilizirana_kastrirana'] = 1
                        if("cepljen" in thing.lower()):
                            veterinarska['cepljena'] = 1
            #print(url)
            #print(zival_dict)
            zivali_dict.append(zival_dict)
            veterinarska_dict.append(veterinarska)
            id_counter+=1
def thread2(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding="utf-8")
    tables = soup.find_all("table")
    names =[]
    for table in tables:
        links = table.find_all("a")
        if(links is not None):
            for link in links:
                if('Več informacij' in str(link)):
                    if('pes/' in link['href'] or 'muc/' in link['href'] ):
                        print(link['href'])
                        url = "https://www.zavetisce-horjul.net/" + link['href']
                        if('pes' in url or 'muc' in url):
                            if(link['href'] not in names):
                                names.append(link['href'])
                                t = threading.Thread(target = threaded_function, args = (url, ))
                                t.start()
                                threads.append(t)
            for t in threads:
                t.join()
url = "https://www.zavetisce-horjul.net"
urls = []
zivali_fields = ['id', 'ime', 'datum_sprejema', 'datum_oddaje', 'spol', 'felvfiv', 'tip']
zivali_dict = []
veterinarska_fields = ['id', 'sterilizirana_kastrirana', 'cepljena', 'cipirana']
veterinarska_dict = []

url = "https://www.zavetisce-horjul.net/spet_doma.php"
r = requests.get(url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.content, 'html.parser', from_encoding="utf-8")
arhiv = soup.find("a", text="Arhiv - 2018")
arhiv_parent = arhiv.find_parent('p')
links = arhiv_parent.find_all("a")[2:-2]
for link in links:
    urls.append("https://www.zavetisce-horjul.net" + link['href'])
#print(urls)
for url in urls:
    #print(url)
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding="utf-8")
    tables = soup.find_all("table")
    names =[]
    for table in tables:
        links = table.find_all("a")
        if(links is not None):
            for link in links:
                if('Več informacij' in str(link)):
                    if('pes/' in link['href'] or 'muc/' in link['href'] ):
                        print(link['href'])
                        url = "https://www.zavetisce-horjul.net/" + link['href']
                        if('pes' in url or 'muc' in url):
                            if(link['href'] not in names):
                                names.append(link['href'])
                                t = threading.Thread(target = threaded_function, args = (url, ))
                                t.start()
                                threads.append(t)
            for t in threads:
                t.join()

                               
filename = "zivali.csv"
with open(filename, 'w', encoding='utf-8') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=zivali_fields)
 
    # writing headers (field names)
    writer.writeheader()
 
    # writing data rows
    writer.writerows(zivali_dict)

filename = "veterinarska_oskrba.csv"
with open(filename, 'w', encoding='utf-8') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=veterinarska_fields)
 
    # writing headers (field names)
    writer.writeheader()
 
    # writing data rows
    writer.writerows(veterinarska_dict)