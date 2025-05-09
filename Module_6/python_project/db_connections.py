
import psycopg2

def connect_to_bank(vault_file):
    try:
        with open(vault_file, 'r') as file:
            username = file.readline().strip()
            password = file.readline().strip()

        conn = psycopg2.connect(
            dbname="bank",
            user=username,
            password=password,
            host="localhost",
            port="5432"
        )
        return conn
    except FileNotFoundError:
        print(f"❌ Vault file '{vault_file}' not found.")
    except Exception as e:
        print(f"❌ Error connecting to the database: {e}")
    return None
