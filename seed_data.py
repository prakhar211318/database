from app import db, Artist, Artwork, app

with app.app_context():
    db.create_all()

    # Delete old data (if needed)
    Artwork.query.delete()
    Artist.query.delete()
    db.session.commit()

    # Add fresh sample artists and artworks
    artist1 = Artist(name="Salvador Dalí", bio="Spanish surrealist known for striking and bizarre images.")
    artist2 = Artist(name="Hokusai", bio="Japanese ukiyo-e painter and printmaker.")
    artist3 = Artist(name="Pablo Picasso", bio="Spanish painter, sculptor, printmaker.")

    art1 = Artwork(
        title="The Persistence of Memory",
        description="A surreal painting famous for its melting clocks.",
        price=1500000,
        image_url="https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg",
        artist=artist1
    )

    art2 = Artwork(
        title="The Great Wave off Kanagawa",
        description="A famous Japanese woodblock print showing a massive wave.",
        price=900000,
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0a/Great_Wave_off_Kanagawa2.jpg",
        artist=artist2
    )

    art3 = Artwork(
        title="Guernica",
        description="Powerful anti-war painting by Picasso.",
        price=2000000,
        image_url="https://upload.wikimedia.org/wikipedia/en/7/74/PicassoGuernica.jpg",
        artist=artist3
    )

    db.session.add_all([artist1, artist2, artist3, art1, art2, art3])
    db.session.commit()

    print("✅ Fresh seed data added successfully!")
