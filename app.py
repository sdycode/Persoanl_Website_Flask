from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index.html')
def hello_worldwe():
    return render_template('index.html')


@app.route('/chats.html')
def chats():
    return render_template('chats.html')

@app.route('/musicplayer.html')
def music():
    return render_template('musicplayer.html')
    
@app.route('/receipies.html')
def receipies():
    return render_template('receipies.html')

@app.route('/spacexcrew.html')
def spacexcrew():
    return render_template('spacexcrew.html')

@app.route('/ymart.html')
def ymart():
    return render_template('ymart.html')

@app.route('/weather.html')
def weather():
    return render_template('weather.html')

@app.route('/appList.html')
def appList():
    return render_template('appList.html')


@app.route('/navbar.html')
def navbar():
    return render_template('navbar.html')


@app.route('/youtube.html')
def youtube():
    return render_template('youtube.html')


if __name__ == '__main__':
    app.run(debug=True)
