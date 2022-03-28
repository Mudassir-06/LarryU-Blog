from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User



# Registration Form: The class RegistrationForm will inherit from FlaskForm. Within our form, we'll have different form fields.
class RegistrationForm(FlaskForm):

    # Create a new attribute:

    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=50)])

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])

    # Once we have finished these forms, we need a submit button to send that info to us --> can do that using SubmitField
    submit = SubmitField("Sign Up")

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is already taken. Please choose a different one.")

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is already taken. Please choose a different one.")


# Login Form: The class LoginForm will inherit from FlaskForm. Within our form, we'll have different form fields, so we create attributes accordingly.
class LoginForm(FlaskForm):
    # Create a new attribute:
    # We will use the email as the Login form here.

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    # Need to allow users to stay logged in for some time after their browser closes, using a secure cookie.
    remember = BooleanField("Remember Me")

    # Once we have finished these forms, we need a submit button to send that info to us --> can do that using SubmitField
    submit = SubmitField("Login")

    # Next : Need to set up a secret key for our app. A secret key will protect against modifying cookies, cross-site forgery attacks, etc. Set under out app variable in our application file.


class UpdateAccountForm(FlaskForm):

    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "That username is already taken. Please choose a different one."
                )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "That email is already taken. Please choose a different one."
                )


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email. You must register first!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")