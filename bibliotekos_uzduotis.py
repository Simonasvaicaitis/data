# import sqlite3

# # Sukurti knygos klasę su bent 3-jomis sąvybėmis. Ir pamėginti leisti naudotojui atlikti 4 CRUD veiksmus.
 
# # Sukurti naują knygą ir įdėti ją į duomenų bazę, kaip įrašą
# # Ištrinti egzistuojančią knygą (pagal id)
# # Peržiūrėti duomenų bazėje esančių knygų sąrašą.
# # Atnaujinti egzistuojančią knygą pagal id (Šitą darykite paskutinį, kai prieš tai buve bus atlikti)

# class Book:
#     def __init__(self, title, author, data, genre):
#         self.title = title
#         self.author = author
#         self.release_date = data
#         self.genre = genre
    
#     def __str__(self):
#         return(f"{self.title} {self.author} {self.release_date} {self.genre}")


# def create_connection(db_file):
#     """Create a database connection to the SQLite database specified by db_file."""
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(f"Connected to database: {db_file}")
#     except sqlite3.Error as e:
#         print(f"Error connecting to database: {e}")
#     return conn

# def sukurt_lentele():
#     cursor.execute('''CREATE TABLE IF NOT EXISTS
#                 Biblioteka (Pavadinimas TEXT PRIMARY KEY, Autorius TEXT, Metai INTEGER, Žanras TEXT)''')
#     conn.commit()
#     print("Lentele sukurta.")

# def pridet_knyga():
#     with conn:
#         cursor.execute(f"INSERT INTO Biblioteka (Pavadinimas,Autorius,Metai,Žanras) VALUES (:)")

# cursor.execute("INSERT INTO users (name, age) VALUES (:vardas, :amzius)", {'amzius': age,'vardas': name}) # Naudojant žodyną, kad būtų saugiau nuo SQL injekcijų


# db_kelias = r"D:\duombaze\data\bibliotekos_duombaze.db"

# conn = create_connection(db_kelias)

# cursor = conn.cursor()

# sukurt_lentele()