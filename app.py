from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Models
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    artworks = db.relationship('Artwork', backref='artist')

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image_url = db.Column(db.String(200))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    otp = db.Column(db.String(10))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.id'))

# Routes
@app.route('/')
def home():
    artworks = Artwork.query.limit(3).all()  # Show just 3 artworks on homepage
    return render_template('index.html', artworks=artworks)

@app.route('/gallery')
def gallery():
    artworks = Artwork.query.all()
    return render_template('gallery.html', artworks=artworks)

@app.route('/login/<int:artwork_id>', methods=['GET', 'POST'])
def login(artwork_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        otp = str(random.randint(1000, 9999))
        buyer = Buyer(name=name, email=email, phone=phone, otp=otp, artwork_id=artwork_id)
        db.session.add(buyer)
        db.session.commit()
        return render_template('success.html', otp=otp)
    return render_template('login.html', artwork_id=artwork_id)

if __name__ == '__main__':
    app.run(debug=True)
