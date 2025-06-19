import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file) # Greitkelis (tarp programos ir duomenų bazės)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

db_kelias = r"D:\duombaze\data\sukurt_duombaze.db"

conn = create_connection(db_kelias)
cursor = conn.cursor()


# •Sukurkite naudotojų lentelę su stulpeliais (id,name,last_name)
# •Padarykite idprimary key

def sukurt_lentele(conn):
    with conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Naudotojai (
                ID INTEGER PRIMARY KEY NOT NULL,
                Name CHAR(30) NOT NULL,
                Last_name CHAR(30) NOT NULL)""")
    
# sukurt_lentele(conn)


# •Pridėkite naują stulpelį į šią lentelę pavadinimu age

def pridet_age(conn):
    with conn:
        cursor.execute("""ALTER TABLE Naudotojai ADD Age INT""")
    
# pridet_age(conn)



# •Pridėkite stulpelį gimimo data (datetime)

def pridet_bday(conn):
    with conn:
        cursor.execute("""ALTER TABLE Naudotojai ADD Gimimo_data DATE""")

# pridet_bday(conn)



# •Ištrinkite stulpelį gimimo data

def istrint_bday(conn):
    with conn:
        cursor.execute("""ALTER TABLE Naudotojai DROP Gimimo_data""")

# istrint_bday(conn)



# •Sukurkite antrą lentelę automobilis kuri turėtų pagaminimo datetime su Default reikšme dabartinė data
# (su bent trejais stulpeliais ir primary key (viskas vienoje užklausoje, be alter))

def sukurt_lentele2(conn):
    with conn:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Automobilis (
                       ID INTEGER PRIMARY KEY NOT NULL,
                       Pagaminimo_data DATETIME DEFAULT CURRENT_DATE,
                       Marke TEXT NOT NULL,
                       Modelis TEXT NOT NULL)""")

# sukurt_lentele2(conn)


# •Sukurti ryšį, kad naudotojas galėtų turėti daug automobilių, tai pasieksite sukurdami foreign key apribojimą.

def pridet_isrorini_rakta(conn):
    with conn:
        cursor.execute("""ALTER TABLE Automobilis
                       ADD COLUMN Vartotojo_ID INTEGER REFERENCES Naudotojai(ID)""")

# pridet_isrorini_rakta(conn)
