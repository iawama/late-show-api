from app import app, db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()
    
    # Seed guests
    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Smith", occupation="Comedian")
    db.session.add_all([guest1, guest2])
    
    # Seed episodes
    episode1 = Episode(date=date(2025, 6, 1), number=1)
    episode2 = Episode(date=date(2025, 6, 2), number=2)
    db.session.add_all([episode1, episode2])
    
    # Seed appearances
    appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
    appearance2 = Appearance(rating=5, guest_id=2, episode_id=2)
    db.session.add_all([appearance1, appearance2])
    
    db.session.commit()
    print("Database seeded successfully!")