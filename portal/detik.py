#nidahsiapjansetuhlgi
import html5lib
import re
from .konfigurasi import ddmmmyyyy, getReq
from scrapereport.models import history
from datetime import datetime
import time
#nama kolom berita
column =    ["article"]

#data berita
dtk_link =  []
dtk_img =   []
dtk_title = []
dtk_date =  []

#jumlah halaman
page = 1
start_time = time.time()
while page <= 99999:
    dtk_soup = getReq("https://www.detik.com/search/searchall?query=penyakit%20obat&siteid=2&sortby=time&fromdatex=01/01/2020&page={0}", page)
    print (page)
    for n in column:
        dtk = dtk_soup.findAll(n)
        for x in dtk:
            #mining berdasarkan tag
            link = x.find('a').get('href')
            if len(dtk_date) == 200:
                print ("")
            img = x.find('img').get('src')
            title = x.find('h2', {'class': 'title'}).text
            finddate = x.find('span', {'class': 'date'}).text
            temp_date = re.sub(r"(\D.*, )", "", finddate)
            date = ddmmmyyyy(re.sub(r"\s(\d*:.*)","", temp_date)) #hasil sebelom masok fungsi 17 Agu 2020
            #masukkan data kedalam list data berita
            dtk_link.append(link)
            dtk_img.append(img)
            dtk_title.append(title)
            dtk_date.append(date)
            
            if date == '01 January 2020':
                page += 999999999999999
                
        else:
            continue
        break
    page += 1

history_save = history(
    site            = 'detik',
    latest_update   = datetime.today().strftime('%d %B %Y'),
    scrap_time      = round(time.time() - start_time),
    total_news      = len(dtk_link))
history_save.save()