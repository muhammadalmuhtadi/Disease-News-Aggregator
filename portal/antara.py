#nidahsiap!
import html5lib
import re
from datetime import datetime
from .konfigurasi import ddMyyyy, getReq
from scrapereport.models import history
import time

#nama kolom berita
column =     ["simple-post simple-big clearfix"]

#data berita
ant_link =  []
ant_img =   []
ant_title = []
ant_date =  []

#jumlah halaman
page = 1
start_time = time.time()
while page <=999999:
    ant_soup = getReq("https://www.antaranews.com/search/penyakit-obat/{0}", page)
    ant = ant_soup.find_all('article', {'class': column})
    for x in ant:
        #mining berdasarkan tag
        link = x.find('a').get('href')
        if len(ant_date) == 1000:
            print ("antara sudah 1000 berita")
        img = x.find('img').get('data-src')
        title = x.find('a').get('title')
        temp_date = x.find('span').text
        if temp_date == " 2 Januari 2020 12:36":
            break
        datetemp = re.sub(r"\s\d*:\d*", "", temp_date)
        if 'lalu' in datetemp:
            datetemp = datetime.now().strftime(" %d %B %Y")
        date = ddMyyyy(datetemp)
        ant_link.append(link)
        ant_img.append(img)
        ant_title.append(title)
        if date == '':
            date = ant_date[-1]
        ant_date.append(date)
        '''
        if len(ant_link) == 100:
            break
        '''
    else:
        page += 1
        continue
    break

history_save = history(
    site            = 'antara',
    latest_update   = datetime.today().strftime('%d %B %Y'),
    scrap_time      = round(time.time() - start_time),
    total_news      = len(ant_link))
history_save.save()
print(len(ant_link))
