# •Sukurti programą, kuri:
# •Sukurtų duomenų bazę
# •Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
# •Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80)
# •Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
# •Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# •Ištrintų paskaitą, kurios dėstytojas – „Tomas“
# •Atspausdintų visas paskaitas (visą lentelę)



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

db_kelias = r"D:\duombaze\data\duomenu_baze2.db"

conn = create_connection(db_kelias)

cursor = conn.cursor()

# #  •Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme

# # def lenteles_kurimas():
# #     cursor.execute('''CREATE TABLE IF NOT EXISTS
# #                    Paskaitos (Pavadinimas TEXT PRIMARY KEY, Destytojas TEXT, Trukme INTEGER)''')
# #     conn.commit()

# # lenteles_kurimas()

# # # •Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80)

# # def paskaitu_kurimas(pavadinimas, destytojas, trukme):
# #     cursor.execute(f"INSERT INTO Paskaitos (Pavadinimas, Destytojas, Trukme) VALUES(?,?,?)",(pavadinimas, destytojas, trukme))
# #     conn.commit()

# # paskaita1 = paskaitu_kurimas("Vadyba", "Domantas", 40)
# # paskaita2 = paskaitu_kurimas("Python", "Donatas", 80)
# # paskaita3 = paskaitu_kurimas("Java", "Tomas", 80)

# # •Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50

# # def pagal_trukme():
# #     cursor.execute("SELECT * FROM Paskaitos WHERE Trukme >= 50")
# #     rows = cursor.fetchall()
# #     for row in rows:
# #         print(row)

# # pagal_trukme()


# # •Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“

# # def atnaujinti_pavadinima():
# #     cursor.execute("UPDATE Paskaitos SET Pavadinimas = 'Python programavimas' WHERE Pavadinimas = 'Python'")
# #     conn.commit()

# # atnaujinti_pavadinima()

# # •Ištrintų paskaitą, kurios dėstytojas – „Tomas“

# # def istrinti_irasa():
# #     cursor.execute("DELETE FROM Paskaitos WHERE Destytojas = 'Tomas'")
# #     conn.commit()

# # istrinti_irasa()

# # •Atspausdintų visas paskaitas (visą lentelę)

# def spausdint_viska():
#     cursor.execute("SELECT * FROM Paskaitos")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# spausdint_viska()
