from flask import Flask, render_template
from utils import BAD_RETURN_CODE,SCORES_FILE_NAME,file_exist
app = Flask(__name__)


@app.route('/')
def score_server():
    if file_exist(SCORES_FILE_NAME):
        return render_template('score_server.html', name='SCORES')
    else:
        return render_template('scores_error.html', name='ERROR')

if __name__ == '__main__':
    app.run()
