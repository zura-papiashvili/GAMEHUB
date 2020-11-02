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
<<<<<<< HEAD
    #  One_to_one relationship
    # A student only has one teacher, thus uselist is False.
    # Strong assumption of 1 teacher per 1 student and vice versa.
    teacher = db.relationship('Teacher', backref="gamers", uselist=False)
=======
    email = db.Column(db.String,unique=True)
    password = db.Column(db.String)
    photo = db.Column(db.String)
    role = db.Column(db.String)
    # posts = relationship('posts', backref="author",lazy=True)
    # clan = relationship('clans', backref="member")
    role = db.Column(db.String)
>>>>>>> e29d5db273b9cb57533b08de20ee33cb631bdf3a


    def __init__(self, name,email,password):
        # მხოლოდ გვჭირდება ამ ბაზის მოდელისთვის უნიკალური წევრის ატრიბუტის აღწერა
        self.name = name
        self.email=email
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):

        return f"Gamer: {self.name}"


class Post(db.Model):
    tablename = "posts"
    gamers = db.relationship(Gamer)
    id = db.Column(db.Integer, primary_key=True)
    gamer_id=db.Column(db.Integer,db.ForeignKey('gamers.id'),nullable=False)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    reaction = db.Column(db.Integer)  # raodenoba ramdeni mowoneba aqvs
    comment = db.relationship('comment', backref="posts")
    #author = db.relationship('gamers', backref="posts")


    def __init__(self, title, text,gamer_id):
        self.title = title
        self.text = text
        self.gamer_id = gamer_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
