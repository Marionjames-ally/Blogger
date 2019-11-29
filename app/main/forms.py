from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog title'. validators=[Required()])
    content = TextAreaField('Your Blog', validators=[Required()])
    submit = SubmitField('Submit')
