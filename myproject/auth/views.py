from flask import Blueprint, render_template,redirect,url_for
from myproject import db
from myproject.models import Gamer
from myproject.auth.forms import LoginForm, RegistrationForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_blueprint.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        gamer = Gamer.query.filter_by(email = form.email.data).first()
        if gamer.check_password(form.password.data) and gamer is not None:
            login_user(gamer)
            flash('Log in Success!')
            return redirect(url_for("index"))
    return render_template('login.html',form=form)


@auth_blueprint.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        gamer = Gamer(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(gamer)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)