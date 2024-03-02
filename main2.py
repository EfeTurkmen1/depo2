from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def hello_world():
    return f'<h1>Merhaba, websitemize hosgelediniz! efe sayfasina gitmek icin <a href="/efe"> buraya </a> tilayabilirsiniz.</h1>'

@app.route("/efe")
def efe():
    return "<h1> Merhaba benim ismim efe </h1>"

app.run(debug=True)
