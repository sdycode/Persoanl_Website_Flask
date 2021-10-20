    
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/index.html')
def hello_world():
    return render_template('index.html')

@app.route('/chats.html')
def chats():
    return render_template('chats.html')



@app.route('/appList.html')
def appList():
    return render_template('appList.html')
    
@app.route('/youtube.html')
def youtube():
    return render_template('youtube.html')

if __name__ == '__main__':
    app.run(debug=True)