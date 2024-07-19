from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
  name = StringField("Pet Name", validators=[InputRequired()])
  species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("rabbit", "Rabbit")])
  photo_url = StringField("Photo URL", validators=[Optional(), URL()])               
  age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=20)])
  notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
  photo_url = StringField('Photo URL')
  notes = StringField("Notes", validators=[Optional()])
  available = BooleanField("Available")