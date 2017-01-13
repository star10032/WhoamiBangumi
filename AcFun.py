# -*- coding:utf_8 -*-
import urllib2
from bs4 import BeautifulSoup
from Bangumi import Bangumi

AcFunURL = "http://www.acfun.cn"

def getAcfun():
    """AcFun processing function"""
    # Get AcFun bangumi HTML
    req = urllib2.Request(AcFunURL)
    try:
        res = urllib2.urlopen(req)
        html = res.read()
    except urllib2.URLError:
        return Bangumi.empty('AcFun')
    bangumi = Bangumi('AcFun')
    # Give the HTML to BeautifulSoup
    # TODO: Change the parser to lxml for better performance
    soup = BeautifulSoup(html, "html.parser")
    # Get lists of a week
    bweek = soup.find_all(class_="time-block")
    wd = 1
    for binfoList in bweek:
        binfos = binfoList.find_all('li')
        for binfo in binfos:
            bname = binfo.find('b').string
            bupdate = binfo.find('p').string
            # Remove special character may cause GBK encoding error
            if '•'.decode('utf-8') in bupdate:
                bupdate = bupdate[2:]
            bangumi.add(wd, bname, bupdate)
        wd += 1
    return bangumi
    
    
