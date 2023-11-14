import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask,render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>朱芷伶Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>朱芷伶簡介網頁</a><br>"
    homepage += "<a href=/account>網頁表單輸入帳密傳值</a><br>"
    homepage += "<br><a href=/read>人選之人演員查詢</a><br>"
    homepage += "<br><a href=/book>精選圖書列表</a><br>"

    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    now = datetime.now()
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/read")
def read():
    Result = ""
    collection_ref = db.collection("人選之人-造浪者")
    docs = collection_ref.order_by("birth", direction=firestore.Query.DESCENDING).get()
    for doc in docs: 
        x = doc.to_dict()
        Result += "演員：{},劇中角色是{},出生於{}".format(x["name"],x["role"],x["birth"]) + "<br>"
    return Result

@app.route("/book")
def book():
    Result = ""
    db = firestore.client()
    collection_ref = db.collection("圖書精選")
    docs = collection_ref.get()
    for doc in docs: 
        bk = doc.to_dict()
        Result += "書名：" + bk["title"] + "<br>"
        Result += "作者：" + bk["aauthor"] + "<br>"
        Result += str(bk["anniversary"]) + "週年紀念版<br>"
        Result += "<img src=" + bk["cover"] +" ></img><br><br>"

    return Result

#if __name__ == "main":
 #   app.run(debug=True)


