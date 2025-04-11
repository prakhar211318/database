from app import db, Artist, Artwork, app

with app.app_context():
    # Find existing artist or create new
    artist = Artist.query.filter_by(name="Claude Monet").first()
    if not artist:
        artist = Artist(name="Claude Monet", bio="French impressionist painter.")
        db.session.add(artist)
        db.session.commit()

    artwork = Artwork(
        title="Impression, Sunrise",
        description="The painting that gave Impressionism its name.",
        price=1200000,
        image_url="https://upload.wikimedia.org/wikipedia/en/7/74/PicassoGuernica.jpg",
        artist=artist
    )
    artwork = Artwork(
        title="Impression, Sunrise",
        description="The painting that gave Impressionism its name.",
        price=1200000,
        image_url="https://upload.wikimedia.org/wikipedia/en/7/74/PicassoGuernica.jpg",
        artist=artist
    )
    artwork = Artwork(
        title="Impression, Sunrise",
        description="The painting that gave Impressionism its name.",
        price=1200000,
        image_url="https://upload.wikimedia.org/wikipedia/en/7/74/PicassoGuernica.jpg",
        artist=artist
    )
    db.session.add(artwork)
    db.session.commit()
    print("✅ Artwork added successfully!")
