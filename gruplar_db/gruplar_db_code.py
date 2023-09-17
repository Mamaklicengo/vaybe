import sqlite3

con = sqlite3.connect("gruplar_db/gruplar.db")

cur = con.cursor()
try:
    cur.execute("CREATE TABLE gruplar(chat_id, title)")
except:
    pass

def dbde_var_mi(chat_id):
    res = cur.execute('SELECT chat_id FROM gruplar')
    veri = str(res.fetchall()).replace(',)', '').replace('(', '')
    değer = str(chat_id) in veri
    return değer

def db_yazici(chat_id, title):
    cur.execute(f"INSERT INTO gruplar VALUES('{chat_id}', '{title}')")
    con.commit()

def kategoriye_göre_veri_listesi():
    res = cur.execute('SELECT chat_id FROM gruplar')
    l = []
    for i in res:
        l.append(str(i).replace('(', '').replace(',)', '').replace("'", ""))
    return l

def db_sil(id):
    cur.execute(f"DELETE FROM gruplar WHERE chat_id='{id}'")
    con.commit()