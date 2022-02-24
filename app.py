from re import L
from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

dummyPosts = [
    {
        'author' : 'Girish',
        'date'   : '17th July 2022',
        'title'  : 'Random Gibberish',
        'content': 'I posted this ass shit'
    },
    {
        'author' : 'Ashwin',
        'date'   : '9th June 2020',
        'title'  : 'More Random Gibberish',
        'content': 'I posted more ass shit'
    }
]


app = Flask(__name__)
app.config['SECRET_KEY'] = '11105a147f4846ffc9062bd46c2477cf'

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