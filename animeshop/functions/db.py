import sqlite3

def getdb():
    return sqlite3.connect('db.sqlite3')

def getCategories(footer=False):
    db = getdb()
    cur =  db.cursor()
    cur.execute('SELECT * FROM categories')
    tr= ''
    r = cur.fetchall()
    for cat in r:
        if not footer:
            tr+=f'<li><a class="dropdown-item" href="/c/{cat[0]}">{cat[1]}</a></li>'
        else:
            tr+=f'<li class="nav-item "><a class="nav-link px-2 text-white" href="/c/{cat[0]}">{cat[1]}</a></li>' 
    return tr

def getCategoriesFooter():
    return getCategories(True)

def getItem(i):
    db = getdb()
    cur =  db.cursor()
    cur.execute('SELECT * FROM items where item = ?', [i])
    tr= ''
    r = cur.fetchone()
    return r 

def getCard(i):
    db = getdb()
    cur =  db.cursor()
    cur.execute('SELECT * FROM membership_cards where card = ?', [i])
    tr= ''
    r = cur.fetchone()
    return r 

def getItems(c):
    db = getdb()
    cur =  db.cursor()
    cur.execute('SELECT * FROM items where category = ?', [c])
    tr= ''
    r = cur.fetchall()
    return r

def getItemsAll():
    db = getdb()
    cur =  db.cursor()
    cur.execute('SELECT * FROM items')
    tr= ''
    r = cur.fetchall()
    return r

def getCategory(cid):
    db = getdb()
    cur =  db.cursor()
    cur.execute('SELECT * FROM categories WHERE id = ?', [cid])
    tr= ''
    r = cur.fetchall()
    return r[0] if len(r)!=0 else None