from flask import Flask, request
from lxml import etree
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        try:
            p = etree.XMLParser(resolve_entities=True, no_network=True)
            doc = etree.fromstring(request.data, p)
            return "<pre>"+etree.tostring(doc).decode(errors="replace")+"</pre>"
        except Exception as e:
            return str(e)
    return '<h1>API XML</h1><p>Envia tu XML con POST al / (Content-Type: application/xml).</p>'
app.run(host="0.0.0.0", port=5000)
