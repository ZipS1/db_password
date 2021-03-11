import sqlite3
from hashlib import sha256
from getpass import getpass


class Handler():
    def __init__(self):
        self.db = sqlite3.connect("inf.db")
        self.cursor = self.db.cursor()


class Db_handler(Handler):
    def __init__(self):
        super().__init__()

    def input(self):
        pass

    def delete(self):
        pass

    def set(self):
        pass


class Pwd_handler(Handler):
    """docstring for Pwd_handler"""
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS keys (
            pwd TEXT
            )""")
        self.db.commit()
        self.cursor.execute("SELECT pwd FROM keys")
        if self.cursor.fetchone() is None:
            self._new()

    def _new(self):
        pwd = getpass("I detected that you have no password here, "
                      "enter yours: ")
        pwd_rpt = getpass("Confirm your new password: ")
        while not pwd == pwd_rpt:
            print("Your passwords do not match!")
            pwd = getpass("\nEnter password: ")
            pwd_rpt = getpass("Confirm your new password: ")

        hashed_pwd = sha256(pwd.encode("utf-8")).hexdigest()
        self.cursor.execute(f"INSERT INTO keys VALUES (?)", (hashed_pwd,))
        self.db.commit()
        print("Your password successfully recorded!")

    def input(self):
        pwd = getpass("Enter your code-word: ")

    def check(self):
        pass

    def set(self):
        pass


def setup():
    print("Nice to meet you here bro :)\n")
    pwd_handler = Pwd_handler()


def main():
    setup()


if __name__ == '__main__':
    main()
