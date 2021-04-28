#! /usr/bin/python

import mysql.connector as mc
from mysql.connector import errorcode
from datetime import datetime


class DB:
    def __init__(self):
        try:
            mydb = mc.connect(
                host="10.0.0.126",
                user="sqluser",
                password="essqueel",
                charset="utf8mb4"
            )

            cursor = mydb.cursor()

        except mc.Error as e:
            print("{}:".format(e.errno) + e.msg)
