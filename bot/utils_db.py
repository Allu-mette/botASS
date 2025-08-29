import sqlite3

from config import DB_PATH

def getLastResponses()->list[tuple]:
    """
    Get the five last responses
    """

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT content FROM tt_exercices ORDER BY id DESC LIMIT 5")
        response = cur.fetchall()
        return response
    
def addResponse(difficulty: str, tokenCounts: int, content: str):
    """
    Add a response in the table
    """

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        query = "INSERT INTO tt_exercices (date, difficulty, tokenCounts, content) VALUES (CURRENT_DATE, ?, ?, ?)"
        values = (difficulty, tokenCounts, content)
        cur.execute(query, values)
        
        conn.commit()