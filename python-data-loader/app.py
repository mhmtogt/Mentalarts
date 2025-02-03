import psycopg2
from psycopg2 import OperationalError
import time
from pymongo import MongoClient
import redis

# PostgreSQL Bağlantısı
def connect_postgres():
    while True:
        try:
            pg_conn = psycopg2.connect(
                dbname="testdb",
                user="user",
                password="password",
                host="postgres_db"
            )
            return pg_conn
        except OperationalError:
            print("[!] PostgreSQL hazır değil, bekleniyor...")
            time.sleep(5)

pg_conn = connect_postgres()
pg_cursor = pg_conn.cursor()
pg_cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, data TEXT);")
pg_cursor.execute("INSERT INTO test (data) VALUES ('Hello from PostgreSQL!');")
pg_conn.commit()
pg_cursor.close()
pg_conn.close()
print("[✔] PostgreSQL'e veri eklendi.")

# MongoDB Bağlantısı
mongo_client = MongoClient("mongodb://mongo_db:27017/")
mongo_db = mongo_client["testdb"]
mongo_collection = mongo_db["test_collection"]
mongo_collection.insert_one({"message": "Hello from MongoDB!"})
print("[✔] MongoDB'ye veri eklendi.")

# Redis Bağlantısı
redis_client = redis.StrictRedis(host="redis_db", port=6379, decode_responses=True)
redis_client.set("message", "Hello from Redis!")
print("[✔] Redis'e veri eklendi.")
