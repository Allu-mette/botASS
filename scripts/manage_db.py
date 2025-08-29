import sqlite3
import argparse
import os, sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from config import DB_PATH

def createTBase():
    """
    Create the table if not exists
    """

    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS tt_exercices 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    date TEXT NOT NULL, 
                    difficulty TEXT NOT NULL,
                    tokenCounts INT NOT NULL, 
                    content TEXT NOT NULL)""")

        conn.commit()

def clearBase():
    """
    Clear the table
    """

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM tt_exercices")
        cur.execute("DELETE FROM sqlite_sequence WHERE name='tt_exercices'")
        conn.commit()
        
def clearLast(n: int):
    """
    Clear the n last element of the table
    """

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        query = "DELETE FROM tt_exercices WHERE id IN (SELECT id FROM tt_exercices ORDER BY id DESC LIMIT ?)"
        value = (n,)
        cur.execute(query, value)
        conn.commit()
        


def showLast(n: int):
    """
    Show the n last element of the table  
    """
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        query = "SELECT * FROM tt_exercices ORDER BY id DESC LIMIT ?"
        value = (n,)
        cur.execute(query, value)

        rows = cur.fetchall()
        if rows :
            for row in rows:
                print(row)


parser = argparse.ArgumentParser(description="Database manager")

parser.add_argument(
    "action",
    choices=["create", "clear", "clearLast", "showLast"],
    help="Actions to do on the Database"
)
parser.add_argument(
    "-n",
    type=int,
    default=1,
    help="Nombre d'éléments pour showLast ou clearLast (défaut=1)"
)

args = parser.parse_args()

if args.action == "create":
    createTBase()
elif args.action == "clear":
    clearBase()
elif args.action == "clearLast":
    clearLast(args.n)
elif args.action == "showLast":
    showLast(args.n)