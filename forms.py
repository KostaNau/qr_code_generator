from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import Length, InputRequired


class UserTextField(FlaskForm):
    text = StringField(label='Input you text for encoding:', validators=[
        Length(min=5, max=140, message='Minimum 5 characters or 140 characters for maximum'), InputRequired()
    ])

    mode = SelectField(label='Choose your mode:', choices=[('link', 'Get a link'), ('download', 'Download file')])

