import sqlite3

class DataBase:
    def __init__(self, db_fie):
        self.conn = sqlite3.connect(db_fie)
        self.cursor = self.conn.cursor()

    def create_table(self):
        with self.conn:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS narkos (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                'user_id INTEGER'
                                'user_name TEXT'
                                'count_pay INTEGER'
                                'friends INTEGER'
                                'your_friend INTEGER'
                                'bonus INTEGER'
                                ')')
    def add_user(self, user_id, user_name, count_pay, friends, your_friend, bonus):
        with self.conn:
            self.cursor.execute('INSERT INTO narkos (user_id, user_name, count_pay, friends, your_friend, bonus) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, user_name, count_pay, friends, your_friend, bonus))
            self.conn.commit()

    def check_user(self, user_id):
        with self.conn:
            self.cursor.execute()


