import sqlite3

def create_table(id, name):
    con = sqlite3.connect("SQL.sqlite")
    cur = con.cursor()

    cur.execute(
        """CREATE TABLE user(
            id int PRIMARY KEY,
            name TEXT
        )
        """
    )
    cur.execute("INSERT INTO user VALUES (?,?)", (id, name))
    con.commit()

create_table()
