from flask import Flask, request
import urllib.request
app = Flask(__name__)
@app.route("/")
def index():
    return '<h1>URL Preview</h1><p>Ejemplo: /fetch?url=http://example.com</p>'
@app.route("/admin")
def admin():
    if request.remote_addr in ("127.0.0.1","::1"):
        return open("/flag.txt").read()
    return "403: este panel solo es accesible desde localhost"
@app.route("/fetch")
def fetch():
    u = request.args.get("url","")
    try:
        return "<pre>"+urllib.request.urlopen(u, timeout=5).read().decode(errors="replace")+"</pre>"
    except Exception as e:
        return str(e)
app.run(host="0.0.0.0", port=5000, threaded=True)
