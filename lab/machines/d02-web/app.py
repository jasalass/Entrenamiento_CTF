from flask import Flask, request, make_response
import base64
app = Flask(__name__)
@app.route("/")
def index():
    r = make_response('<h1>Portal</h1><p>Sesion de invitado creada. Visita <a href="/panel">/panel</a>.</p>')
    r.set_cookie("auth", base64.b64encode(b"user").decode())
    return r
@app.route("/panel")
def panel():
    c = request.cookies.get("auth","")
    try:
        role = base64.b64decode(c).decode()
    except Exception:
        role = ""
    if role == "admin":
        return "<pre>"+open("/flag.txt").read()+"</pre>"
    return "<p>Rol actual: "+role+". Solo 'admin' puede ver el flag.</p>"
app.run(host="0.0.0.0", port=5000)
