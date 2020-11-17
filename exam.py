from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import config
from api_blue import blue_bp

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#注册蓝图
app.register_blueprint(blue_bp)
db.init_app(app)

#用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))

@app.route('/')
def hello_world():
    u1 = User(username = "哇咔咔",email = "871105356@qq.com")
    u2 = User(username = "哒哒",email = "110@qq.com")
    db.session.add_all([u1,u2])
    db.session.commit()
    return render_template("index.html")

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True,port=9999)
