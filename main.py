import sqlite3
from hashlib import sha256
from getpass import getpass


class Db_handler():
    def __init__(self):
        self.db = sqlite3.connect("inf.db")
        self.cursor = self.db.cursor()


class Data_handler(Db_handler):
    def __init__(self):
        super().__init__()

    def input(self):
        pass

    def delete(self):
        pass

    def set(self):
        pass


class Pwd_handler(Db_handler):
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
        pwd = getpass("\nI detected that you have no password here, "
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

    def inputpwd(self):
        pwd = getpass("\nEnter your code-word: ")
        correct = self._check(pwd)
        while not correct:
            pwd = getpass("Wrong! Enter again: ")
            correct = self._check(pwd)

    def _check(self, pwd):
        hashed_pwd = sha256(pwd.encode("utf-8")).hexdigest()
        self.cursor.execute(f"SELECT pwd FROM keys WHERE pwd = '{hashed_pwd}'")
        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def set(self):
        pass


def main():
    print("Nice to meet you here bro :)")
    pwd_handler = Pwd_handler()
    pwd_handler.inputpwd()
    print("Access to database granted :)")


if __name__ == '__main__':
    main()
