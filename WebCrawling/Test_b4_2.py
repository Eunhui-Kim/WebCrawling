from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        htmlFile = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(htmlFile.read(), "html.parser")
        title = bsObj.title
    except AttributeError as e:
        return None
    return title


url = "http://plus.cnu.ac.kr/"
title = getTitle(url)
if(title == None):
    print("Title not found")
else:
    print(title)