from flask import Flask
from config.utils import BAD_RETURN_CODE, SCORES_FILE_NAME,file_exist

app = Flask(__name__)


@app.route('/')
def score_server():
    if file_exist(SCORES_FILE_NAME):
        return "<html> <head><title>Scores Game</title></head><body><h1>The score is:</h1><div id='score'>8</div></body></html>"
    elif BAD_RETURN_CODE==0:
        return "<html><head><title>Scores Game</title></head><body><h1>ERROR:</h1><div id='score' style='color=red'>{ERROR}</div></body></html>"


if __name__ == '__main__':
    app.run()
