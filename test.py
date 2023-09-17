import requests
from bs4 import BeautifulSoup
from utils import sehirler_kod
import json
import asyncio
import random
from config import *
from pyrogram import Client
bot = Client('ayet_bot',api_hash=api_hash, api_id=api_id, bot_token=BOT_TOKEN)
with open('../ayetbot/sehirler_ilceler_kod.json', 'r') as f:
    sehirler_ilceler_kod = json.load(f)
async def get_iftar_sahur_data():
    data = {}
    for sayı, sehir in enumerate(sehirler_ilceler_kod):
        ilceler = {}
        for ilce in sehirler_ilceler_kod[sehir]:
            
            sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][ilce]}/{ilce}-icin-namaz-vakti"
            try:
                r = requests.get(sehir_ezan_link, timeout = 10)
            except Exception as e:
                print(str(e))
                pass
            soup = BeautifulSoup(r.text, 'lxml')
            
            vakitler = soup.find_all('div', attrs={'class':'today-pray-times'})[0].text.split('\n')
            vakitler = str(vakitler).replace("'', ", "").split(', ')
            vakit_iftar = vakitler[9]
            vakit_sahur = vakitler[1]
            
            print(f"{sayı}: {ilce}")
            
            ilceler.update(
                {ilce:{
                    'iftar':vakit_iftar,
                    'sahur':vakit_sahur
                    }
                }
            )
            
            #await asyncio.wait_for(asyncio.sleep(0.5), timeout=1)
            await asyncio.sleep(0.1)

            il_ve_ilceler = {sehir:ilceler}
            data.update(il_ve_ilceler)
    print('yazmaya geçtim')
    with open('../ayetbot/text_iftar_sahur.json', 'w') as f:
        json.dump(data, f, indent=4)


asyncio.run(get_iftar_sahur_data())
