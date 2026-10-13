from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def index():
    return '<h1>Descargas</h1><p>Ejemplo: <a href="/download?file=manual.txt">/download?file=manual.txt</a></p>'
@app.route("/download")
def download():
    f = request.args.get("file","manual.txt")
    try:
        return "<pre>"+open("/srv/files/"+f).read()+"</pre>"
    except Exception as e:
        return str(e)
app.run(host="0.0.0.0", port=5000)
