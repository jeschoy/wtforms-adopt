from models import db, Pet
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name='Fido', species='dog', photo_url='https://hips.hearstapps.com/hmg-prod/images/small-fluffy-dog-breeds-maltipoo-66300ad363389.jpg?crop=0.668xw:1.00xh;0.151xw,0&resize=640:*', age=3, notes='Friendly and fun!', available=True)
pet2 = Pet(name='Mittens', species='cat', age=4, notes='Lazy but loves to cuddle!', available=True)
pet3 = Pet(name='Spot', species='dog', photo_url='https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', age=7, notes='High energy for age!', available=True)
pet4 = Pet(name='Harriet', species='dog', age=2, notes='Quiet and shy!', available=False)
pet5 = Pet(name='Fluffy', species='cat', photo_url='https://images.squarespace-cdn.com/content/v1/554e744ce4b026a2b08ca248/1617119487270-BETH6VBY11R14F01R5O3/2020_6_Ada_Foster_AndrewDorman_2.jpg', age=1, notes='Young and learning life!', available=True)

db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()
