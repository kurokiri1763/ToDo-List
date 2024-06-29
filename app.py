from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


### タスクを表示する ###
@app.route("/", methods=["GET", "POST"])
def home():
    # データベースから全てのTodoレコードを取得
    todo_list = Todo.query.all()
    # 取得したTodoリストを"index.html"テンプレートに渡し、ウェブページとして表示
    return render_template("index.html", todo_list=todo_list)
### タスク追加 ###
@app.route("/add", methods=["GET"])
def add():
    return render_template('add_task.html')


@app.route("/add_task", methods=["POST","GET"])
def add_task():
    if request.method == 'POST':
        # ユーザーから送信されたフォームデータからタイトルを取得
        title = request.form.get("title")
        # 新しいTodoオブジェクトを作成
        new_todo = Todo(title=title)
        # 新しいTodoをデータベースセッションに追加
        db.session.add(new_todo)
        # 変更をデータベースにコミット
        db.session.commit()
        # タスク追加後、ホームページにリダイレクト
        return redirect(url_for('home'))
    else:# method GETなら以下の処理を行う
        return render_template('add_task.html')


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



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="127.0.0.1", port=8888)