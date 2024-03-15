from utils import SCORES_FILE_NAME, file_exist, replace_txt


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    html_path = 'main_score.py'
    if file_exist(SCORES_FILE_NAME):
        score_file = open(SCORES_FILE_NAME, 'r')
        file_contents = score_file.readlines()
        for line in file_contents:
            file_contents = POINTS_OF_WINNING + int(line)
            score_file = open(SCORES_FILE_NAME, 'w')
            score_file.write(str(file_contents))
        print(file_contents)
        replace_txt(html_path, '{SCORE}', file_contents)
        score_file.close()
    else:
        score_file = open(SCORES_FILE_NAME, 'w')
        score_file.write(str(POINTS_OF_WINNING))
        score_file.close()
        score_file = open(SCORES_FILE_NAME, 'r')
        file_con = score_file.read()
        print(file_con)
        replace_txt(html_path, '{SCORE}', file_con)
        score_file.close()
