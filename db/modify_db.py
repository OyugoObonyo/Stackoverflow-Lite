"""
A module that handels the running sql queries
"""
from flask import current_app
import psycopg2
import psycopg2.extras as ext


conn = psycopg2.connect(
            host=current_app.config['DB_HOST'],
            database=current_app.config['DB_NAME'],
            user=current_app.config['DB_USERNAME'],
            password=current_app.config['DB_PASSWORD'],
            sslmode='require')

def run_sql(sql: str, conn, values=None) -> list:
    """
    run_sql - function that handles the running of sql queries
    @sql: the sql query to be run
    @values: values to be run om sql query. Default is none
    Return
    """
    conn = None
    results = []

    try:
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
