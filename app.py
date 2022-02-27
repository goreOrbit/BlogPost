from this import d
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from re import L
from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

dummyPosts = [
    {
        'author' : 'Girish',
        'date'   : '17th July 2022',
        'title'  : 'SHHWISXBTSXABB',
        'content': 'AJBSCHJBASXHJBADVH'
    },
    {
        'author' : 'Ashwin',
        'date'   : '9th June 2020',
        'title'  : 'AJBXHABSHVASHG',
        'content': 'ASXBAHSSVHASBCHGSAHGXHGASV'
    }
]


app = Flask(__name__)
app.config['SECRET_KEY'] = '11105a147f4846ffc9062bd46c2477cf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}, '{self.date_posted}')"

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home', posts=dummyPosts)

@app.route('/chat')
def chat():
    return render_template('chat.html', title='Chats')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)