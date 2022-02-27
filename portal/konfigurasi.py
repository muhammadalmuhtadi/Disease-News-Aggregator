from datetime import datetime
import re

#bersihin tanggal 
def ddmmmyyyy(date):
    if "Agu" in date:
        date = re.sub('gu', 'ug', date)
    if "Mei" in date:
        date = re.sub('ei', 'ay', date)
    if "Des" in date:
        date = re.sub('s', 'c', date)
    if "Okt" in date:
        date = re.sub('kt', 'ct', date)
    date_format = datetime.strptime(date, '%d %b %Y')
    return date_format.strftime("%d %B %Y")

def ddmmyyyy(date):
    date_format = datetime.strptime(date, '%d %m %Y')
    return date_format.strftime("%d %B %Y")

def ddMyyyy(date):
    if "Januari" in date:
        date = re.sub('i', 'y', date) 
    elif "Februari" in date:
        date = re.sub('i', 'y', date) 
    elif "Maret" in date:
        date = re.sub('et', 'ch', date)
    elif "Mei" in date:
        date = re.sub('ei', 'ay', date) 
    elif "Juni" in date:
        date = re.sub('i', 'e', date) 
    elif "Juli" in date:
        date = re.sub('i', 'y', date) 
    elif "Agustus" in date:
        date = re.sub('gustus', 'ugust', date)  
    elif "Oktober" in date:
        date = re.sub('k', 'c', date)  
    elif "Desember" in date:
        date = re.sub('Des', 'Dec', date)
    elif date == '':
        return ('')
    date_format = datetime.strptime(date, ' %d %B %Y')
    return date_format.strftime("%d %B %Y")

#method get req dan souping data
def getReq(link, page):
    import requests
    from bs4 import BeautifulSoup
    req = requests.get(link.format(page))
    souped = BeautifulSoup(req.content, 'html5lib')
    return souped
