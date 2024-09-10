## データベースが作られてない時の対処法

```
python3
```
でpythonの対話モードに入ります

```python
>>>from app import app
>>>from app import db
>>> with app.app_context():
...     db.create_all()

# 抜け方
exit()
```

## ポートに関して
もし`flask run`で指定したポートじゃない時
```sh
flask run --port 8888
```


## githubに関して
クローン
```sh
git clone https://github.com/kurokiri1763/ToDo-List.git
```
ブランチを切る
```bash
git branch {ブランチの名前}
# or
git checkout -b {ブランチの名前}
```
ブランチの移動方法
```sh
git checkout {移動したいブランチの名前}
```
プッシュまでの流れ
```sh
git add .
git commit -m "コミットの内容"
git push origin {プッシュしたいブランチの名前}
```
変更内容の確認
```sh
git status
```

developからoriginにpull
```sh
git pull origin
```

mergeするとき
```sh
git merge {取り込みたいブランチ} {取り込み先のブランチ}
```


## その他メモ
デバッグモードを起動する
```python
export FLASK_DEBUG=1
```

## dbの更新
migrateというものを使う
### 流れ
```

```sh
flask db init # データベースを初期化
flask db migrate # dbをmigrateする
flask db upgrade # 更新する
```


### エラーメモ

```sh
no such command 'db'
```

```sh
この場合は
flask-migrateが入っていない時に起こる
pipでインストールしてimportしてやる
```