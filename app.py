from datetime import datetime
from flask_migrate import Migrate
import pytz
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'your_secret_key'  # セッション管理のためのキー

Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15))
    content = db.Column(db.String(500))
    created_at =  db.Column(db.DateTime, default=datetime.now(pytz.timezone("Asia/Tokyo")))


### タスクを表示する ###
@app.route("/", methods=["GET", "POST"])
def home():
    # データベースから全てのTodoレコードを取得
    todo_list = Todo.query.all()
    # 取得したTodoリストを"index.html"テンプレートに渡し、ウェブページとして表示
    return render_template("index.html", todo_list=todo_list)

### タスクを追加する ###
@app.route("/add", methods=["GET"])
def add():
    return render_template('add_task.html')

@app.route("/add_task", methods=["POST","GET"])
def add_task():
    if request.method == 'POST':
        # ユーザーから送信されたフォームデータからタイトルを取得
        title = request.form.get("title")
        # ユーザーから送信されたフォームデータからコンテンツを取得
        content = request.form.get("content")
        # 新しいTodoオブジェクトを作成
        new_todo = Todo(title=title, content=content)
        # 新しいTodoをデータベースセッションに追加
        db.session.add(new_todo)
        # 変更をデータベースにコミット
        db.session.commit()
        # タスク追加後、ホームページにリダイレクト
        return redirect(url_for('home'))
    else:# method GETなら以下の処理を行う
        return render_template('add_task.html')

### タスクを編集する ###
@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id): #変数を定義する
    todo = Todo.query.get(id) #データベースからTodo_idを取得
    return render_template("edit_task.html", todo=todo) #タスク編集画面に移動

@app.route("/update/<int:id>",methods=["POST","GET"])
def update(id):
    todo = Todo.query.get(id)
    todo.title = request.form['title']

    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('home'))

### タスク削除 ###
@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    # URLから渡されたIDに基づいて、該当するTodoをデータベースから取得
    todo = Todo.query.filter_by(id=todo_id).first()
    # 取得したTodoをデータベースセッションから削除
    db.session.delete(todo)
    # 変更をデータベースにコミット
    db.session.commit()
    # タスク削除後、ホームページにリダイレクト
    return redirect(url_for("home"))

### タスク確認 ###
@app.route("/check/<int:id>",methods=["GET", "POST"])
def check(id):
    todo_list = Todo.query.get(id) #データベースからidカラムを確認し対応したレコードを取得
    return render_template('check_task.html', todo_list=todo_list) #check.htmlに表示

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="127.0.0.1", port=8888)