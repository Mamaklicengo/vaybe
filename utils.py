import requests
from bs4 import BeautifulSoup
from config import kuran_sure, diyanet, ezan_vakitleri
from db_code import db_yaz
#r = requests.get(kuran_sure)
#soup = BeautifulSoup(r.text, 'lxml')
#linkler = soup.find_all('a')
#
##sureler
#for sayı in range(113):
#    tefsirler = list()
#    for i in linkler:
#        link = i.get('href')
#        if link.startswith('/tefsir'):
#            tefsirler.append(diyanet+link)
#    r = requests.get(tefsirler[sayı])
#    soup = BeautifulSoup(r.text, 'lxml')
#    butun_linkler = soup.find_all('a')
#
#    #ilk surenin ayetleri
#    ayet_linkler = list()
#    for i in butun_linkler:
#        link = i.get('href')
#        if link.startswith('/tefsir'):
#            ayet_linkler.append(diyanet+link)
#
#    #ayetin bölümleri
#
#
#    ayetler = ''
#    for i in range(len(ayet_linkler)):
#        r = requests.get(ayet_linkler[i])
#        soup = BeautifulSoup(r.text, 'lxml')
#        baslik = soup.find_all('div', {'class':'panel-heading'})
#        turkçesi = soup.find_all('div', {'class':'alert alert-warning'})
#        ayet_ve_yeri = f"{(baslik[0].contents[0].replace('Tefsiri', 'Meali', 1))}\n{str(turkçesi[0].text)}***"
#        ayetler += ayet_ve_yeri
#        print(ayet_ve_yeri)
#    try:
#        db_yaz(sure=str(ayetler.split(' ')[0].replace("'", "’")), ayetler=ayetler.replace("'", "’"))
#    except:
#        pass
#sehir_ezan_link = f'https://namazvakitleri.diyanet.gov.tr/tr-TR/9158/ankara-icin-namaz-vakti'
#r = requests.get(sehir_ezan_link)
#soup = BeautifulSoup(r.text, 'lxml')
#tarih = soup.find_all('div', attrs={'class':'w3-col s7 tt-takvim'})[0].text.split(' ')

sureler = {
    'fil suresi':'https://www.namazzamani.net/assets/img/fil-suresi-okunusu.jpg',
    'kureyş suresi':'https://www.namazzamani.net/assets/img/kureys-suresi-okunusu.jpg',
    'maun suresi':'https://www.namazzamani.net/assets/img/maun-suresi-okunusu.jpg',
    'kevser suresi':'https://www.namazzamani.net/assets/img/kevser-suresi-okunusu.jpg',
    'kafirun suresi':'https://www.namazzamani.net/assets/img/kafirun-suresi-okunusu.jpg',
    'nasr suresi':'https://www.namazzamani.net/assets/img/nasr-suresi-okunusu.jpg',
    'tebbet suresi':'https://www.namazzamani.net/assets/img/tebbet-suresi-okunusu.jpg',
    'ihlas suresi':'https://www.namazzamani.net/assets/img/ihlas-suresi-okunusu.jpg',
    'felak suresi':'https://www.namazzamani.net/assets/img/felak-suresi-okunusu.jpg',
    'nas suresi':'https://www.namazzamani.net/assets/img/nas-suresi-okunusu.jpg',
}

#buton yapıcı
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
def buton_yap(liste, bas):
    butonlar = []
    for i in liste:
        button = InlineKeyboardButton(i, bas+i)
        butonlar.append(button)
    return butonlar

#butonları istediğin kadar kolona böl, 'cokca' parametresi sayesinde
def cokla(liste, cokca=2):
    coklu_liste = []
    sayi = 0
    for i in range(int(len(liste)/2+1)):
        coklu_eleman = liste[sayi:sayi+cokca]
        coklu_liste.append(coklu_eleman)
        sayi += cokca
    return coklu_liste

sehirler_kod = {
    'adana':9146,
    'adiyaman':9158,
    'afyonkarahisar':9167,
    'agri':9185,
    'amasya':9198,
    'ankara':9206,
    'antalya':9225,
    'artvin':9246,
    'aydin':9252,
    'balikesir':9270,
    'bilecik':9297,
    'bingol':9303,
    'bitlis':9311,
    'bolu':9315,
    'burdur':9327,
    'bursa':9335,
    'canakkale':9352,
    'cankiri':9359,
    'corum':9370,
    'denizli':9392,
    'diyarbakir':9402,
    'edirne':9419,
    'elazig':9432,
    'erzincan':9440,
    'erzurum':9451,
    'eskisehir':9470,
    'gaziantep':9479,
    'giresun':9494,
    'gumushane':9501,
    'hakkari':9507,
    'hatay':20089,
    'isparta':9528,
    'mersin':9737,
    'istanbul':9541,
    'izmir':9560,
    'kars':9594,
    'kastamonu':9609,
    'kayseri':9620,
    'kirklareli':9638,
    'kirsehir':9646,
    'kocaeli':9654,
    'konya':9676,
    'kutahya':9689,
    'malatya':9703,
    'manisa':9716,
    'kahramanmaras':9577,
    'mardin':9726,
    'mugla':9747,
    'mus':9755,
    'nevsehir':9760,
    'nigde':9766,
    'ordu':9782,
    'rize':9799,
    'sakarya':9807,
    'samsun':9819,
    'siirt':9839,
    'sinop':9847,
    'sivas':9868,
    'tekirdag':9879,
    'tokat':9887,
    'trabzon':9905,
    'tunceli':9914,
    'sanliurfa':9831,
    'usak':9919,
    'van':9930,
    'yozgat':9949,
    'zonguldak':9955,
    'aksaray':9193,
    'bayburt':9295,
    'karaman':9587,
    'kirikkale':9635,
    'batman':9288,
    'sirnak':9854,
    'bartin':9285,
    'ardahan':9238,
    'igdir':9522,
    'yalova':9935,
    'karabuk':9581,
    'kilis':9629,
    'osmaniye':9788,
    'duzce':9414
}
sehirler_kod2 = {
    'adana':{'adana':9146,
             'aladag':9147,
             'ceyhan':9148,
             'feke':9149,
             'imamoglu':9150,
             'karaisali':9151,
             'karatas':9152,
             'kozan':9153,
             'pozanti':9154,
             'saimbeyli':9155,
             'tufanbeyli':9156,
             'yumartalik':9157},
    'adiyaman':{'adiyaman':9158,
                'besni':9159,
                'celikhan':9160,
                'gerger':9161,
                'golbasi':9162,
                'kahta':9163,
                'samsat':9164,
                'sincik':9165,
                'tut':9166},
    'afyonkarahisar':{ 'afyonkarahisar':9167,
                       'basmakci':9168,
                       'bayat':9169,
                       'bolvadin':9170,
                       'cay':9171,
                       'cobanlar':9172,
                       'dazkiri':9173,
                       'dinar':9174,
                       'emirdag':9175,
                       'evciler':9176,
                       'hocalar':9177,
                       'ihsaniye':9178,
                       'iscehisar':9179,
                       'kiziloren':9180,
                       'sandikli':9181,
                       'sinanpasa':9182,
                       'suhut':9183,
                       'sultandagi':9184},
    'agri':{
        'agri':9185,
        'diyadin':9186,
        'dogubeyazit':9187,
        'eleskirt':9188,
        'patnos':9189,
        'taslicay':9190,
        'tutak':9191
    },
    'amasya':9198,
    'ankara':9206,
    'antalya':9225,
    'artvin':9246,
    'aydin':9252,
    'balikesir':9270,
    'bilecik':9297,
    'bingol':9303,
    'bitlis':9311,
    'bolu':9315,
    'burdur':9327,
    'bursa':9335,
    'canakkale':9352,
    'cankiri':9359,
    'corum':9370,
    'denizli':9392,
    'diyarbakir':9402,
    'edirne':9419,
    'elazig':9432,
    'erzincan':9440,
    'erzurum':9451,
    'eskisehir':9470,
    'gaziantep':9479,
    'giresun':9494,
    'gumushane':9501,
    'hakkari':9507,
    'hatay':20089,
    'isparta':9528,
    'mersin':9737,
    'istanbul':9541,
    'izmir':9560,
    'kars':9594,
    'kastamonu':9609,
    'kayseri':9620,
    'kirklareli':9638,
    'kirsehir':9646,
    'kocaeli':9654,
    'konya':9676,
    'kutahya':9689,
    'malatya':9703,
    'manisa':9716,
    'kahramanmaras':9577,
    'mardin':9726,
    'mugla':9747,
    'mus':9755,
    'nevsehir':9760,
    'nigde':9766,
    'ordu':9782,
    'rize':9799,
    'sakarya':9807,
    'samsun':9819,
    'siirt':9839,
    'sinop':9847,
    'sivas':9868,
    'tekirdag':9879,
    'tokat':9887,
    'trabzon':9905,
    'tunceli':9914,
    'sanliurfa':9831,
    'usak':9919,
    'van':9930,
    'yozgat':9949,
    'zonguldak':9955,
    'aksaray':9193,
    'bayburt':9295,
    'karaman':9587,
    'kirikkale':9635,
    'batman':9288,
    'sirnak':9854,
    'bartin':9285,
    'ardahan':9238,
    'igdir':9522,
    'yalova':9935,
    'karabuk':9581,
    'kilis':9629,
    'osmaniye':9788,
    'duzce':9414
}

import config
async def log_gonder(bot, message=None, buton=False, CallbackQuery=None):
    if buton != True:
        chat_id = message.chat.id
        chat_title = message.chat.title
        grup_username = message.chat.username
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        link = ''
        if grup_username != None:
            link = f"t.me/{grup_username}"
        await bot.send_message(config.log_grup, f"""
<u>Group:</u> <a href='{link}'>{chat_title}</a> (<code>{chat_id}</code>)
<u>User:</u> <a href='tg://user?id={user_id}'>{first_name}</a> (<code>{user_id}</code>)
{message.text}""", disable_web_page_preview=True)
    elif buton:
        first_name = CallbackQuery.from_user.first_name
        chat_id = CallbackQuery.message.chat.id
        chat_title = CallbackQuery.message.chat.title
        user_id = CallbackQuery.from_user.id
        grup_username = CallbackQuery.message.chat.username
        link = ''
        if grup_username != None:
            link = f"t.me/{grup_username}"
        await bot.send_message(config.log_grup, f"""
<u>Group:</u> <a href='{link}'>{chat_title}</a> (<code>{chat_id}</code>)
<u>User:</u> <a href='tg://user?id={user_id}'>{first_name}</a> (<code>{user_id}</code>)
{CallbackQuery.data}""", disable_web_page_preview=True)