from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_type = db.Column(db.String(50), nullable=False)
    booking_date = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session.modified = True
            return redirect(url_for('book_car'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have successfully logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except:
            flash('Username already exists.', 'danger')
    return render_template('register.html')

@app.route('/book', methods=['GET', 'POST'])
def book_car():
    if 'user_id' not in session:
        flash('You need to login first.', 'warning')
        return redirect(url_for('login'))
    if request.method == 'POST':
        car_type = request.form['carType']
        booking_date = request.form['bookingDate']
        user_id = session['user_id']
        new_booking = Booking(user_id=user_id, car_type=car_type, booking_date=booking_date)
        db.session.add(new_booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('book_car'))
    return render_template('book.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
