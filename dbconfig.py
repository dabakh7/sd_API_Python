
import requests
import json
import mysql.connector
import random

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dabakh7.",
    database = "JSONPlaceholder"
)

mycursor = mydb.cursor()


