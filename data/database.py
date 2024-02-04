import sqlite3


class DataBase:
    def __init__(self, db_fie):
        self.conn = sqlite3.connect(db_fie)
        self.cursor = self.conn.cursor()

    def create_table(self):
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS narkos (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, count_pay INTEGER, friends INTEGER, your_friends INTEGER, bonus INTEGER)')

    def location_base(self):
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS locations (id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT, price INTEGER, area TEXT, foto1 TEXT, foto2 TEXT)')

    def add_user(self, user_id, count_pay, friends, your_friends, bonus):
        with self.conn:
            self.cursor.execute('INSERT OR IGNORE INTO narkos (user_id, count_pay, friends, your_friends, bonus) VALUES (?, ?, ?, ?, ?)', (user_id, count_pay, friends, your_friends, bonus))
            self.conn.commit()

    def check_user(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT your_friend FROM narkos WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def in_is_base(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT user_id FROM narkos WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def your_friends(self, user_id, your_friends):
        with self.conn:
            result = self.cursor.execute('UPDATE narkos SET your_friends = ? WHERE user_id = ?', (user_id, your_friends))
            self.conn.commit()

