from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea

'''
Form for lowell student easier latin searching
For emerson lol
'''


class LatinForm(FlaskForm):
    link = None
    word = StringField('Word:')
    submit = SubmitField('Find')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class CreateShortLink(FlaskForm):
    longurl = StringField(
        'Url to shorten', validators=[DataRequired(), Length(max=120)]
    )
    clearCount = BooleanField('Clear url usage count?')
    submit = SubmitField('Shorten')


class ConfirmPassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class CreateWorkshop(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=80)])
    repo = StringField('Repo url', validators=[Length(max=100)])
    markdown = StringField('Markdown url', validators=[DataRequired(), Length(max=150)])
    url = StringField(
        'Url Route', validators=[DataRequired(), Length(max=80)]
    )
    text = TextAreaField(
        'Description',
        widget=TextArea(),
        validators=[
            DataRequired(),
            Length(max=1500, message='Description must be 500 characters or less'),
        ],
    )
    submit = SubmitField('Create')


class CreateUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create')
