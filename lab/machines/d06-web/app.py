from flask import Flask, request
import sqlite3
app = Flask(__name__)
DB = "/tmp/app.db"
def init():
    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE IF NOT EXISTS users(user TEXT, pass TEXT, note TEXT)")
    if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        flag = open("/flag.txt").read().strip()
        db.execute("INSERT INTO users VALUES('admin','s3cr3t',?)", (flag,))
        db.execute("INSERT INTO users VALUES('guest','guest','sin permisos')")
        db.commit()
    db.close()
@app.route("/", methods=["GET","POST"])
def login():
    out = ""
    if request.method == "POST":
        u = request.form.get("user",""); p = request.form.get("pass","")
        db = sqlite3.connect(DB)
        q = "SELECT user,note FROM users WHERE user='%s' AND pass='%s'" % (u, p)
        try:
            rows = db.execute(q).fetchall()
            out = "<pre>"+"\n".join(str(r) for r in rows)+"</pre>" if rows else "login incorrecto"
        except Exception as e:
            out = "error SQL: "+str(e)
        db.close()
    return '<h1>Login</h1><form method="post">user <input name="user"> pass <input name="pass" type="password"><button>entrar</button></form>'+out
init()
app.run(host="0.0.0.0", port=5000)
