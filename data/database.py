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
            self.cursor.execute('CREATE TABLE IF NOT EXISTS locations (id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT, price INTEGER, area TEXT, foto1 TEXT)')

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

    def prof_friends(self, user_id):
        with self.conn:
            result = self.cursor.execute('SELECT COUNT(friends) FROM refers WHERE user_id = ?', (user_id,)).fetchone()
            return result[0] if result else 0

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

    def get_info(self, user_id):
        with self.conn:
            return self.cursor.execute('SELECT * FROM narkos WHERE user_id=?', (user_id,)).fetchall()

    def add_loc(self, product, price, area, foto1):
        """Добавление новой локации в таблицу"""
        with self.conn:
            self.cursor.execute('''INSERT INTO locations (product, price, area, foto1) VALUES (?, ?, ?, ?)''', (product, price, area, foto1))

    def count_products(self, product):
        """Определение количества товаров в таблице"""
        with self.conn:
            self.cursor.execute("SELECT COUNT(*) FROM locations WHERE product=?", (product,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Возвращаем количество товаров
            else:
                return 0  # Если таблица пуста, возвращаем 0

    def count_pays(self, user_id):
        """Определение количества продаж в профиле"""
        with self.conn:
            self.cursor.execute("SELECT count FROM payment WHERE user_id=?", (user_id,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Возвращаем количество товаров
            else:
                return 0  # Если таблица пуста, возвращаем 0

    async def clear_payment_bd(self, user_id):
        with self.conn:
            return self.cursor.execute('UPDATE to_buy SET prod=NULL, location=NULL, price=NULL WHERE user_id=?', (user_id,))

    def check_product_availability(self, area, product):
        """Проверяет наличие товара в указанном районе."""
        with self.conn:
            self.cursor.execute("SELECT COUNT(*) FROM locations WHERE area=? AND product=?", (area, product))
            result = self.cursor.fetchone()
            if result:
                return result[0] > 0  # Возвращаем True, если товар есть в наличии, иначе False
            else:
                return False

    def take_bonus(self, user_id):
        # Получаем всех друзей пользователя user_id
        with self.conn:
            friends = self.cursor.execute('SELECT friends FROM refers WHERE user_id = ?', (user_id,)).fetchall()
        for friend_id in friends:
            friend_id = friend_id[0]  # Распаковываем кортеж
            with self.conn:
                # Получаем значение count для друга
                count = self.cursor.execute('SELECT count FROM payment WHERE user_id = ?', (friend_id,)).fetchone()

            # Если count равно 1, начисляем бонус пользователю user_id
            if count == 1:
                with self.conn:
                    # Начисляем бонус пользователю user_id
                    self.cursor.execute('UPDATE narkos SET bonus = bonus + 1 WHERE user_id = ?', (user_id,))

    def check_bonus(self, user_id):
        with self.conn:
            bonus = self.cursor.execute('SELECT bonus FROM narkos WHERE user_id = ?', (user_id,)).fetchone()
            return bonus[0]


