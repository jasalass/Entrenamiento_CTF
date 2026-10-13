from flask import Flask, request, make_response
import base64, json, hmac, hashlib
app = Flask(__name__); SECRET = b"no-lo-adivinaras"
def b64u(b): return base64.urlsafe_b64encode(b).decode().rstrip("=")
def ub64u(s): return base64.urlsafe_b64decode(s + "="*(-len(s) % 4))
def make(payload):
    h = b64u(b'{"alg":"HS256","typ":"JWT"}'); p = b64u(json.dumps(payload).encode())
    sig = b64u(hmac.new(SECRET, (h+"."+p).encode(), hashlib.sha256).digest())
    return h+"."+p+"."+sig
def verify(tok):
    h, p, s = tok.split(".")
    alg = json.loads(ub64u(h)).get("alg")
    if alg == "none":   # VULNERABILIDAD: acepta tokens sin firma
        return json.loads(ub64u(p))
    if alg == "HS256":
        exp = b64u(hmac.new(SECRET, (h+"."+p).encode(), hashlib.sha256).digest())
        if hmac.compare_digest(exp, s): return json.loads(ub64u(p))
    return None
@app.route("/")
def index():
    r = make_response('<h1>App</h1><p>Tienes un token de invitado. Visita <a href="/panel">/panel</a>.</p>')
    r.set_cookie("token", make({"user":"guest"})); return r
@app.route("/panel")
def panel():
    t = request.cookies.get("token","")
    try: data = verify(t)
    except Exception: data = None
    if data and data.get("user") == "admin":
        return "<pre>"+open("/flag.txt").read()+"</pre>"
    return "<p>Usuario: "+str(data)+". Necesitas ser admin.</p>"
app.run(host="0.0.0.0", port=5000)
