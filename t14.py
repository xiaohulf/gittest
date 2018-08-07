from bs4 import BeautifulSoup
import urllib.request
import datetime
import random
import re
import io
import sys
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url = "http://cl.gtta.pw/htm_data/7/1702/2278418.html"
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

def save_file(file_name, data):
    path = "D:\\ct\\1111\\"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()
	
def handleImage(imUrl):
    name = imUrl[-10:]
    aa = urllib.request.build_opener()
    aa.addheaders = [headers]
    d = opener.open(imUrl).read()
    save_file(name,d)

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

bsObj = BeautifulSoup(data,"html.parser")

images = bsObj.findAll("img",{"src":re.compile("https:\/\/go\.imgs\.co\/u\/2017\/02\/27\/")})

for image in images:
    imageUrl = image["src"]
    handleImage(imageUrl)

