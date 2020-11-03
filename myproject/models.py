from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Gamer.query.get(user_id)

class Gamer(db.Model,UserMixin):
    __tablename__ = "gamers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String,unique=True)
    password = db.Column(db.String)
    photo = db.Column(db.String)
    role = db.Column(db.String)
    posts = db.relationship('Post', backref="gamers",lazy='dynamic')
    # clan = relationship('clans', backref="member")
    role = db.Column(db.String)


    def __init__(self, name,email,password):
        # მხოლოდ გვჭირდება ამ ბაზის მოდელისთვის უნიკალური წევრის ატრიბუტის აღწერა
        self.name = name
        self.email=email
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):

        return f"Gamer: {self.name}"


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    reaction = db.Column(db.Integer)  # raodenoba ramdeni mowoneba aqvs
    #comment = db.relationship('comment', backref="posts")
    author_id = db.Column(db.Integer,db.ForeignKey("gamers.id"))

    def __init__(self, title, text,gamer_id):
        self.title = title
        self.text = text
        self.author_id = gamer_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"

    def author_name(self):
        return "Unknown"
