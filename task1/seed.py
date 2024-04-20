import psycopg2
from faker import Faker
import random

fake = Faker()


def connect_to_database():
    try:
      
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="567234",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        return None


def insert_fake_data():
    conn = connect_to_database()
    if conn is None:
        return
    cursor = conn.cursor()


    status_values = [('new',), ('in progress',), ('completed',)]
    for status in status_values:
        cursor.execute("SELECT * FROM status WHERE name = %s", (status,))
        if cursor.fetchone() is None: 
            cursor.execute("INSERT INTO status (name) VALUES (%s)", status)

  
    for _ in range(100):
        fullname = fake.name()
        email = fake.email()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

    
    cursor.execute("SELECT id FROM users")
    user_ids = [id[0] for id in cursor.fetchall()]
    cursor.execute("SELECT id FROM status")
    status_ids = [id[0] for id in cursor.fetchall()]

    for _ in range(20):
        title = fake.sentence()
        description = fake.text()
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                       (title, description, status_id, user_id))


    conn.commit()
    cursor.close()
    conn.close()
    print("Fake data successfully inserted into the database.")


if __name__ == "__main__":
    insert_fake_data()