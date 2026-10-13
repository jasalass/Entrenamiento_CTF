from flask import Flask, request
import sqlite3
app = Flask(__name__); DB = "/tmp/shop.db"
def init():
    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER, name TEXT)")
    db.execute("CREATE TABLE IF NOT EXISTS secret(id INTEGER, flag TEXT)")
    if db.execute("SELECT COUNT(*) FROM items").fetchone()[0] == 0:
        db.execute("INSERT INTO items VALUES(1,'manzana')"); db.execute("INSERT INTO items VALUES(2,'pera')")
        db.execute("INSERT INTO secret VALUES(1,?)", (open("/flag.txt").read().strip(),)); db.commit()
    db.close()
@app.route("/")
def index():
    return '<h1>Tienda</h1><p>Ver producto: <a href="/item?id=1">/item?id=1</a></p>'
@app.route("/item")
def item():
    i = request.args.get("id","1")
    db = sqlite3.connect(DB); q = "SELECT id,name FROM items WHERE id="+i
    try:
        rows = db.execute(q).fetchall(); out = "<pre>"+"\n".join(str(r) for r in rows)+"</pre>"
    except Exception as e:
        out = "error SQL: "+str(e)
    db.close(); return out
init(); app.run(host="0.0.0.0", port=5000)
