#nidahsiapjansetuhlgi!
import html5lib
import re
from .konfigurasi import getReq, ddmmyyyy
from scrapereport.models import history
from datetime import datetime
import time

#nama kolom berita
column =    ["col-bs9-6", "col-bs9-3", "article__list clearfix"]

import time#deletdis

#data berita
kmp_link =  []
kmp_img =   []
kmp_title = []
kmp_date =  []

#jumlah halaman
page = 1
start_time = time.time()
while page <=9999:
    kmp_soup = getReq("https://www.kompas.com/tag/penyakit?sort=desc&page={0}", page)
    for n in column:
        kmp = kmp_soup.find_all('div', {'class': n})
        for x in kmp:
            #mining berdasarkan tag
            link = x.find('a').get('href')
            img = x.find('img').get('src')
            title = x.find('a', {'class': 'article__link'}).text
            temp_date = x.find('div', {'class': 'article__date'}).text
            if temp_date == '01/01/2020, 07:02 WIB': #or len(kmp_link) == 100 2nd limit
                page += 200000
                break
            date = ddmmyyyy(re.sub(r",\s.*", "", temp_date).replace('/',' ')) #Hasil sebelum masok fungsi : 02 09 2020
            #masukkan data kedalam list data berita
            kmp_link.append(link)
            kmp_img.append(img)
            kmp_title.append(title)
            if len(kmp_link) == 1000:
                print("kompas sudah 1000")
            kmp_date.append(date)
            '''
            #batas
            if len(kmp_link) == 100:
                page += 200000
                break
            '''
        else:
            continue
        break
    page += 1                

history_save = history(
    site            = 'kompas',
    latest_update   = datetime.today().strftime('%d %B %Y'),
    scrap_time      = round(time.time() - start_time),
    total_news      = len(kmp_link))
history_save.save()
print(len(kmp_link))
