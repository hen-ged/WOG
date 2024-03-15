FROM python:3.8-alpine
COPY ./Requirements.txt Requirements.txt
COPY ./Scores.txt Scores.txt
RUN pip install -r Requirements.txt
RUN pip install -r Requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=main_score.py
CMD ["flask", "run", "--host", "0.0.0.0"]
