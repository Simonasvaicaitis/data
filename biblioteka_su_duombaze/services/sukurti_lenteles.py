import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

db_kelias = r"D:\duombaze\data\biblioteka_su_duombaze\biblioteka.db"

conn = create_connection(db_kelias)

cursor = conn.cursor()


def sukurti_knygos_lentele(conn):
    with conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Knygos (
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Pavadinimas TEXT NOT NULL,
                       Autorius TEXT NOT NULL,
                       Išleidimo_metai DATE NOT NULL,
                       Žanras TEXT NOT NULL,
                       Kiekis INTEGER NOT NULL,
                       CREATED_ON DATETIME,
                       CREATED_BY TEXT,
                       MODIFIED_ON DATETIME,
                       MODIFIED_BY TEXT,
                       DELETED BOOLEAN)""")
        conn.commit()

def sukurt_naudotojas_lentele(conn):
    with conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Naudotojas (
                       Naudotojo_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Vardas TEXT NOT NULL,
                       Pavardė TEXT NOT NULL,
                       CREATED_ON DATETIME,
                       CREATED_BY TEXT,
                       MODIFIED_ON DATETIME,
                       MODIFIED_BY TEXT,
                       DELETED BOOLEAN)""")
        conn.commit()

def sukurt_paskolintos_knygos_lentele(conn):
    with conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Paskolintos_knygos (
                       Knygos_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       Naudotojas_ID NOT NULL,
                       CREATED_ON DATETIME,
                       CREATED_BY TEXT,
                       MODIFIED_ON DATETIME,
                       MODIFIED_BY TEXT,
                       DELETED BOOLEAN)""")
        conn.commit()