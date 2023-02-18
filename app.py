import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("/home/chrisnoper/bidding-game-server-v2/db.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def main():  # put application's code here
    conn = get_db_connection()
    player_stats = conn.execute("SELECT * from players").fetchall()

    return render_template('index.html', player_stats=player_stats)


if __name__ == '__main__':
    app.run()
