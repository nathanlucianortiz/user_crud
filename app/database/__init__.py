from flask import g
import sqlite3

DATABASE="user_crud_db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["first_name"] = result[0]
        res_dict["last_name"] = result[1]
        res_dict["job_title"] = result[2]
        out["body"].append(res_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(user_last_name):
    query = """
        SELECT *
        FROM user
        WHERE last_name like ?
        """
    cursor = get_db().execute(query, (str(user_last_name)))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(user_last_name, fields: dict):
    field_string = ",".join(
                    "%s=\"%s\"" % (key, val)
                        for key, val 
                        in fields.items())
    query = """
            UPDATE user
            SET %s
            WHERE last_name = ?
            """ % field_string
    cursor = get_db()
    cursor.execute(query, (user_last_name))
    cursor.commit()
    return True


def create(first_name, last_name, job_title):
    value_tuple = (first_name, last_name, job_title)
    query = """
            INSERT INTO user (
                    first_name,
                    last_name,
                    job_title)
            VALUES (?, ?, ?)
        """
    cursor = get_db()
    last_row_last_name = cursor.execute(query, value_tuple).last_row_last_name
    cursor.commit()
    return last_row_last_name


def delete(user_last_name):
    query = "DELETE FROM user WHERE last_name=%s" % user_last_name
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True 