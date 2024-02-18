import sqlite3
from configure.config import ADMIN


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

    def to_buy_table(self):
        """Создание таблицы для покупки товара"""
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS to_buy (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, prod TEXT, location TEXT, price INTEGER)')

    def payment_table(self):
        """Создание таблицы для оплаты"""
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS payment (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, name TEXT, role TEXT, status BOOLEAN NOT NULL DEFAULT (False), label TEXT DEFAULT (1), count INTEGER DEFAULT (0))')



    def add_user_in_narcos(self, user_id, count_pay, bonus):
        with self.conn:
            self.cursor.execute('INSERT OR IGNORE INTO narkos (user_id, count_pay, bonus) VALUES (?, ?, ?)', (user_id, count_pay, bonus))
            self.conn.commit()

    def add_user_in_refers(self, user_id, friends, your_friend):
        with self.conn:
            self.cursor.execute('INSERT OR IGNORE INTO refers (user_id, friends, your_friend) VALUES (?, ?, ?)', (user_id, friends, your_friend))
            self.conn.commit()

    def add_in_to_buy(self, user_id, prod, location, price):
        with self.conn:
            self.cursor.execute('INSERT OR IGNORE INTO to_buy (user_id, prod, location, price) VALUES (?, ?, ?, ?)', (user_id, prod, location, price))
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

    def add_product(self, user_id, prod, price):
        """Добавляем выбранный товар"""
        with self.conn:
            result = self.cursor.execute('UPDATE to_buy SET prod=?, price=? WHERE user_id=?', (prod, price, user_id))

    def add_location(self, user_id, location):
        """Добавляем выбранный район"""
        with self.conn:
            result = self.cursor.execute('UPDATE to_buy SET location=? WHERE user_id=?', (location, user_id))

    def list_pay(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT * FROM to_buy WHERE user_id=?', (user_id,)).fetchone()
            return result

    async def add_users_payment(self, user_id, name):
        """Добавляем в базу оплаты"""
        with self.conn:
            return self.cursor.execute("""INSERT INTO payment (user_id, name, role) VALUES (?, ?, ?)""", [user_id, name, 'admin' if user_id == int(ADMIN) else 'user'])

    async def update_label(self, label_id, user_id):
        with self.conn:
            return self.cursor.execute('UPDATE payment SET label=? WHERE user_id=?', (label_id, user_id))

    async def get_payment_status(self, user_id):
        with self.conn:
            return self.cursor.execute('SELECT status, label FROM payment WHERE user_id=?', (user_id,)).fetchall()

    async def update_payment_status(self, user_id):
        with self.conn:
            return self.cursor.execute('UPDATE payment SET status=?, count=count+1 WHERE user_id=?', (True, user_id))

    async def clear_payment_status(self, user_id):
        with self.conn:
            return self.cursor.execute('UPDATE payment SET status=FALSE, label=1 WHERE user_id=?', (user_id,))

    def get_location(self, area, amount):
        with self.conn:
            return self.cursor.execute('SELECT * FROM locations WHERE area=? and price=?', (area, amount)).fetchall()