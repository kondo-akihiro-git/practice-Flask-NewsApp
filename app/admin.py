# app/admin.py

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    from app import db
    from app.models import Article

    admin = Admin(app, name='News Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(Article, db.session))
