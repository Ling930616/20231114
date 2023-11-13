from flask import Flask, render_template, request
from datetime import datetime,timezone,timedelta
app = Flask(__name__)



@app.route("/")
def index():
    homepage = "<h1>朱芷伶個人網頁</h1>"
    homepage += "<a href=/home>首頁</a><br>"
    homepage += "<a href=/TearsofThemis>何倫碼</a><br>"
    homepage += "<a href=/HonKaiStarRail>自傳履歷</a><br>"
    homepage += "<a href=/HonkaiImpact3>公司</a><br>"

    return homepage


@app.route("/home")
def home():
    now = datetime.now()
    return render_template("home.html")

@app.route("/TearsofThemis")
def TearsofThemis():
    now = datetime.now()
    return render_template("TearsofThemis.html") 

@app.route("/HonKaiStarRail")
def HonKaiStarRail():
    now = datetime.now()
    return render_template("HonKaiStarRail.html") 

@app.route("/HonkaiImpact3")
def HonkaiImpact3():
    now = datetime.now()
    return render_template("HonkaiImpact3.html") 



#if __name__ == "__main__":
#  app.run()

