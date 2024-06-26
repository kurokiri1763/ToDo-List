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



