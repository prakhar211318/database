from app import db, app, Artist, Artwork, Buyer
from tabulate import tabulate

with app.app_context():
    artists = Artist.query.all()
    artworks = Artwork.query.all()
    buyers = Buyer.query.all()

    print("\n🎨 Artists:")
    print(tabulate([[a.id, a.name, a.bio] for a in artists], headers=["ID", "Name", "Bio"]))

    print("\n🖼️ Artworks:")
    print(tabulate(
        [[a.id, a.title, a.artist_id, a.price, a.image_url] for a in artworks],
        headers=["ID", "Title", "Artist ID", "Price", "Image URL"]
    ))

    print("\n🛍️ Buyers:")
    print(tabulate([[b.id, b.name, b.email, b.otp] for b in buyers], headers=["ID", "Name", "Email", "OTP"]))
