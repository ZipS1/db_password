# HASHING EXAMPLE
#
# data = input('Enter plaintext data: ')
# output = sha256(data.encode('utf-8'))

import sqlite3
from hashlib import sha256
from getpass import getpass


class Db_handler():
    def __init__(self):
        pass

    def input(self):
        pwd = getpass("Enter your code-word: ")

    def delete(self):
        pass

    def set(self):
        pass


class Pwd_handler:
    """docstring for Pwd_handler"""
    def __init__(self):
        pass

    def _new(self):
        pass

    def input(self):
        pass

    def check(self):
        pass

    def set(self):
        pass


def setup():
    pwd_handler = Pwd_handler()
    db_handler = Db_handler()
    print("Nice to meet you here bro :)")


def main():
    setup()


if __name__ == '__main__':
    main()
