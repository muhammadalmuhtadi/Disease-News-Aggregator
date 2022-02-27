def kumpul():
    from scrapereport.models import history
    from portal import detik as dtk
    from portal import kompas as kmp
    from portal import antara as ant


    data = [] 
    '''
    data = 
    [

    [https://health.detik.com/berita-detikhealth/d-5232128/peneliti-sebut-dampak-covid-19-bisa-bikin-otak-menua-10-tahun,
    Peneliti Sebut Dampak COVID-19 Bisa Bikin Otak 'Menua' 10 Tahun,
    https://akcdn.detik.net.id/community/media/visual/2020/05/13/af89eb1c-1588-4470-8e0c-022c4cdd9a5b_43.jpeg?w=250&q=,
    October 2020],
    
    [https://health.detik.com/berita-detikhealth/d-5232128/peneliti-sebut-dampak-covid-19-bisa-bikin-otak-menua-10-tahun,
    Peneliti Sebut Dampak COVID-19 Bisa Bikin Otak 'Menua' 10 Tahun,
    https://akcdn.detik.net.id/community/media/visual/2020/05/13/af89eb1c-1588-4470-8e0c-022c4cdd9a5b_43.jpeg?w=250&q=,
    October 2020],
    ......
    ....
    ..
    ]
    '''
    judul = dtk.dtk_title + ant.ant_title + kmp.kmp_title
    link = dtk.dtk_link + ant.ant_link + kmp.kmp_link
    img = dtk.dtk_img + ant.ant_img + kmp.kmp_img
    date = dtk.dtk_date + ant.ant_date + kmp.kmp_date



    for a,b,c,d in zip(link,judul,img,date):
        if 'kompas.com' in a:
            e = 'kompas'
            data.append([a,b,c,d,e])
        elif 'detik.com' in a:
            e = 'detik'
            data.append([a,b,c,d,e])
        elif 'antaranews.com' in a:
            e = 'antara'
            data.append([a,b,c,d,e])

    
    return data

datas = kumpul()



