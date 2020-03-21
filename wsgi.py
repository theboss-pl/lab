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

@application.route("/")
def hello():
    return "Hey! Now it's " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@application.route("/version")
def version():
    return db_connect()

if __name__ == "__main__":
    application.run()
