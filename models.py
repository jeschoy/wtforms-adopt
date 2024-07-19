from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

DEFAULT_URL = 'https://media.istockphoto.com/id/1142468743/fr/vectoriel/icône-de-forme-de-coeur-en-rouge-rose-couleur-animal-patte-imprimé.jpg?s=170667a&w=0&k=20&c=fIZbfZHl3B23hPDNs5BNtOTHGUAq2nDrh4Oa_UY-7TQ='

class Pet(db.Model):
  __tablename__ = "pets"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  species = db.Column(db.Text, nullable=False)
  photo_url = db.Column(db.Text)
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean, nullable=False, default=True)

  def image_url(self):
    return self.photo_url or DEFAULT_URL


