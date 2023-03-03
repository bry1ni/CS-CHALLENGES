import sqlite3

# Connect to the database
with sqlite3.connect('DATABASE.db') as conn:
    # necriyiw une table tae compte
    conn.execute(
        "CREATE TABLE IF NOT EXISTS account (username TEXT, psw TEXT)"
    )


    def verif(username, password):
        # nchekiw ida yexisti f la table taena
        c = conn.execute(
            "SELECT username, psw FROM account WHERE username=? and psw=?", (username, password)
        )
        account = c.fetchone()

        if account is not None:  # tssema recupira heja == il existe
            print('Access granted.')
        else:
            register(username, password)


    def register(username, password):
        conn.execute(
            "INSERT OR REPLACE INTO account (username, psw) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print(f"Registration complete for {username}.")


    # njibou info
    username = input("Username: ")
    password = input("Password: ")

    # nchekiw
    verif(username, password)
