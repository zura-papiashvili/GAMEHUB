from flask import Blueprint, render_template,redirect,url_for
from myproject import db
from myproject.models import Gamer
from myproject.auth.forms import LoginForm, RegistrationForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_blueprint.route("/auth",methods=["GET","POST"])
def auth():

    registrationForm = RegistrationForm()
    loginForm = LoginForm()

    if registrationForm.validate_on_submit():
        gamer = Gamer(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(gamer)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('auth'))
    if loginForm.validate_on_submit():
        gamer = Gamer.query.filter_by(email = form.email.data).first()
        if gamer.check_password(form.password.data) and gamer is not None:
            login_user(gamer)
            flash('Log in Success!')
            return redirect(url_for("index"))
    return render_template('auth.html', regForm=registrationForm,loginForm=loginForm)