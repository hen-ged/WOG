from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def score_server():
    return render_template('score_server.html',name='SCORES')

if __name__ == '__main__':
    app.run()

