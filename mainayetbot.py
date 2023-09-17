from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import *
from db_code import veri_tabanindan_getirme
import asyncio
import random
import requests
from utils import sureler, sehirler_kod, buton_yap, cokla, log_gonder
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaPhoto
import gruplar_db.kullanıcılar as gk
from io import BytesIO

from datetime import datetime, timedelta
from pyrogram import errors

bot = Client('ayet_bot',api_hash=api_hash, api_id=api_id, bot_token=BOT_TOKEN)



@bot.on_message(filters.command('start'))
async def start(bot:Client, message:Message):
    chat_id = message.chat.id
    name = message.from_user.first_name.replace("'", "").replace('"', '')
    user_id = message.from_user.id
    username = message.from_user.username
    if username == None:
        username = 'None'
    try:    
        await log_gonder(bot=bot, message=message)
    except:
        pass
    buton = [[InlineKeyboardButton('KOMUTLAR', 'komutlar')], [InlineKeyboardButton('NAMAZ SURELERİ', 'namaz_sureleri_baslat')]] #, [InlineKeyboardButton('GENEL BİLGİ', 'genel_bilgi')]
    await bot.send_message(chat_id, "Esselamu aleykum ve rahmetullahi ve berekatuhu ve magfiratuhu ebeden ve daimen. (Rabbimin selamı, rahmeti, bereketi ve mağfireti daimi ve ebedi olarak sizin üstünüze olsun) 🌙", 
                           reply_markup=InlineKeyboardMarkup(buton))
    if gk.dbde_var_mi(user_id):
        return
    else:
        gk.db_yazici(id=user_id, firstname=name, username=username)

@bot.on_message(filters.command('ayet'))
async def ayet(bot:Client, message:Message):
    chat_id = message.chat.id
    try:
        random_sayı = random.randint(0, 112)
        ayet = random.choice(veri_tabanindan_getirme(kolon='ayetler', istenilenveri=random_sayı).replace("'", "").replace(r'\n', '\n').replace(r'\r', '').split('***'))
        await bot.send_message(chat_id, str(ayet))
    except errors.MessageEmpty:
        try:
            ayet = random.choice(veri_tabanindan_getirme(kolon='ayetler', istenilenveri=random_sayı).replace("'", "").replace(r'\n', '\n').replace(r'\r', '').split('***'))
            await bot.send_message(chat_id, str(ayet))
        except errors.MessageEmpty as e:
            try:
                ayet = random.choice(veri_tabanindan_getirme(kolon='ayetler', istenilenveri=random_sayı).replace("'", "").replace(r'\n', '\n').replace(r'\r', '').split('***'))
                await bot.send_message(chat_id, str(ayet))
            except Exception as e:
                await bot.send_message(log_grup, f"#hata\nTanımsız hata Ayet komutu\n{e}")
    except Exception as e:
        await bot.send_message(log_grup, f"#hata\nTanımsız hata Ayet komutu\n{e}")
    try:    
        await log_gonder(bot=bot, message=message)
    except:
        pass
        

@bot.on_message(filters.regex('imanla bizi'))
async def imanpower(bot:Client, message:Message):
    chat_id = message.chat.id
    random_sayı = random.randint(0, 112)
    ayet = random.choice(veri_tabanindan_getirme(kolon='ayetler', istenilenveri=random_sayı).replace("'", "").replace(r'\n', '\n').replace(r'\r', '').split('***'))
    await bot.send_message(chat_id, str(ayet))


def turkce_karakterleri_duzelt(girdi, karakter_sozlugu=None):
    if not karakter_sozlugu:
        karakter_sozlugu = {"ğ":"g", "Ğ":"G", "ç":"c", "Ç":"C", "ş":"s", "Ş":"S", "ü":"u", "Ü":"U", "ö":"o", "Ö":"O", "ı":"i", "İ":"I"}
    duzeltilmis = []
    for karakter in girdi:
        if karakter in karakter_sozlugu:
            duzeltilmis.append(karakter_sozlugu[karakter])
        else:
            duzeltilmis.append(karakter)
    return "".join(duzeltilmis)

import json

with open('text_iftar_sahur.json', 'r') as f:
    sehir_ilce_iftar_sahur = json.load(f)
with open('sehirler_ilceler_kod.json', 'r') as f:
    sehirler_ilceler_kod = json.load(f)

kısa_sehir_dict = {'maras':'kahramanmaras', 'afyon':'afyonkarahisar', 'ist':'istanbul', 'antep':'gaziantep', 'urfa':'sanliurfa', 'izmit':'kocaeli'}

@bot.on_message(filters.command('ezan'))
async def ezan(bot:Client, message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        sehir = turkce_karakterleri_duzelt(girdi=message.command[1])
        sehir = sehir.lower()
        if sehir in kısa_sehir_dict:
            sehir = kısa_sehir_dict[sehir]
        sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_kod[sehir]}/{sehir}-icin-namaz-vakti"
        r = requests.get(sehir_ezan_link)
        soup = BeautifulSoup(r.text, 'lxml')
        
        tarih_hicri_miladi = soup.find_all('div', attrs={'class':'w3-col s7 tt-takvim'})[0].text.split(' ')
        vakitler = soup.find_all('div', attrs={'class':'today-pray-times'})[0].text.split('\n')
        vakitler = str(vakitler).replace("'', ", "").split(', ')
        
        vakitler = f"""
Miladi: {tarih_hicri_miladi[1]} {tarih_hicri_miladi[2]} {tarih_hicri_miladi[3]}
Hicri: {tarih_hicri_miladi[5][1:]} {tarih_hicri_miladi[6]} {tarih_hicri_miladi[7]}
🕌 {message.command[1].lower().capitalize()} için ezan vakitleri:
📿 {vakitler[0]}: {vakitler[1]}
☀️ {vakitler[2]}: {vakitler[3]}
📿 {vakitler[4]}: {vakitler[5]}
📿 {vakitler[6]}: {vakitler[7]}
📿 {vakitler[8]}: {vakitler[9]}
📿 {vakitler[10]}: {vakitler[11]}
""".replace("'", "").replace('[', '')
        await bot.send_message(chat_id, str(vakitler))  
    except Exception as e:
        print(e)
        await message.reply('🕌 Kullanım şekli: /ezan <code>şehir ismi</code> şeklinde olmalıdır.')
    try:    
        await log_gonder(bot=bot, message=message)
    except:
        pass



import gruplar_db.kullanıcı_sehir_db_code as kullanıcı_sehir
@bot.on_message(filters.command('sahur'))
async def sahur(bot:Client, message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    firstname = str(message.from_user.first_name).replace("'", "")
    suan = datetime.now() + timedelta(hours=3)
    suan = suan.time()
    hour = int(suan.hour)
    minute = int(suan.minute)
    second = int(suan.second)
    
    try:
        if len(message.command) == 2 or len(message.command) == 3:    
            sehir = turkce_karakterleri_duzelt(girdi=message.command[1])
            sehir = sehir.lower()
            texte_yazılacak_yer = message.command[1].lower().capitalize()
            if sehir in kısa_sehir_dict:
                sehir = kısa_sehir_dict[sehir]
            if len(message.command) == 2:
                vakit = sehir_ilce_iftar_sahur[sehir][sehir]['sahur']
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][sehir]}/{sehir}-icin-namaz-vakti"
            elif len(message.command) == 3:
                ilce = turkce_karakterleri_duzelt(girdi=str(message.command[2])).lower()
                vakit = sehir_ilce_iftar_sahur[sehir][ilce]['sahur']
                texte_yazılacak_yer = str(message.command[1]).lower().capitalize() + '-' + str(message.command[2]).lower().capitalize()
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][ilce]}/{ilce}-icin-namaz-vakti"
            kalan_saat = int(vakit[1:3])-hour
            kalan_dakika = int(vakit[4:6])-minute
            if kalan_dakika < 0 or kalan_dakika == 0:
                kalan_saat = kalan_saat - 1
                kalan_dakika = kalan_dakika + 60
            if kalan_saat < 0:
                kalan_saat = kalan_saat + 24
                
            vakit = f"""
🕋 <b>{texte_yazılacak_yer}</b> için sahur vakti: {vakit}

⏱ Sahur vaktine <b>{kalan_saat} saat {kalan_dakika-1} dakika</b> kaldı.

🔗 <a href='{sehir_ezan_link}'>Kontrol için tıklayınız.</a>
""".replace("'", "").replace('[', '')
            if kalan_saat == 0:
                vakit = vakit.replace('0 saat ', '')
                if kalan_dakika < 10:
                    vakit = vakit.replace('dakika', f'dakika {60 - second} saniye')
                    if kalan_dakika == 1:
                        vakit = vakit.replace('0 dakika ', '')
            if kalan_saat == 23 and kalan_dakika == 60:
                await bot.send_audio(chat_id, random.choice(ezanlar), caption=f'{texte_yazılacak_yer} için hayırlı sahurlar 🕌')
            else:
                await message.reply(str(vakit), disable_web_page_preview=True)   ###############################################
            if kullanıcı_sehir.dbde_var_mi(user_id):
                kullanıcı_sehir.db_sil(user_id)
                if len(message.command) == 2:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=message.command[1])
                elif len(message.command) == 3:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=texte_yazılacak_yer)
            else:
                if len(message.command) == 2:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=message.command[1])
                elif len(message.command) == 3:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=texte_yazılacak_yer)
        elif len(message.command) == 1:          
            sehir = ''
            sehir_tr = kullanıcı_sehir.kullanici_sehir_list_dict()[str(user_id)]
            yazılacak_yer = sehir_tr.lower().capitalize()
            if kullanıcı_sehir.dbde_var_mi(user_id):
                if '-' in str(sehir_tr):
                    sehir, ilce = sehir_tr.split('-')
                    yazılacak_yer = sehir.lower().capitalize() + '-' + ilce.lower().capitalize()
                    sehir = turkce_karakterleri_duzelt(girdi=sehir).lower()
                    ilce = turkce_karakterleri_duzelt(girdi=ilce).lower()                    
                elif '-' not in sehir_tr:
                    sehir = turkce_karakterleri_duzelt(girdi=sehir_tr).lower()
            else:
                await message.reply('Daha önce şehir sorgusu yapmamışsınız.')
                return
            if sehir in kısa_sehir_dict:
                sehir = kısa_sehir_dict[sehir]
            if '-' in sehir_tr:
                vakit = sehir_ilce_iftar_sahur[sehir][ilce]['sahur']
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][ilce]}/{ilce}-icin-namaz-vakti"
            elif '-' not in sehir_tr:
                vakit = sehir_ilce_iftar_sahur[sehir][sehir]['sahur']
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][sehir]}/{sehir}-icin-namaz-vakti"
            kalan_saat = int(vakit[1:3])-hour
            kalan_dakika = int(vakit[4:6])-minute
            if kalan_dakika < 0 or kalan_dakika == 0:
                kalan_saat = kalan_saat - 1
                kalan_dakika = kalan_dakika + 60
            if kalan_saat < 0:
                kalan_saat = kalan_saat + 24
                
            vakit = f"""
🕋 <b>{yazılacak_yer}</b> için sahur vakti: {vakit}

⏱ Sahur vaktine <b>{kalan_saat} saat {kalan_dakika-1} dakika</b> kaldı.

🔗 <a href='{sehir_ezan_link}'>Kontrol için tıklayınız.</a>
""".replace("'", "").replace('[', '')
            if kalan_saat == 0:
                vakit = vakit.replace('0 saat ', '')
                if kalan_dakika < 10:
                    vakit = vakit.replace('dakika', f'dakika {60 - second} saniye')
                    if kalan_dakika == 1:
                        vakit = vakit.replace('0 dakika ', '')
            if kalan_saat == 23 and kalan_dakika == 60:
                await bot.send_audio(chat_id, random.choice(ezanlar), caption=f'{yazılacak_yer} için hayırlı sahurlar 🕌')
            else:
                await message.reply(str(vakit), disable_web_page_preview=True)     
    except Exception as e:
        await message.reply(f'🕌 Kullanım şekli: /sahur <code>şehir ismi</code> şeklinde olmalıdır.')
    try:    
        await log_gonder(bot=bot, message=message)
    except:
        pass
denenen_sayı = 0
async def yollama(bot:Client, message:Message, idler):
    global denenen_sayı
    try: 
        sayı = 0
        denenen_sayı = 0
        db_silici = gg.db_sil
        await message.reply(f'Yollama başladı. Tahmini gönderilecek:{str(len(idler))}')
        if 'özelden' in str(message.text):
            db_silici = gk.db_sil
        for i in idler:
            denenen_sayı += 1
            while True:
                try:
                    if 'ilet' in str(message.text).lower():
                        await bot.forward_messages(int(i), message.chat.id, message.reply_to_message_id)
                    else:
                        await bot.copy_message(int(i), message.chat.id, message.reply_to_message_id, reply_markup = message.reply_to_message.reply_markup)
                    sayı += 1
                    with open('yollama_log.txt', 'a', encoding="utf-8") as f:
                        f.write(f'✅{denenen_sayı}|ID:{i}|Başarılı!\n')
                    break
                except errors.FloodWait as e:
                    await asyncio.sleep(e.value)
                except errors.UserIsBlocked as e:
                    with open('yollama_log.txt', 'a', encoding="utf-8") as f:
                        f.write(f'❌{denenen_sayı}ID:{i}|Başarısız ve sildim. Hata:{e}\n')
                    db_silici(id=i)
                    break
                except errors.InputUserDeactivated as e:
                    with open('yollama_log.txt', 'a', encoding="utf-8") as f:
                        f.write(f'❌{denenen_sayı}ID:{i}|Başarısız ve sildim. Hata:{e}\n')
                    db_silici(id=i)
                    break
                except errors.PeerIdInvalid as e:
                    with open('yollama_log.txt', 'a', encoding="utf-8") as f:
                        f.write(f'❌{denenen_sayı}ID:{i}|Başarısız ve sildim. Hata:{e}\n')
                    db_silici(id=i)
                    break
                except errors.ChannelInvalid as e:
                    with open('yollama_log.txt', 'a', encoding="utf-8") as f:
                        f.write(f'❌{denenen_sayı}ID:{i}|Başarısız ve sildim. Hata:{e}\n')
                    db_silici(id=i)
                    break
                except Exception as e:
                    with open('yollama_log.txt', 'a', encoding="utf-8") as f:
                        f.write(f'❌{denenen_sayı}ID:{i}|Başarısız, silmedim. Hata:{e}\n')
                    break
        await bot.send_message(message.chat.id, f'Yollama bitti. Toplam gönderilen:{sayı}')
        await bot.send_document(message.chat.id, 'yollama_log.txt')
        os.remove('yollama_log.txt')
    except Exception as e:
        await message.reply(f"başaramadık knk. genel hata = {e}")

@bot.on_message(filters.command('hduyuru')&admin_filter)
async def yolla(bot:Client, message:Message):
    grup_idler = gg.kategoriye_göre_veri_listesi()
    kullanıcı_idler = gk.kategoriye_göre_veri_listesi()
    if 'deneme' in str(message.text).lower():
        await yollama(bot=bot, message=message, idler=[admin_grup])
    elif 'özelden' in str(message.text).lower():
        await yollama(bot=bot, message=message, idler=kullanıcı_idler)
    else:
        await yollama(bot=bot, message=message, idler=gg.kategoriye_göre_veri_listesi())

async def idurum(bot, message, idler):
    try:
        global denenen_sayı
        await message.reply(f"gönderi durumu:{denenen_sayı}/{len(idler)} kalan:{len(idler)-denenen_sayı}")
    except Exception as e:
        await message.reply(f"{e}")

@bot.on_message(filters.command('hdurum')&admin_filter)
async def durum(bot, message):
    await idurum(bot=bot, message=message, idler=gk.kategoriye_göre_veri_listesi())

@bot.on_message(filters.audio & admin_filter & filters.private)
async def audio(bot, message):
    await message.reply(message.audio.file_id)



#@bot.on_message(filters.command('ezanat')&admin_filter)
#async def ezanat(bot, message):
#    chat_id = message.chat.id
#    try:
#        await bot.send_audio(chat_id, 'CQACAgIAAxkBAAEBIS9kLOJo42g6i1u5Fdc5qnasQ8PR3QACQAUAAlk0gUjdAAEwcRhRuGYeBA', caption='OKUNUYOR🕌')
#    except Exception as e:
#        await message.reply(str(e))

@bot.on_message(filters.command('iftar'))
async def iftar(bot:Client, message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    firstname = str(message.from_user.first_name).replace("'", "")
    suan = datetime.now() + timedelta(hours=3)
    suan = suan.time()
    hour = int(suan.hour)
    minute = int(suan.minute)
    second = int(suan.second)
    try:
        if len(message.command) == 2 or len(message.command) == 3:   
            sehir = turkce_karakterleri_duzelt(girdi=message.command[1])
            sehir = sehir.lower()
            texte_yazılacak_yer = message.command[1].lower().capitalize()
            if sehir in kısa_sehir_dict:
                sehir = kısa_sehir_dict[sehir]
            if len(message.command) == 2:
                vakit = sehir_ilce_iftar_sahur[sehir][sehir]['iftar']
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][sehir]}/{sehir}-icin-namaz-vakti"
            elif len(message.command) == 3:
                ilce = turkce_karakterleri_duzelt(girdi=str(message.command[2])).lower()
                vakit = sehir_ilce_iftar_sahur[sehir][ilce]['iftar']
                texte_yazılacak_yer = str(message.command[1]).lower().capitalize() + '-' + str(message.command[2]).lower().capitalize()
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][ilce]}/{ilce}-icin-namaz-vakti"
            kalan_saat = int(vakit[1:3])-hour
            kalan_dakika = int(vakit[4:6])-minute
            if kalan_dakika < 0 or kalan_dakika == 0:
                kalan_saat = kalan_saat - 1
                kalan_dakika = kalan_dakika + 60
            if kalan_saat < 0:
                kalan_saat = kalan_saat + 24
            
            vakit = f"""
🕋 <b>{texte_yazılacak_yer}</b> için iftar vakti: {vakit}

⏱ İftar vaktine <b>{kalan_saat} saat {kalan_dakika-1} dakika</b> kaldı.

🔗 <a href='{sehir_ezan_link}'>Kontrol için tıklayınız.</a>
""".replace("'", "").replace('[', '')
            if kalan_saat == 0:
                vakit = vakit.replace('0 saat ', '')
                if kalan_dakika < 10:
                    vakit = vakit.replace('dakika', f'dakika {60 - second} saniye')
                    if kalan_dakika == 1:
                        vakit = vakit.replace('0 dakika ', '')
            if kalan_saat == 23 and kalan_dakika == 60:
                await bot.send_audio(chat_id, random.choice(ezanlar), caption=f'{texte_yazılacak_yer} için hayırlı iftarlar 🕌')
            else:
                await message.reply(str(vakit), disable_web_page_preview=True)
            if kullanıcı_sehir.dbde_var_mi(user_id):
                kullanıcı_sehir.db_sil(user_id)
                if len(message.command) == 2:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=message.command[1])
                elif len(message.command) == 3:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=texte_yazılacak_yer)
            else:
                if len(message.command) == 2:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=message.command[1])
                elif len(message.command) == 3:
                    kullanıcı_sehir.db_yazici(id=user_id, sehir=texte_yazılacak_yer)
        elif len(message.command) == 1:   ########################################
            sehir = ''
            sehir_tr = kullanıcı_sehir.kullanici_sehir_list_dict()[str(user_id)]
            yazılacak_yer = sehir_tr.lower().capitalize()
            if kullanıcı_sehir.dbde_var_mi(user_id):
                if '-' in sehir_tr:
                    sehir, ilce = sehir_tr.split('-')
                    yazılacak_yer = sehir.lower().capitalize() + '-' + ilce.lower().capitalize()
                    sehir = turkce_karakterleri_duzelt(girdi=sehir).lower()
                    ilce = turkce_karakterleri_duzelt(girdi=ilce).lower()
                elif '-' not in sehir_tr:
                    sehir = turkce_karakterleri_duzelt(girdi=sehir_tr).lower()
            else:
                await message.reply('Daha önce şehir sorgusu yapmamışsınız.')
                return
            
            if sehir in kısa_sehir_dict:
                sehir = kısa_sehir_dict[sehir]
            if '-' in sehir_tr:
                vakit = sehir_ilce_iftar_sahur[sehir][ilce]['iftar']
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][ilce]}/{ilce}-icin-namaz-vakti"
            elif '-' not in sehir_tr:
                vakit = sehir_ilce_iftar_sahur[sehir][sehir]['iftar']
                sehir_ezan_link = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{sehirler_ilceler_kod[sehir][sehir]}/{sehir}-icin-namaz-vakti"
            kalan_saat = int(vakit[1:3])-hour
            kalan_dakika = int(vakit[4:6])-minute
            
            if kalan_dakika < 0 or kalan_dakika == 0:
                kalan_saat = kalan_saat - 1
                kalan_dakika = kalan_dakika + 60
            if kalan_saat < 0:
                kalan_saat = kalan_saat + 24
                
            vakit = f"""
🕋 <b>{yazılacak_yer}</b> için iftar vakti: {vakit}

⏱ İftar vaktine <b>{kalan_saat} saat {kalan_dakika-1} dakika</b> kaldı.

🔗 <a href='{sehir_ezan_link}'>Kontrol için tıklayınız.</a>
""".replace("'", "").replace('[', '')
            if kalan_saat == 0:
                vakit = vakit.replace('0 saat ', '')
                if kalan_dakika < 10:
                    vakit = vakit.replace('dakika', f'dakika {60 - second} saniye')
                    if kalan_dakika == 1:
                        vakit = vakit.replace('0 dakika ', '')
            if kalan_saat == 23 and kalan_dakika == 60:
                await bot.send_audio(chat_id, random.choice(ezanlar), caption=f'{yazılacak_yer} için hayırlı iftarlar 🕌')
            else:
                await message.reply(str(vakit), disable_web_page_preview=True)
    except Exception as e:
        await message.reply('🕌 Kullanım şekli: /iftar <code>şehir ismi</code> şeklinde olmalıdır.')
    try:    
        await log_gonder(bot=bot, message=message)
    except:
        pass

@bot.on_callback_query()
async def butonlar(bot:Client, CallbackQuery):
    data = CallbackQuery.data
    chat_id = CallbackQuery.message.chat.id
    callback_id = CallbackQuery.id
    baslangicfoto = 'AgACAgQAAxkBAAIDIGQVxieRjoxa_fBtviiVKDeyPpMYAALcvTEbklqwUFPA11UyEtNAAAgBAAMCAAN4AAceBA'
    buton = [[InlineKeyboardButton('KOMUTLAR', 'komutlar')], [InlineKeyboardButton('NAMAZ SURELERİ', 'namaz_sureleri_baslat')]] #, [InlineKeyboardButton('GENEL BİLGİ', 'genel_bilgi')]
    if data == 'start':
        await bot.edit_message_caption(chat_id=chat_id,
                                       message_id=CallbackQuery.message.id,
                                       caption="Esselamu aleykum ve rahmetullahi ve berekatuhu ve magfiratuhu ebeden ve daimen.(Rabbimin selamı,rahmeti,bereketi ve mağfireti daimi ve ebedi olarak sizin üstünüze olsun)",
                                       reply_markup=InlineKeyboardMarkup(buton))
    elif data == 'komutlar':
        await bot.edit_message_caption(chat_id=chat_id, 
                                       message_id=CallbackQuery.message.id, 
                                       caption=f"""
/ayet: Kuran-ı Kerim'den ayetler atar.
/ezan <code>şehir ismi</code>: Ezan vaktini söyler.
/sahur <code>şehir ismi</code>: Sahur vaktini söyler.
/iftar <code>şehir ismi</code>: İftar vaktini söyler.
/sure: namaz surelerini atar.
        """, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅️', 'start')]]))
    elif data.startswith('namaz_sureleri'):
        if data.startswith('namaz_sureleri_baslat'):
            msg = await bot.send_photo(chat_id=chat_id,
                photo='photo_2023-03-18_17-09-44.jpg', 
                reply_markup=InlineKeyboardMarkup(cokla(buton_yap(sureler, bas='namaz_sureleri_sureler'))))
#            await CallbackQuery.edit_message_caption(chat_id=chat_id,
#                                           message_id = CallbackQuery.message.id,
#                                           caption='Sure seçiniz.')
        elif data.startswith('namaz_sureleri_sureler'):
            data = data.replace('namaz_sureleri_sureler', '')
            await CallbackQuery.edit_message_media( 
                                         media=InputMediaPhoto(sureler[data]), 
                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅️', 'namaz_sureleri_edit')]]))
        elif data.startswith('namaz_sureleri_edit'):
            await CallbackQuery.edit_message_media(
                media=InputMediaPhoto('photo_2023-03-18_17-09-44.jpg'),
                reply_markup=InlineKeyboardMarkup(cokla(buton_yap(sureler, bas='namaz_sureleri_sureler')))
            )
    elif data == 'genel_bilgi':
        pass

@bot.on_message(filters.command('sure'))
async def sure(bot:Client, message:Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    try:
        await bot.send_photo(chat_id=chat_id,
        photo='photo_2023-03-18_17-09-44.jpg', 
        reply_markup=InlineKeyboardMarkup(cokla(buton_yap(sureler, bas='namaz_sureleri_sureler'))))
    except errors.Forbidden as e:
        await message.reply('Lütfen medya göndermeme izin veriniz')
    try:    
        await log_gonder(bot=bot, message=message)
    except:
        pass
    
    
@bot.on_message(filters.photo & filters.private)
async def photo(bot:Client, message:Message):
    chat_id = message.chat.id
    photo_id = message.photo.file_id
    await bot.send_message(chat_id, f"<code>{photo_id}</code>")



async def ayet_gonderici():
    await bot.start()
    chat_id = gg.kategoriye_göre_veri_listesi()
    
    while True:
        ayet_saatler = ['20:00', '00:00', '04:00', '08:00', '12:00', '16:00', '13:16']
        camii_saatler = ['20:05:00', '00:05:00', '04:05:00', '08:05:00', '12:05:00', '16:05:00']
        now = datetime.now() + timedelta(hours=3)
        now = str(now.time())[0:8]
        uzatma_süresi = 60 #0.999
        if now[0:5] in ayet_saatler:
            await bot.send_message(bot_owner, 'aaa')
            try:
                random_sayı = random.randint(0, 112)
                ayet = random.choice(veri_tabanindan_getirme(kolon='ayetler', istenilenveri=random_sayı).replace("'", "").replace(r'\n', '\n').replace(r'\r', '').split('***'))
                if len(str(ayet)) < 100:
                    continue
                for i in chat_id:
                    while True:
                        try:
                            await bot.send_message(i, str(ayet))
                        except errors.FloodWait as e:
                            await asyncio.sleep(e.value+1)
                        
                        except errors.PeerIdInvalid as e:
                            with open('ayet_gonderici_log.txt', 'a', encoding="utf-8") as f:
                                f.write(f'❌ID:{i}|Başarısız ve sildim. Hata:{e}\n')
                            gg.db_sil(chat_id=i)
                            break
                        except errors.ChannelInvalid as e:
                            with open('ayet_gonderici_log.txt', 'a', encoding="utf-8") as f:
                                f.write(f'❌ID:{i}|Başarısız ve sildim. Hata:{e}\n')
                            gg.db_sil(chat_id=i)
                            break
                        except Exception as e:
                            with open('ayet_gonderici_log.txt', 'a', encoding="utf-8") as f:
                                f.write(f'❌ID:{i}|Başarısız, silmedim. Hata:{e}\n')
                            break
#            if now in camii_saatler:
#                camii_photo = random.choice(['AgACAgQAAxkBAAIFFGQYEsNrO6yVpM5f3GywrSv9ZyoIAAKwrzEbtqLFUPpxrL_rL40cAAgBAAMCAAN3AAceBA',
#                                             'AgACAgQAAxkBAAIFGGQYEsOXevxy2Jr7Lfz_ArUrf-2xAAJQsDEbRJ7FUG2gNqX5s5hxAAgBAAMCAAN3AAceBA',
#                                             'AgACAgQAAxkBAAIFFWQYEsN0lVVVmKJMu1FCldB3UpFRAALjrzEbbTjFUHQ0-F51EyERAAgBAAMCAAN3AAceBA',
#                                             'AgACAgQAAxkBAAIFF2QYEsO219sQz8RefWHo4yRO1f3EAALKrzEb8yvEUDKA5nDk5mgkAAgBAAMCAAN3AAceBA',
#                                             'AgACAgQAAxkBAAIFFmQYEsNwZdkbJ3Y2z3ODYNdgFW8jAAJ_rzEbVtrEUJveYnWO6_JnAAgBAAMCAAN3AAceBA',
#                                             'AgACAgQAAxkBAAIFHmQYEyXiGDiltNmaOUEvDd0Bger5AAL8rzEbYNDEUFEeg68J88fNAAgBAAMCAAN3AAceBA',
#                                             'AgACAgQAAxkBAAIFH2QYEyV0yPlifKvCbJ_IVN0KqjETAALtrzEbfJ3EUAAB0v0xYARYUQAIAQADAgADdwAHHgQ'])
#                for i in chat_id:
#                    try:
#                        await bot.send_photo(i, camii_photo)
#                    except errors.ChatForbidden:
#                        continue
#                    except errors.PeerIdInvalid:
#                        continue
#                    except errors.ChannelInvalid:
#                        continue

            except errors.MessageEmpty as e:
                await bot.send_message(log_grup, f"message empty hatası ama atlanıyor...")
                uzatma_süresi = 0.48
                continue
            except Exception as e:
                await bot.send_message(log_grup, f"tanımsız hata. 4 saatte bir ayet {e}")
                continue
        if now[0:5] == '00:11':
            await bot.send_message(admin_grup, 'vakitler yenileniyor')
            await asyncio.create_subprocess_shell('sudo python3 /iftar-sahur-ayet-bot/test.py')
            await bot.send_message(admin_grup, 'vakitler yenilendi')
        await bot.send_document(admin_grup, 'ayet_gonderici_log.txt')
        os.remove('ayet_gonderici_log.txt')
        await asyncio.sleep(uzatma_süresi)

#asyncio.run(ayet_gonderici())

@bot.on_message(filters.command('gruplar') & filters.private & admin_filter)
async def gruplar(bot:Client, message):
    await bot.send_message(bot_owner, str(gg.kategoriye_göre_veri_listesi()))


import gruplar_db.gruplar_db_code as gg
@bot.on_chat_member_updated()
async def new_chat(bot, message):
    chat_id = message.chat.id 
    chat_title = message.chat.title
    grup_username = message.chat.username
    grup_idler = gg.kategoriye_göre_veri_listesi()
    if gg.dbde_var_mi(chat_id=chat_id):
        return
    else:
        gg.db_yazici(chat_id=chat_id, title=chat_title)
        link = ""
        if grup_username != None:
            link = f"t.me/{grup_username}"
        await bot.send_message(log_grup, f"👥 <a href='{link}'>{chat_title}</a> (<code>{chat_id}</code>) ⟶ {len(grup_idler)}", disable_web_page_preview=True)


import os

async def reset_at(hard_reset = False):
    try:
        bot.terminate()
    except Exception as e:
        print('hata')
        asyncio.ensure_future(bot.stop())
        with open("tambunoktadahatavarpanpaaaa.txt", "w") as wwww:
            wwww.write(str(e))
    await asyncio.sleep(.5)
    
    if not hard_reset:
        os.system('sudo nohup python3 mainayet.py &')
    await asyncio.sleep(.5)

    if hard_reset:
        os.system('sudo bash /etc/rc.local')
    os.kill(os.getpid(), 9)


@bot.on_message(filters.command('res') & filters.private & admin_filter)
async def resres(bot:Client, message:Message):
    text = ''
    text = message.text.replace('/res ', '')
    if text == 'hard':
        await message.reply('hard reset atılıyor...')
        await reset_at(hard_reset=True)
    else:
        await message.reply('reset atılıyor...')
        await reset_at()


@bot.on_message(filters.command('totaluser') & admin_filter)
async def totaluser(bot:Client, message:Message):
    chat_id = message.chat.id
    gruplar_sayı = str(len(gg.kategoriye_göre_veri_listesi()))
    kullanici_sayisi = str(len(gk.kategoriye_göre_veri_listesi()))
    await bot.send_message(chat_id, f"gruplar: {gruplar_sayı}, kullanıcılar: {kullanici_sayisi}")


# TODO: log'a bot başlatıldı mesajı atsın

print('bot run')
bot.run()
#if __name__ == '__main__':
#    bot.run(ayet_gonderici())


