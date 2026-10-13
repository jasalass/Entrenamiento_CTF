from flask import Flask, request
app = Flask(__name__)
NOTES = {0: open("/flag.txt").read().strip(), 1: "Tu nota privada: comprar leche."}
@app.route("/")
def index():
    return '<h1>Mis Notas</h1><p>Tu nota: <a href="/note?id=1">/note?id=1</a></p>'
@app.route("/note")
def note():
    try: i = int(request.args.get("id","1"))
    except Exception: i = 1
    return "<pre>"+str(NOTES.get(i,"no existe"))+"</pre>"
app.run(host="0.0.0.0", port=5000)
