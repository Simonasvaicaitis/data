import sqlite3


# def create_connection(db_file):
#     """Create a database connection to the SQLite database specified by db_file."""
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file) # Greitkelis (tarp programos ir duomenų bazės)
#         print(f"Connected to database: {db_file}")
#     except sqlite3.Error as e:
#         print(f"Error connecting to database: {e}")
#     return conn

# db_kelias = r"Data\duombaze.db"

# conn = create_connection(db_kelias)

# # create cursor
# cursor = conn.cursor() # tarsi automobilis, kuris gali vykdyti SQL komandas

# cursor.execute('''CREATE TABLE IF NOT EXISTS
#                 users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# conn.commit() # vaziuok i duombaze ir sukurk lentele

# name = input("Enter your name: ") # Justas"; Drop Table Users
# age = int(input("Enter your age: "))
# # Insert sample data
# # cursor.execute(f'Insert into Users (name, age) Values("{name}", "{age}")') # Justas"; Drop Table Users;
# # cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
# # cursor.execute("INSERT INTO users (name, age) VALUES (:vardas, :amzius)", {'amzius': age,'vardas': name}) # Naudojant žodyną, kad būtų saugiau nuo SQL injekcijų

# with conn:
#     cursor.execute("INSERT INTO users (name, age) VALUES (:vardas, :amzius)", {'amzius': age,'vardas': name}) # Naudojant žodyną, kad būtų saugiau nuo SQL injekcijų
#     input("Paspausk Enter, kad įrašas būtų pridėtas...") # Palauk, kol vartotojas paspaus Enter
# # galima isivaizduoti, kad pabaigus with conn atitraukima yra padaroma conn.commit() (taip pat dalinai yra padaroma ir conn.close())
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()  # Gauk visus įrašus iš lentelės
# print(rows) # rows yra sarašo pavidalu, kuriame yra visi įrašai kaip tuples
# for row in rows:
#     print(row)  # Spausdink kiekvieną įrašą
#     print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
# # Close the connection
# conn.close()  # Uždaryk duomenų bazės ryšį






























def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file) # Greitkelis (tarp programos ir duomenų bazės)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

db_kelias = r"D:\duombaze\data\duombaze.db"

conn = create_connection(db_kelias)
cursor = conn.cursor()


# # 1.Išrinkite visus duomenis iš stulpelių “VARDAS”,”PAVARDĖ”, “PAREIGOS” - lentelėje “DARBUOTOJAI”.

# def vard_pavard_pareig():
#     cursor.execute("Select VARDAS,PAVARDE,PAREIGOS from DARBUOTOJAS")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# vard_pavard_pareig()

# 1.Išrinkite skirtingas reikšmes iš stulpelio SKYRIUS_PAVADINIMAS - lentelėje “DARBUOTOJAI”.

# def skirtingos_reiksmes():
#     cursor.execute("Select distinct(SKYRIUS_PAVADINIMAS) From Darbuotojas")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# skirtingos_reiksmes()

# 1.Išrinkite visus duomenis apie darbuotojus, kurių gimimo data - 1986-09-19

# def info_pagal_data():
#     cursor.execute("Select * from DARBUOTOJAS Where GIMIMOMETAI = '1986-09-19'")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# info_pagal_data()

# 1.Išrinkite duomenis (vardą ir pavardę) apie programuotojus iš Java skyriaus

# def vardas_pavarde_is_java():
#     cursor.execute("Select VARDAS,PAVARDE FROM DARBUOTOJAS WHERE SKYRIUS_PAVADINIMAS = 'Java'")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# vardas_pavarde_is_java()

# 1.Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami visus reikiamus laukus (asmens_kodas, vardą, pavardę, gimimo metus, pareigas, skyriaus pavadinimą).

# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name,))

# def naujas_darbuotojas():
#     cursor.execute('INSERT INTO DARBUOTOJAS (ASMENSKODAS,VARDAS,PAVARDE,DIRBANUO,GIMIMOMETAI,PAREIGOS,SKYRIUS_PAVADINIMAS,PROJEKTAS_ID,DEPARTAMENTAS_ID) VALUES (38526588469,"Simas","Simaitis","2015-05-05","1999-09-09","Programuotojas","Java",2,3)')
#     conn.commit()

# naujas_darbuotojas()

# 1.Ištrinkite lentelės “DARBUOTOJAI” įrašą, kurio gimimo data yra tokia, kurią jūs sukūrėte.

# def istrint_pagal_data():
#     cursor.execute("DELETE FROM DARBUOTOJAS WHERE GIMIMOMETAI = '1999-09-09'")
#     conn.commit()

# istrint_pagal_data()

# 1.Suskaičiuokite, kiek įmonėje dirba Testuotojų.

# def kiek_testuotoju():
#     cursor.execute("SELECT COUNT(*) FROM DARBUOTOJAS WHERE Pareigos = 'Testuotojas'")
#     rows = cursor.fetchall()
#     print(rows)

# kiek_testuotoju()

# conn.close()











# −1.Išrinkite duomenis apie darbuotoją (asmens kodą, vardą ir pavarde) iš lentelės DARBUOTOJAS kurie būtų gimę 1988m liepos 20d.

# def ivestis():
#     return input("Iveskite metus (YYYY-MM-DD): ")

# def isrinkt_duomenis():
#     cursor.execute(f"SELECT ASMENSKODAS,VARDAS,PAVARDE FROM Darbuotojas WHERE GIMIMOMETAI = '{ivestis()}'")
#     rows = cursor.fetchall()
#     if not rows:
#         print("Nera darbuotoju tokia gimimo data.")
#     else:
#         for row in rows:
#             print(row)
    
# isrinkt_duomenis()



# −2.Išrinkite visus duomenis apie darbuotojus  iš lentelės DARBUOTOJAS, kurie yra gimę iki 1988m liepos 29d

# def ivestis():
#     return input("Iveskite metus (YYYY-MM-DD): ")

# def isrinkti():
#     with conn:
#         cursor.execute(f"SELECT * FROM Darbuotojas WHERE GIMIMOMETAI < '{ivestis()}'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Klaida")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()


# −3.Išrinkite duomenis apie darbuotojus(dirba nuo kada ir gimimo metus) iš lentelės DARBUOTOJAS, kurie būtų įsidarbinę nuo 2009m spalio 30d iki 2012m lapkričio 11d.

# def data_nuo():
#     return input("Iveskite pradzios data (YYYY-MM-DD): ")

# def data_iki():
#     return input("Iveskite pabaigos data (YYYY-MM-DD): ")

# def isrinkti():
#     with conn:
#         cursor.execute(f"SELECT DIRBANUO,GIMIMOMETAI FROM DARBUOTOJAS WHERE DIRBANUO BETWEEN '{data_nuo()}' AND '{data_iki()}'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)


# isrinkti()

# −4.Išrinkite duomenis apie darbuotojus (vardą, Skyrių ir Projekto ID)  iš lentelės DARBUOTOJAS kurie dirba 2 ir 3 projektuose. (Panaudoti IN operatorių).

# def isrinkt_duomenis():
#     with conn:
#         cursor.execute("SELECT VARDAS,SKYRIUS_PAVADINIMAS,PROJEKTAS_ID FROM DARBUOTOJAS WHERE PROJEKTAS_ID IN (2,3)")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkt_duomenis()



# −5.Išrinkite duomenis (vardą, pavarde ir asmens kodą) apie visas moteris iš lentelės DARBUOTOJAS (panaudojant operatorių LIKE).

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS,PAVARDE,ASMENSKODAS FROM DARBUOTOJAS WHERE VARDAS LIKE '%a'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()

# −6.Išrinkite visus duomenis apie visus darbuotojus iš lentelės DARBUOTOJAS,  kurie yra gimę 12 diena (panaudojant operatorių LIKE).

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT * FROM DARBUOTOJAS WHERE GIMIMOMETAI LIKE '%12'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()

# −7.išrinkite visus projektus iš lentelės PROJEKTAS kad projekto pavadinime 3 raidė būtų ‘u’.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT PAVADINIMAS FROM PROJEKTAS WHERE PAVADINIMAS LIKE '__u%'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()



# −8.Išrinkite visus darbuotojus iš lentelės DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT * FROM DARBUOTOJAS WHERE PAREIGOS IS NULL")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()


# −9.Išrinkite duomenis apie darbuotoją (vardą, pavardę, nuo kada dirba ir pareigas) kad tenkintų sąlygas: (dirba nuo 2011-02-12 ir jų pareigos yra Programuotojai).

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS,PAVARDE,DIRBANUO,PAREIGOS FROM DARBUOTOJAS WHERE DIRBANUO > '2011-02-11' AND PAREIGOS LIKE 'Programuot%'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()



# −10.Išrinkite duomenis apie darbuotojus (vardą, pavardę, skyriaus pavadinimą ir projekto ID)  iš lentelės DARBUOTOJAS su sąlyga, kad jie butų iš Java skyriaus arba 1 projekto.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS,PAVARDE,SKYRIUS_PAVADINIMAS,PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_PAVADINIMAS = 'Java' OR PROJEKTAS_ID = '1'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()



# −11.Išrinkite visus darbuotojų vardus išskyrus tuos, kurių vardai prasideda raide ‘S’ .

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS FROM DARBUOTOJAS WHERE VARDAS NOT LIKE 'S%'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()


# −12.Išrinkite duomenis ( vardą, dirba nuo kada ir gimimo metus)  iš lentelės “DARBUOTOJAS”, 
# apie visus darbuotojus tik ne tuos, kurie įsidarbino  nuo 2009m spalio 30d iki 2012m lapkričio 11d.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS,DIRBANUO,GIMIMOMETAI FROM DARBUOTOJAS WHERE DIRBANUO NOT BETWEEN '2009-10-30' AND '2012-11-11'")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()



# −13.Išrinkite duomenis apie darbuotojus (vardą, pavardę ir gimimo metus) iš lentelės DARBUOTOJAS ir išrikiuokite visus duomenis nuo seniausio žmogaus iki jauniausio.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS,PAVARDE,GIMIMOMETAI FROM DARBUOTOJAS ORDER BY GIMIMOMETAI ASC")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()



# −14.Išrinkite duomenis apie darbuotojus (vardą, pavardę ir gimimo metus) iš lentelės DARBUOTOJAS ir išrikiuokite visus duomenis nuo jauniausio žmogaus iki seniausio.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT VARDAS,PAVARDE,GIMIMOMETAI FROM DARBUOTOJAS ORDER BY GIMIMOMETAI DESC")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()


# -- Select PAREIGOS, max(GIMIMOMETAI) From DARBUOTOJAS Group By PAREIGOS -- SU GROUP BY GRIEŽTAI NEGALIMA NAUDOTI TU Stulpeliu, kuriu nera prie GROUP BY arba nera
# -- ideti i agregacijos funkcija (kaip max,min,sum,avg)
# -- Select PAREIGOS, max(GIMIMOMETAI), count(Pareigos) From DARBUOTOJAS Group By PAREIGOS
# -- Select Max(Vardas), PAVARDE, Max(GimimoMetai) From DARBUOTOJAS
# Select PAREIGOS, SKYRIUS_PAVADINIMAS, max(GIMIMOMETAI), count(Pareigos) From DARBUOTOJAS Where Pareigos is not null Group By PAREIGOS, SKYRIUS_PAVADINIMAS
# HAVING count(pareigos) > 3
# -- having identiškas Where tik jis veikia jau grupių viduje, ir naudojas tik po group by





# −15.Išrinkite iš lentelės DARBUOTOJAS didžiausią ir mažiausią gimimo datą.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT MAX(GIMIMOMETAI), MIN(GIMIMOMETAI) FROM DARBUOTOJAS")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for row in rows:
#                 print(row)

# isrinkti()


# −16.Išrinkite duomenis apie projektą ir kiek tame projekte yra priskirta žmonių iš lentelės DARBUOTOJAS (projekto numeris ir skaičius kiek dalyvauja žmonių).

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT PROJEKTAS_ID, COUNT(*) FROM DARBUOTOJAS GROUP BY PROJEKTAS_ID")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for projektas_id, skaicius in rows:
#                 print(f"Projekto id: {projektas_id}. Zmoniu: {skaicius}.")

# isrinkti()


# −17.Išrinkite duomenis (projekto numeris, pareigos, skaičius) iš lentelės DARBUOTOJAS kiek dirba programuotojų kiekvienam projekte.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT PROJEKTAS_ID, PAREIGOS, COUNT(*) FROM DARBUOTOJAS WHERE PAREIGOS LIKE 'Programuot%' GROUP BY PROJEKTAS_ID")
#         rows = cursor.fetchall()
#         if not rows:
#             print("Duomenu nerasta.")
#         else:
#             for projektas_id, pareigos, skaicius in rows:
#                 print(f"Projekto ID: {projektas_id}. Pareigos: {pareigos}. #Darbuotoju skaicius: {skaicius}.")

# isrinkti()





# −18.#17 punkto užklausą pataisykite taip, kad rodytų tik tuos projektus, kur dirba bent 2 darbuotojai.

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT PROJEKTAS_ID, PAREIGOS, COUNT(PAREIGOS) FROM DARBUOTOJAS WHERE PAREIGOS LIKE 'Programuot%' GROUP BY PROJEKTAS_ID, PAREIGOS HAVING COUNT(PAREIGOS)>1")
#         rows = cursor.fetchall()
#         return rows

# print(isrinkti())
# conn.close()

# Rasti, kuris darbuotojas dirba ilgiausiai metu ir išvesti darbo trukmę metais ilgiausiai dirbančio darbuotojo.

# def isrinkti():
#     with conn:
#         cursor.execute("")
#         rows = cursor.fetchall()
#         return rows

# print(isrinkti())
# conn.close()

# Select PAREIGOS, AVG(amzius) From 
# (Select *, ('2025-06-17' - GIMIMOMETAI) as amzius From DARBUOTOJAS)
# Group By PAREIGOS




# -- Select * From DARBUOTOJAS JOIN PROJEKTAS ON PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID
# -- Select * From DARBUOTOJAS JOIN DEPARTAMENTAS on DEPARTAMENTAS.ID = DARBUOTOJAS.DEPARTAMENTAS_ID 
# Where PAREIGOS Like 'Program%' and PAVADINIMAS = 'IT' and DARBUOTOJAS.SKYRIUS_PAVADINIMAS = 'Java'
# -- Select * From DARBUOTOJAS 
# -- Join PROJEKTAS ON PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID 
# -- Join DEPARTAMENTAS on DEPARTAMENTAS.ID = DARBUOTOJAS.DEPARTAMENTAS_ID

# Select d1.*, d2.Vardas as Vadovo_Vardas, d2.PAVARDE as Vadovo_Pavarde
# From DARBUOTOJAS as d1 
# Join SKYRIUS on d1.SKYRIUS_PAVADINIMAS = SKYRIUS.PAVADINIMAS
# Join DARBUOTOJAS as d2 ON SKYRIUS.VADOVAS_ASMENSKODAS = d2.ASMENSKODAS


# −Išrinkite darbuotojų vardus, pavardes ir projektų pavadinimus, kuriuose jie dirba

# def isrinkti():
#     with conn:
#         cursor.execute("SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDE, PROJEKTAS.PAVADINIMAS FROM DARBUOTOJAS JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)



# −Išrinkite skyrių pavadinimus ir vadovų vardus bei pavardes (iš skyrių lentelės)

# def isrinkti():
#     with conn:
#         cursor.execute("""SELECT SKYRIUS.PAVADINIMAS, DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDE FROM DARBUOTOJAS
#         JOIN SKYRIUS ON DARBUOTOJAS.ASMENSKODAS = SKYRIUS.VADOVAS_ASMENSKODAS""")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)



# −Išrinkite darbuotojų vardus, pavardes, skyrių pavadinimus ir projektų pavadinimus, kuriuose jie dirba

# def isrinkti():
#     with conn:
#         cursor.execute("""SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDE, DARBUOTOJAS.SKYRIUS_PAVADINIMAS, PROJEKTAS.PAVADINIMAS
#                        FROM DARBUOTOJAS JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID""")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)




# −Išrinkite darbuotojų vardus, pavardes ir skyrius ir projekto pavadinimą, kuriuose jie dirba, kurie yra įsidarbinę nuo 2010m iki 2012m

# def isrinkti():
#     with conn:
#         cursor.execute("""SELECT DARBUOTOJAS.VARDAS, DARBUOTOJAS.PAVARDE, DARBUOTOJAS.SKYRIUS_PAVADINIMAS, PROJEKTAS.PAVADINIMAS
#                        FROM DARBUOTOJAS JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID WHERE DIRBANUO BETWEEN '2010-01-01' AND '2012-12-31'""")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)


# −Išrinkite skyrių pavadinimus ir darbuotojų skaičių kiekviename skyriuje

# def isrinkti():
#     with conn:
#         cursor.execute("""SELECT SKYRIUS.PAVADINIMAS, COUNT(*) AS SKAICIUS
#                        FROM DARBUOTOJAS JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_PAVADINIMAS = SKYRIUS.PAVADINIMAS GROUP BY SKYRIUS.PAVADINIMAS""")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)




# −Išrinkite visus darbuotojus, kurių pavardė prasideda 'S' raide, ir jų projektų pavadinimus


# def isrinkti():
#     with conn:
#         cursor.execute("""SELECT DARBUOTOJAS.PAVARDE, PROJEKTAS.PAVADINIMAS
#                        FROM DARBUOTOJAS JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
#                        WHERE DARBUOTOJAS.PAVARDE LIKE 'S%' ORDER BY DARBUOTOJAS.PAVARDE""")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)



# −Išrinkite darbuotojų vardus ir pavardes bei jų vadovų vardus ir pavardes

# def isrinkti():
#     with conn:
#         cursor.execute("""Select d1.*, d2.Vardas as Vadovo_Vardas, d2.PAVARDE as Vadovo_Pavarde
#                         From DARBUOTOJAS as d1 
#                         Join SKYRIUS on d1.SKYRIUS_PAVADINIMAS = SKYRIUS.PAVADINIMAS
#                         Join DARBUOTOJAS as d2 ON SKYRIUS.VADOVAS_ASMENSKODAS = d2.ASMENSKODAS""")
#         rows = cursor.fetchall()
#         return rows

# rows = isrinkti()
# for row in rows:
#     print(row)
