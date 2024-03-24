FROM python:3.8-alpine
RUN mkdir /app
WORKDIR /app
COPY ./Requirements.txt app/Requirements.txt
COPY ./Scores.txt app/Scores.txt
COPY ./main_score.py app/main_score.py
COPY ./utils.py app/utils.py
RUN pip install -r app/Requirements.txt
ENV FLASK_APP=app/main_score.py
EXPOSE 5000
CMD ["flask", "run","--host", "0.0.0.0"]
