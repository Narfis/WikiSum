import psycopg2
import os
from dotenv import load_dotenv

class DataBase:
    def __init__(self):
        load_dotenv()
        try:
            self.connection = psycopg2.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.connection.cursor()
        except psycopg2.errors.OperationalError:
            print("Unable to access database, continues without database connection.")
            self.connection = None
            self.cursor = None

    def insert_summary(self, page_name: str, summary: str):
        self.cursor.execute("INSERT INTO summary_table (wiki_page_name, page_summary) VALUES (%s, %s)", (page_name, summary))
        self.connection.commit()

    def get_summary(self, page_name: str):
        self.cursor.execute("SELECT page_summary FROM summary_table WHERE wiki_page_name = %s", (page_name,))
        summary = self.cursor.fetchone()
        return summary[0] if summary else None
    
    def get_key_points(self, page_name: str):
        self.cursor.execute("SELECT key_point_id FROM key_points_table WHERE wiki_page_name = %s", (page_name,))
        key_point_id = self.cursor.fetchone()
        if key_point_id:
            self.cursor.execute("SELECT point FROM key_points WHERE id = %s", (str(key_point_id[0]),))
            key_points = self.cursor.fetchall()
            return [point[0] for point in key_points]
        return None
    
    def insert_key_points(self, page_name: str, key_points: list[str], id: str):
        self.cursor.execute("INSERT INTO key_points_table (wiki_page_name, key_point_id) VALUES (%s, %s)", (page_name, str(id)))
        for key_point in key_points:
            self.cursor.execute("INSERT INTO key_points (id, point) VALUES (%s, %s)", (str(id), key_point))
        self.connection.commit()