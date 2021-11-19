from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms import validators
from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment...', validators=[InputRequired()])
    submit = SubmitField('comment')

class PostForm(FlaskForm):
    title = StringField('your item title...', validators=[InputRequired()])
    item_description = TextAreaField("describe what you are selling...", validators=[InputRequired()])
    item_price = IntegerField('Enter the items price..', validators=[InputRequired()]) 
    category = RadioField('pick a category where your item falls into', validators=[InputRequired()], choices=[('vegetables'), ('fruits'), ('diaries'), ('meat')])
    submit = SubmitField('post item')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about yourself...')
    submit = SubmitField('submit')