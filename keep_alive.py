from threading import Thread
from flask import Flask


app = Flask('')


@app.route('/')
def home():
    return "Hello. I am alive!"


def run():
    app.run(host='ordo-bot.herokuapp.com', port=443)


def keep_alive():
    t = Thread(target=run)
    t.start()
