from flask import Flask, render_template
import json

app = Flask(__name__, template_folder="temps")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books():
    import time
    time.sleep(5)
    return json.dumps(["西游记", "三国演义", "水浒传", "金瓶梅"], ensure_ascii=False)


@app.route("/books2")
def books2():
    return json.dumps(["西游记2", "三国演义2", "水浒传2", "金瓶梅2"], ensure_ascii=False)


app.run()  # 默认端口号
