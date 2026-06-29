import sqlite3
from pathlib import Path

DB_PATH = Path("data/hermes.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            chat_id INTEGER UNIQUE NOT NULL,

            first_name TEXT,

            username TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            active INTEGER DEFAULT 1

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interests (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            category TEXT,

            FOREIGN KEY(user_id) REFERENCES users(id)

        )
    """)

    conn.commit()
    conn.close()


def add_user(chat_id, first_name, username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users
        (chat_id, first_name, username)
        VALUES (?, ?, ?)
    """, (chat_id, first_name, username))

    conn.commit()
    conn.close()


def get_users():

    conn = get_connection()

    users = conn.execute(
        "SELECT * FROM users WHERE active = 1"
    ).fetchall()

    conn.close()

    return users