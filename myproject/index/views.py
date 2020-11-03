from flask import Blueprint, render_template,redirect,url_for
from myproject.index.forms import PostForm
from myproject.models import Post,Gamer
from flask_login import current_user
from myproject import db

index_blueprint = Blueprint("index",__name__,template_folder="templates/index")

@index_blueprint.route("/",methods=["GET","POST"])
@index_blueprint.route("/index",methods=["GET","POST"])
def index():

    form = PostForm()
    posts = Post.query.all()

    if form.validate_on_submit():

        gamer = Gamer.query.filter_by(name=current_user.name).first()

        post = Post(form.title.data,form.text.data,gamer.id)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("index.html",form=form,posts=posts)