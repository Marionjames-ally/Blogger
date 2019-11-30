from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import login_manager
from . import db

@login_manager.user_loader
def load_user(writer_id):
    return Writer.query.get(int(writer_id))


class Writer(db.Model, UserMixin):
    __tablename__ = 'writers'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    pass_word = db.Column(db.String)
    blogg = db.relationship('Blogs', backref = 'writer', lazy = 'dynamic')

    @property
    def password(self):
        raise  AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_word = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_word, password)

    def __repr__(self):
        return f'Writer {self.username}'

    
class Blogs(db.Model, UserMixin):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key = True)
    blog_id = db.Column(db.Integer)
    blog_title = db.Column(db.String)
    blog_content = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    writer_id = db.Column(db.Integer,db.ForeignKey("writers.id"))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete()

    @classmethod
    def get_blog(cls, id):
        blog = Blogs.query.filter_by(blog_id=id).all()
        return blog

class Quotes:
    '''
    class that returns the quotes objects
    '''

    def __init__(self,author,id,quote):
        self.id = id
        self.author = author
        self.quote = quote
