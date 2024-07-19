from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'whatabigsecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
connect_db(app)

db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
  pets = Pet.query.all()
  return render_template('home.html', pets=pets)

# @app.route("/add", methods=["GET", "POST"])
# def add_pet():
#     """Add a pet."""

#     form = AddPetForm()

#     if form.validate_on_submit():
#         data = {k: v for k, v in form.data.items() if k != "csrf_token"}
#         new_pet = Pet(**data)
#         # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
#         db.session.add(new_pet)
#         db.session.commit()
#         flash(f"{new_pet.name} added.")
#         return redirect('/')

#     else:
#         # re-present form for editing
#         return render_template("pet_add_form.html", form=form)

@app.route('/add', methods=["POST", "GET"])
def add_pet():
  form = AddPetForm()
  if form.validate_on_submit():
    data = form.datadata = {k: v for k, v in form.data.items() if k != "csrf_token"}    
    new_pet = Pet(**data)
    db.session.add(new_pet)
    db.session.commit()
    return redirect('/')
  return render_template('pet_add_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet(pet_id):
  pet = Pet.query.get_or_404(pet_id)
  form = EditPetForm(obj=pet)
  if form.validate_on_submit():
    pet.available = form.available.data
    pet.notes = form.notes.data
    pet.photo_url = form.photo_url.data
    db.session.commit()
  return render_template('pet_details.html', pet=pet, form=form)