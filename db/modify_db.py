"""
A module that handels the running sql queries
"""
from flask import current_app
import psycopg2
import psycopg2.extras as ext


def run_sql(sql, values=None):
    conn = None
    results = []

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="stackoverflow_lite",
            user=current_app.config['DB_USERNAME'],
            password=current_app.config['DB_PASSWORD'],
            sslmode='require')
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
