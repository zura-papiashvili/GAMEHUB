from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

class PostForm(FlaskForm):
    title = StringField(description="Title")
    text = StringField(description="Text")
    submit = SubmitField("Create a Post")