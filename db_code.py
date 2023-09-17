import sqlite3

con = sqlite3.connect('kuran_sureler_ayetler.db')

cur = con.cursor()
try:
    cur.execute('CREATE TABLE kuran(sure, ayetler)')
except:
    pass



def db_yaz(sure, ayetler):
    cur.execute(f"INSERT INTO kuran VALUES('{sure}', '{ayetler}')")
    con.commit()
def veri_tabanindan_getirme(kolon, istenilenveri):
    res = cur.execute(f'SELECT {kolon} FROM kuran')
    veri = str(res.fetchall()[istenilenveri]).replace(',)', '').replace('(', '')
    return veri

#for i in veri_tabanindan_getirme(kolon='ayetler',istenilenveri=0).replace("'", "").split('***'):
#    print(i)

#res = cur.execute(f"SELECT sure FROM kuran")
#
#veri = res.fetchall()
#
#sureler_dict = {}
#for i in enumerate(veri):
#    dict_elemanlar = {i[0]:i[1][0]}
#    sureler_dict.update(dict_elemanlar)
#    print(f"'{i[0]}':'{i[1][0]}'")
#print(sureler_dict)
