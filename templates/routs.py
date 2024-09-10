from flask import render_template, url_for, flash, redirect, request
from your_application import app, db, bcrypt
from your_application.forms import RegistrationForm, LoginForm
from your_application.models import User
from flask_login import login_user, current_user, logout_user, login_required

### ユーザー登録 ###
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('アカウントが作成されました！ログインしてください。', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

### ログイン ###
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('ログインに成功しました。', 'success')
            return redirect(url_for('home'))
        else:
            flash('ログインに失敗しました。メールアドレスまたはパスワードを確認してください。', 'danger')
    return render_template('login.html', title='Login', form=form)

### ログアウト ###
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/home")
@login_required
def home():
    return render_template('home.html')
