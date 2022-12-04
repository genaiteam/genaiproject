from flask import Flask
import psycopg2


DB_HOST = 'db' # this will be the name of the service in the docker-compose file
DB_NAME = 'my_database'
DB_USER = 'postgres'
DB_PASSWORD = 'my_password'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
