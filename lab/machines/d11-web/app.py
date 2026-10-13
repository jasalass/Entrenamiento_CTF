from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.route("/")
def index():
    return '<h1>Gateway</h1><form action="/ping"><input name="host" value="127.0.0.1"><button>ping</button></form><!-- TODO(dev): /ping pasa host a la shell sin sanitizar -->'
@app.route("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /ping\nDisallow: /internal/\n", 200, {"Content-Type":"text/plain"}
@app.route("/internal/")
def internal():
    return "<pre>/ping ejecuta 'ping -c1 <host>' en la shell. Pendiente sanitizar el parametro host.</pre>"
@app.route("/ping")
def ping():
    host = request.args.get("host","")
    try:
        out = subprocess.check_output("ping -c1 "+host, shell=True, stderr=subprocess.STDOUT, timeout=8)
        b = out.decode(errors="replace")
    except subprocess.CalledProcessError as e:
        b = e.output.decode(errors="replace")
    except Exception as e:
        b = str(e)
    return "<pre>"+b+"</pre>"
app.run(host="0.0.0.0", port=5000)
