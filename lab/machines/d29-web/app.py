from flask import Flask, request, render_template_string
app = Flask(__name__)
app.config["FLAG"] = open("/flag.txt").read().strip()
@app.route("/")
def index():
    name = request.args.get("name","mundo")
    return render_template_string('<h1>Hola '+name+'</h1><p>Usa ?name= para saludar.</p>')
app.run(host="0.0.0.0", port=5000)
