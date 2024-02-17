from utils import SCORES_FILE_NAME,file_exist


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    if file_exist(SCORES_FILE_NAME):
        score_file = open(SCORES_FILE_NAME, 'r')
        file_contents = score_file.readlines()
        for line in file_contents:
            file_contents = POINTS_OF_WINNING + int(line)
            score_file = open(SCORES_FILE_NAME, 'w')
            score_file.write(str(file_contents))
        print(file_contents)
        score_file.close()
    else:
        score_file = open(SCORES_FILE_NAME, 'w')
        score_file.write(str(POINTS_OF_WINNING))
        score_file.close()