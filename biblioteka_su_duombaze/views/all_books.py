from colorama import init, Fore, Style
from services.sukurti_lenteles import create_connection


db_kelias = r"D:\duombaze\data\biblioteka_su_duombaze\biblioteka.db"

conn = create_connection(db_kelias)

cursor = conn.cursor()


def list_all_books(conn):
    with conn:
        cursor.execute("SELECT ID, Pavadinimas, Autorius, Išleidimo_metai, Žanras, Kiekis FROM Knygos")
        rows = cursor.fetchall()
        
        if not rows:
            print(f"{Fore.CYAN} Knygų nėra.")
            f"{Style.RESET_ALL}"
            return
        for r in rows:
            print(
                f"{Fore.GREEN}ID: {Fore.CYAN}{r['id']:<32}"
                f"{Fore.GREEN} | Pavadinimas: {Fore.CYAN}{r['title']:<35}"
                f"{Fore.GREEN} | Autorius: {Fore.CYAN}{r['author']:<25}"
                f"{Fore.GREEN} | Išleidimo metai: {Fore.CYAN}{r['release_date']:<7}"
                f"{Fore.GREEN} | Žanras: {Fore.CYAN}{r['genre']:<20}"
                f"{Fore.GREEN} | Kiekis: {Fore.CYAN}{r['total_copies']:<5}"
                f"{Style.RESET_ALL}"
            )

