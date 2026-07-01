import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("data/hermes.db")


class Database:

    def __init__(self):

        DB_PATH.parent.mkdir(exist_ok=True)

        self.conn = sqlite3.connect(DB_PATH)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

        self.create_tables()

    # ============================================================
    # TABLAS
    # ============================================================

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            chat_id INTEGER UNIQUE NOT NULL,

            first_name TEXT,

            last_name TEXT,

            username TEXT,

            language TEXT DEFAULT 'es',

            timezone TEXT DEFAULT 'Atlantic/Canary',

            briefing_time TEXT DEFAULT '08:00',
                            
            active INTEGER DEFAULT 1,

            created_at TEXT,

            last_seen TEXT

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS interests(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            category TEXT,

            enabled INTEGER DEFAULT 1,

            UNIQUE(user_id,category),

            FOREIGN KEY(user_id) REFERENCES users(id)

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS deliveries(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            sent_at TEXT,

            status TEXT,

            duration REAL,

            FOREIGN KEY(user_id) REFERENCES users(id)

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            level TEXT,

            module TEXT,

            message TEXT,

            created_at TEXT

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS news_cache(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            category TEXT,

            title TEXT,

            url TEXT,

            published TEXT

        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            chat_id INTEGER NOT NULL,

            city TEXT NOT NULL,

            UNIQUE(chat_id, city)

        )
        """)
        self.conn.commit()

    # ============================================================
    # UTILIDADES
    # ============================================================

    @staticmethod
    def now():

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def commit(self):

        self.conn.commit()

    def close(self):

        self.conn.commit()

        self.conn.close()
    # ============================================================
    # USERS
    # ============================================================

    def add_user(
        self,
        chat_id,
        first_name="",
        last_name="",
        username=""
    ):

        if self.user_exists(chat_id):

            self.cursor.execute(
                """
                UPDATE users
                SET
                    first_name=?,
                    last_name=?,
                    username=?,
                    last_seen=?,
                    active=1
                WHERE chat_id=?
                """,
                (
                    first_name,
                    last_name,
                    username,
                    self.now(),
                    chat_id,
                ),
            )

        else:

            self.cursor.execute(
                """
                INSERT INTO users
                (
                    chat_id,
                    first_name,
                    last_name,
                    username,
                    created_at,
                    last_seen
                )
                VALUES(?,?,?,?,?,?)
                """,
                (
                    chat_id,
                    first_name,
                    last_name,
                    username,
                    self.now(),
                    self.now(),
                ),
            )

        self.commit()

    def user_exists(self, chat_id):

        row = self.cursor.execute(
            """
            SELECT id
            FROM users
            WHERE chat_id=?
            """,
            (chat_id,),
        ).fetchone()

        return row is not None

    def get_user(self, chat_id):

        row = self.cursor.execute(
            """
            SELECT *
            FROM users
            WHERE chat_id=?
            """,
            (chat_id,),
        ).fetchone()

        if row:

            return dict(row)

        return None
    # ============================================================
# TIMEZONE
# ============================================================

def get_timezone(self, chat_id):

    row = self.cursor.execute(
        """
        SELECT timezone
        FROM users
        WHERE chat_id=?
        """,
        (chat_id,),
    ).fetchone()

    if row:
        return row["timezone"]

    return "Atlantic/Canary"


def set_timezone(self, chat_id, timezone):

    self.cursor.execute(
        """
        UPDATE users
        SET timezone=?
        WHERE chat_id=?
        """,
        (
            timezone,
            chat_id,
        ),
    )

    self.commit()


# ============================================================
# BRIEFING TIME
# ============================================================

def get_briefing_time(self, chat_id):

    row = self.cursor.execute(
        """
        SELECT briefing_time
        FROM users
        WHERE chat_id=?
        """,
        (chat_id,),
    ).fetchone()

    if row:
        return row["briefing_time"]

    return "08:00"


def set_briefing_time(self, chat_id, briefing_time):

    self.cursor.execute(
        """
        UPDATE users
        SET briefing_time=?
        WHERE chat_id=?
        """,
        (
            briefing_time,
            chat_id,
        ),
    )

    self.commit()
    
    # ============================================================
    # OBTENER TODOS LOS USUARIOS
    # ============================================================

    def get_all_users(self):

        rows = self.cursor.execute(
            """
            SELECT *
            FROM users
            WHERE active = 1
            ORDER BY first_name
            """
        ).fetchall()

        return [dict(row) for row in rows]
    # ============================================================
    # ACTUALIZAR ÚLTIMA CONEXIÓN
    # ============================================================

    def update_last_seen(self, chat_id):

        self.cursor.execute(
            """
            UPDATE users
            SET last_seen=?
            WHERE chat_id=?
            """,
            (
                self.now(),
                chat_id,
            ),
        )

        self.commit()
    # ============================================================
    # CITIES
    # ============================================================

    def add_city(self, chat_id, city):

        self.cursor.execute(
            """
            INSERT OR IGNORE INTO cities
            (
                chat_id,
                city
            )
            VALUES (?,?)
            """,
            (
                chat_id,
                city,
            ),
        )

        self.commit()

    def remove_city(self, chat_id, city):

        self.cursor.execute(
            """
            DELETE FROM cities
            WHERE chat_id=?
            AND city=?
            """,
            (
                chat_id,
                city,
            ),
        )

        self.commit()

    def get_cities(self, chat_id):

        rows = self.cursor.execute(
            """
            SELECT city
            FROM cities
            WHERE chat_id=?
            ORDER BY city
            """,
            (chat_id,),
        ).fetchall()

        return [row["city"] for row in rows]
    # ============================================================
    # INTERESTS
    # ============================================================

    def set_interests(self, chat_id, interests):

        user = self.get_user(chat_id)

        if not user:
            return

        self.cursor.execute(
            """
            DELETE FROM interests
            WHERE user_id=?
            """,
            (user["id"],),
        )

        for interest in interests:

            self.cursor.execute(
                """
                INSERT INTO interests
                (
                    user_id,
                    category,
                    enabled
                )
                VALUES (?,?,1)
                """,
                (
                    user["id"],
                    interest,
                ),
            )

        self.commit()

    def get_interests(self, chat_id):

        user = self.get_user(chat_id)

        if not user:
            return []

        rows = self.cursor.execute(
            """
            SELECT category
            FROM interests
            WHERE user_id=?
            AND enabled=1
            ORDER BY category
            """,
            (user["id"],),
        ).fetchall()

        return [row["category"] for row in rows]

    # ============================================================
    # SETTINGS
    # ============================================================

    def set_setting(self, key, value):

        row = self.cursor.execute(
            """
            SELECT id
            FROM settings
            WHERE key=?
            """,
            (key,),
        ).fetchone()

        if row:

            self.cursor.execute(
                """
                UPDATE settings
                SET value=?
                WHERE key=?
                """,
                (
                    value,
                    key,
                ),
            )

        else:

            self.cursor.execute(
                """
                INSERT INTO settings
                (
                    key,
                    value
                )
                VALUES (?,?)
                """,
                (
                    key,
                    value,
                ),
            )

        self.commit()

    def get_setting(self, key, default=None):

        row = self.cursor.execute(
            """
            SELECT value
            FROM settings
            WHERE key=?
            """,
            (key,),
        ).fetchone()

        if row:
            return row["value"]

        return default

    # ============================================================
    # LOGS
    # ============================================================

    def add_log(self, level, module, message):

        self.cursor.execute(
            """
            INSERT INTO logs
            (
                level,
                module,
                message,
                created_at
            )
            VALUES (?,?,?,?)
            """,
            (
                level,
                module,
                message,
                self.now(),
            ),
        )

        self.commit()

    def get_logs(self, limit=100):

        rows = self.cursor.execute(
            """
            SELECT *
            FROM logs
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

        return [dict(row) for row in rows]

    # ============================================================
    # DELIVERIES
    # ============================================================

    def add_delivery(
        self,
        chat_id,
        status="OK",
        duration=0,
    ):

        user = self.get_user(chat_id)

        if not user:
            return

        self.cursor.execute(
            """
            INSERT INTO deliveries
            (
                user_id,
                sent_at,
                status,
                duration
            )
            VALUES (?,?,?,?)
            """,
            (
                user["id"],
                self.now(),
                status,
                duration,
            ),
        )

        self.commit()

    # ============================================================
    # NEWS CACHE
    # ============================================================

    def cache_news(
        self,
        category,
        title,
        url,
        published,
    ):

        exists = self.cursor.execute(
            """
            SELECT id
            FROM news_cache
            WHERE url=?
            """,
            (url,),
        ).fetchone()

        if exists:
            return

        self.cursor.execute(
            """
            INSERT INTO news_cache
            (
                category,
                title,
                url,
                published
            )
            VALUES (?,?,?,?)
            """,
            (
                category,
                title,
                url,
                published,
            ),
        )

        self.commit()

    def get_cached_news(
        self,
        category=None,
        limit=20,
    ):

        if category:

            rows = self.cursor.execute(
                """
                SELECT *
                FROM news_cache
                WHERE category=?
                ORDER BY id DESC
                LIMIT ?
                """,
                (
                    category,
                    limit,
                ),
            ).fetchall()

        else:

            rows = self.cursor.execute(
                """
                SELECT *
                FROM news_cache
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [dict(row) for row in rows]
