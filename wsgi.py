from flask import Flask
import psycopg2

application = Flask(__name__)

def db_connect:
    myConnection = psycopg2.connect(host="10.129.13.10", user="test", password="test123", dbname="sampledb")
    ver = myConnection.server_version
    myConnection.close()
    return "Zażółć gęślą jaźń! " + str(ver)

@application.route("/")
def hello():
    return db_connect()

if __name__ == "__main__":
    application.run()
