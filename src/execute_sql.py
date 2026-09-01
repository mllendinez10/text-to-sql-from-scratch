"""
This file executes a SQL query against the SQLite database.
"""

from pathlib import Path
import sqlite3


DATABASE_FILE = Path("database/products.db")


def execute_sql(sql_query: str) -> list[tuple]:

    # Open connection to communicate with the database
    with sqlite3.connect(DATABASE_FILE) as connection:

        # Object used to send/retrieve SQL commands to the database
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(sql_query)

        # Get all rows returned by the query
        query_result = cursor.fetchall()

    return query_result