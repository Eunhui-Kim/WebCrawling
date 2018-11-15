from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getImages(url):
    try:
        htmlFile = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(htmlFile, "html.parser")
        reExpression = "http:\/\/gdimg1\.gmarket\.co\.kr\/goods_image2\/small_moreimg\/643\/302\/643302475\/643302475_0[0-2]+\.jpg\?ver=1533087275"
        images = bsObj.findAll('img', {"src":re.compile(reExpression)})
        for image in images:
            print(image["src"])
    except AttributeError as e:
        return None


url = "http://item.gmarket.co.kr/Item?goodscode=643302475"
img = getImages(url)
if(img == None):
    print("img not found")

