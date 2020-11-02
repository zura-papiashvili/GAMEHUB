from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTop

from flask_login import current_user
from myproject.models import Gamer

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm',message = 'Password must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    def check_email(self,field):
        if Gamer.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered')

    def check_username(self,field):
        if Gamer.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been already registered')