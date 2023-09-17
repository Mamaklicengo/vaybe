import sqlite3

con = sqlite3.connect("gruplar_db/kullanıcılar.db")

cur = con.cursor()
try:
    cur.execute("CREATE TABLE kullanıcılar(id, firstname, username)")
except:
    pass

def dbde_var_mi(id):
    res = cur.execute('SELECT id FROM kullanıcılar')
    veri = str(res.fetchall()).replace(',)', '').replace('(', '')
    değer = str(id) in veri
    return değer

def db_yazici(id, firstname, username):
    cur.execute(f"INSERT INTO kullanıcılar VALUES('{id}', '{firstname}', '{username}')")
    con.commit()

def kategoriye_göre_veri_listesi():
    res = cur.execute('SELECT id FROM kullanıcılar')
    l = []
    for i in res:
        l.append(str(i).replace('(', '').replace(',)', '').replace("'", ""))
    return l

def db_sil(id):
    cur.execute(f"DELETE FROM kullanıcılar WHERE id='{id}'")
    con.commit()