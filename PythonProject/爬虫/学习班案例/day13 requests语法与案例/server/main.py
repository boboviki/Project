from flask import Flask, request, render_template, make_response
import json
import uuid

app = Flask(__name__, template_folder="temps")

COOKIEID = "8EA6EC79097240F2B4DC58D45A0EC12E"


# 获取登录页面
@app.route("/login")
def login():
    return render_template("login.html")


# 登录认证
@app.route("/auth", methods=['POST'])
def auth():
    # 用户名密码验证
    user = request.form.get("user")
    pwd = request.form.get("pwd")

    if user == "yuan" and pwd == "123":

        resp = make_response("success！")
        # 写cookie
        resp.set_cookie("login_id", COOKIEID)

        return resp
    else:
        return "fail!"


@app.route("/")
def index():
    # cookie验证
    login_id = request.cookies.get("login_id")
    if login_id == COOKIEID:
        return render_template("index.html")
    else:
        return "请登录！"


@app.route("/books")
def books():
    # cookie验证
    login_id = request.cookies.get("login_id")
    if login_id == COOKIEID:
        data = json.dumps(["西游记", "三国演义", "水浒传", "金瓶梅"], ensure_ascii=False)
        return data
    else:
        return "请登录！"


app.run()  # 默认端口号
