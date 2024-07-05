
@app.route('/edit_task/<int:id>', methods=['GET','POST'])
def go_edit(id): # 関数を定義
    todo = Todo.query.get(id) # getidにTodoテーブルのidをget(取得)する
    return render_template('edit_task.html', todo=todo) #タスク編集ページに遷移する

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    todo = Todo.query.get(id)
    todo.title = request.form['title']

    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('home'))
