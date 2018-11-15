
from bs4 import BeautifulSoup

def getTitle(fname):
    htmlFile = open(fname, 'r', encoding='utf-8')
    try:
        bsObj = BeautifulSoup(htmlFile.read(), "html.parser")
        title = bsObj.head.h1
    except AttributeError as e:
        return None
    return title


fname = ".\demo3.html"
title = getTitle(fname)
if(title == None):
    print("Title not found")
else:
    print(title)