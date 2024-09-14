# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# requirements.txt file .....

Flask==1.1.2
gunicorn==20.1.0
Jinja2==3.0.3
werkzeug==2.0.2
itsdangerous==2.0.1

# run cmd.txt file .......

gunicorn app:app & python3 main.py
              or
gunicorn app:app & python3 bot.py

# app.py file ........

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Tech VJ'


if __name__ == "__main__":
    app.run()
  
#Dockerfile

FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD gunicorn app:app & python3 bot.py
