from flask import Flask
from datetime import datetime
import psycopg2

application = Flask(__name__)

def db_connect():
    conn = psycopg2.connect(host="10.129.13.10", user="test", password="test123", dbname="sampledb")
    ver = conn.server_version
#    cursor = conn.cursor()
#    cursor.execute('SELECT VERSION()')
#    row = cursor.fetchone()
#    cursor.close()
    conn.close()
    return str(ver)

def db_connect_2():
    conn = psycopg2.connect(host="172.30.130.175", user="test", password="test123", dbname="sampledb")
    ver = conn.server_version
#    cursor = conn.cursor()
#    cursor.execute('SELECT VERSION()')
#    row = cursor.fetchone()
#    cursor.close()
    conn.close()
    return str(ver)

def db_connect_3():
    conn = psycopg2.connect(host="ip-10-0-146-246.ec2.internal", user="test", password="test123", dbname="sampledb")
    ver = conn.server_version
#    cursor = conn.cursor()
#    cursor.execute('SELECT VERSION()')
#    row = cursor.fetchone()
#    cursor.close()
    conn.close()
    return str(ver)

@application.route("/")
def hello():
    return "Hey! Now it's " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@application.route("/version")
def version():
    return db_connect()

@application.route("/version2")
def version2():
    return db_connect_2()

@application.route("/version3")
def version3():
    return db_connect_3()

if __name__ == "__main__":
    application.run()
