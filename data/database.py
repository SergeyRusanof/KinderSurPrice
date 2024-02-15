import sqlite3


class DataBase:
    def __init__(self, db_fie):
        self.conn = sqlite3.connect(db_fie)
        self.cursor = self.conn.cursor()

    def create_table(self):
        """Создание основной таблицы юзеров"""
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS narkos (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, count_pay INTEGER, bonus INTEGER)')

    def location_base(self):
        """Создание таблицы локаций"""
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS locations (id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT, price INTEGER, area TEXT, foto1 TEXT, foto2 TEXT)')

    def refers_table(self):
        """Создание таблицы рефералов"""
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS refers (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, friends INTEGER, your_friend INTEGER)')

    def add_user_in_narcos(self, user_id, count_pay, bonus):
        with self.conn:
            self.cursor.execute('INSERT OR IGNORE INTO narkos (user_id, count_pay, bonus) VALUES (?, ?, ?)', (user_id, count_pay, bonus))
            self.conn.commit()

    def add_user_in_refers(self, user_id, friends, your_friend):
        with self.conn:
            self.cursor.execute('INSERT OR IGNORE INTO refers (user_id, friends, your_friend) VALUES (?, ?, ?)', (user_id, friends, your_friend))
            self.conn.commit()

    def check_user(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT your_friend FROM narkos WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def in_is_narcos(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT user_id FROM narkos WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def in_is_refers(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT user_id FROM refers WHERE user_id = ?', (user_id,)).fetchone()
            return result

    def your_friend(self, user_id, your_friend):
        with self.conn:
            result = self.cursor.execute('UPDATE refers SET your_friend = ? WHERE user_id = ?', (your_friend, user_id))
            self.conn.commit()

    def friends(self, user_id, friends):
        with self.conn:
            result = self.cursor.execute('UPDATE refers SET friends=? WHERE user_id=?', (friends, user_id))
            self.conn.commit()

