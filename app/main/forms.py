from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from ..models import User
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import Subscription

class PostForm(FlaskForm): #create a class that inherits from FlaskForm class
    category = SelectField('Choose Blog Category', choices =[('General','General'),('Life','Life'),('Cars','Cars'),('News','News'),('Music','Music'),('Technology','Technology')],validators=[Required()])
    post = TextAreaField('Type Blog Post Below:', validators=[Required()])
    submit = SubmitField('Submit')



class CommentsForm(FlaskForm):
    comments = TextAreaField('Comment on the Post', validators=[Required()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR POST')
    submit = SubmitField('SUBMIT')

class SubscribeForm(FlaskForm):
    email = StringField('Email address', validators=[Required(), Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self, email):
        email = Subscription.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already subscribed to our emailing list.')


