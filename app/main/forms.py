from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms import validators
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment...', validators=[InputRequired()])
    submit = SubmitField('comment')

class PostForm(FlaskForm):
    title = StringField('your post title...', validators=[InputRequired()])
    post_content = TextAreaField("what's your post all about...", validators=[InputRequired()])
    submit = SubmitField('create post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell people about yourself...')
    submit = SubmitField('submit')