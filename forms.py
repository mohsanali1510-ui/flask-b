from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo
)


class ContactForm(FlaskForm):
    name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(min=3, max=50)]
    )

    email = StringField(
        "Email Address",
        validators=[DataRequired(), Email()]
    )

    phone = StringField(
        "Phone",
        validators=[DataRequired(), Length(min=11, max=15)]
    )

    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10)]
    )

    submit = SubmitField("Send Message")
    
 
 
 
 
    
class LoginForm(FlaskForm):

    username = StringField("Username", validators=[
            DataRequired(),
            Length(min=3, max=30)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    remember_me = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Login"
    )
    
    
    
    
class RegistrationForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=30)
        ]
    )

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField("Register")