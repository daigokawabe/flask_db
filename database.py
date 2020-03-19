# initialization to use SQLAlchemy in Flask application
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# creating an object of class SQLAlchemy
db = SQLAlchemy()
def init_db(app):
    db.init_app(app)
    Migrate(app, db)
    return db

#### メモ ####
# pythonでデータベースを扱う方法の１つがSQLAlchemy。
# オブジェクト指向言語のオブジェクトをそうでないものに変換するためのモジュール。
# SQLAlchemyを使うとPython上のモデル操作で、実際のデータベース構造を変更（参照）できる。
# マイグレーションとはpython上のモデルから、実際のデータベースへの「変換」を表している。
# https://qiita.com/KI1208/items/2581ed6f211a2d73e5fd
####     ####
