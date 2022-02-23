from flask import Flask, render_template, url_for

dummyPosts = [
    {
        'author' : 'Girish',
        'date'   : '17th July 2022',
        'title'  : 'Random Gibberish',
    },
    {
        'author' : 'Ashwin',
        'date'   : '9th June 2020',
        'title'  : 'More Random Gibberish'
    }
]


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home', posts=dummyPosts)

@app.route('/chat')
def chat():
    return render_template('chat.html', title='Chats')

if __name__ == "__main__":
    app.run(debug=True)