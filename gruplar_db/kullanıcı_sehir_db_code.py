import sqlite3

con = sqlite3.connect("gruplar_db/kullanici_sehir.db")

cur = con.cursor()
try:
    cur.execute("CREATE TABLE kullanici_sehir(id, sehir)")
except:
    pass

def dbde_var_mi(id):
    res = cur.execute('SELECT id FROM kullanici_sehir')
    veri = str(res.fetchall()).replace(',)', '').replace('(', '')
    değer = str(id) in veri
    return değer

def db_yazici(id, sehir):
    cur.execute(f"INSERT INTO kullanici_sehir VALUES('{id}', '{sehir}')")
    con.commit()

def kategoriye_göre_veri_listesi():
    res = cur.execute('SELECT id FROM kullanici_sehir')
    l = []
    for i in res:
        l.append(str(i).replace('(', '').replace(',)', '').replace("'", ""))
    return l

def db_sil(id):
    cur.execute(f"DELETE FROM kullanici_sehir WHERE id='{id}'")
    con.commit()

def kullanici_sehir_list():
    res = cur.execute('SELECT id, sehir FROM kullanici_sehir')
    l = []
    for i in res:
        l.append(i)
    return l

def kullanici_sehir_list_dict():
    liste = kullanici_sehir_list()
    d = {}
    sayi = 0
    for i in range(len(liste)):
        eleman = liste[sayi]
        ilk_eleman = eleman[0]
        ikinci_eleman = eleman[1]
        dict_elemanlar = {ilk_eleman:ikinci_eleman}
        d.update(dict_elemanlar)
        sayi += 1
    return d