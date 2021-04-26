#! /usr/bin/python

import mysql.connector as mc
from mysql.connector import errorcode
from datetime import datetime


class DB:
    def db_conn(self):
        try:
            mydb = mc.connect(
                host="db5002105041.hosting-data.io",
                user="dbu1239445",
                password="$#Cl0th3s)=",
                charset="utf8mb4"
            )

            cursor = mydb.cursor()
            return cursor

        except mc.Error as e:
            print("{}:".format(e.errno) + e.msg)
