
import os
import sqlite3

class Database:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("table.db")
            if self.connection:
                self.cursor = self.connection.cursor()
                self.cursor.execute("CREATE TABLE IF NOT EXISTS emp_salary (id INTEGER PRIMARY KEY, First text, last text, Mobile integer, age integer)")

        except:
            print("Error while connecting to MySQL")

    # read the row of the table one by one keeps memory low
    def fetch_one_by_one(self):
        self.cursor.execute('select * from emp_salary;')
        single_data = self.cursor.fetchone()
        yield single_data
        while single_data != None:
            single_data = self.cursor.fetchone()
            if single_data != None:
                yield single_data

if __name__ == "__main__":
    print(Database().fetch_one_by_one().__next__())