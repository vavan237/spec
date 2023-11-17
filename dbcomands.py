import sqlite3
from typing import List, Any


class Sqligther():

    def __init__(self, database_file):
        # подключаем базу
        self.connection = sqlite3.connect('spec.db')
        self.cursor = self.connection.cursor()

    def get_all_clients(self):
        with self.connection:
            return self.cursor.execute("SELECT client_id, name, street, house_num, room_num, price, balance FROM clients")


    def get_all_streets(self):
        with self.connection:
            return self.cursor.execute('select distinct street from clients')

    def get_all_houses(self):
        with self.connection:
            return self.cursor.execute("select house_num from clients")

    def get_all_rooms(self):
        with self.connection:
            return self.cursor.execute("select room_num from clients")

    def get_debtors(self, num):
        res = []
        self.num = num
        with self.connection:
            cursor = self.cursor.execute(f"select * from clients where balance <= {int('-' + num)}")
            for i in cursor:
                res.append(i)
        return res

    def get_wrong_ls(self):
        res = []
        with self.connection:
            cursor = self.cursor.execute(f'select client_id, price, name from clients where {len("client_id")} <> 10')
            for i in cursor:
                res.append(i)
        return res

    def get_name_pr_cli(self, adres, num, room):
        res = []
        self.adres = adres
        self.num = num
        self.room = room
        with self.connection:
            cursor = self.cursor.execute(f"select name, price, client_id, balance from clients where street == ? and house_num == ?  and room_num == ?", (adres, num, room))
            for i in cursor:
                res.append(i)

        return res

    def add_new_cli(self, name, street, house, room, price):
        self.name = name
        self.street = street
        self.house = house
        self.room = room
        self.price = price
        with self.connection:
            cursor = self.cursor.execute(f"insert into clients(name, street, house_num, room_num, price) values(?, ?, ?, ?, ?)", (name, street, house, room, price))


    def get_all_orders(self):
        res = []
        res1 = []
        res2 =[]
        with self.connection:
            cursor = self.cursor.execute(f'select order_data, adres, knock, not_call, not_open, call_button, master, done, comment from orders')
            for i in cursor:
                res.append(i)
        for r in res:
            res1.append([k for k in r])
        for k in range(len(res1)):
            for m in range(len(res1[k])):
                if res1[k][m] in (0, 'False', None):
                    res1[k][m] = '-'
                elif res1[k][m] == 'True':
                    res1[k][m] = '+'
        return res1

    def get_house_all_rooms(self, street, house):
        self.street=street
        self.house=house
        res = []
        with self.connection:
            cursor = self.cursor.execute(f'select room_num from clients where street == ? and house_num == ?',(street, house))
            for i in cursor:
                res += ([j for j in i])
        return res

    def get_street_all_houses(self, houses):
        self.houses = houses
        res = []
        with self.connection:
            cursor = self.cursor.execute(f'select house_num from clients where street == ? order by house_num', [houses])
            for i in cursor:
                res += ([j for j in i])
        return res

    def get_house_clients(self, street, house):
        self.street = street
        self.house = house
        res = []
        with self.connection:
            cursor = self.cursor.execute(f'select client_id, name, street, house_num, room_num, price, balance FROM clients where street == ? and house_num == ?',
                                         (street, house))
            for i in cursor:
                res += [j for j in i]
        return res

    def add_tarif(self):
        with self.connection:
            cursor = self.cursor.execute(f'update clients set balance = balance - price')