import sqlite3
import tkinter as tk

# Connect to the database
with sqlite3.connect('DATABASE.db') as conn:
    # necriyiw une table tae compte
    conn.execute(
        "CREATE TABLE IF NOT EXISTS account (username TEXT, psw TEXT)"
    )


    def verif():
        # nchekiw ida yexisti f la table taena
        c = conn.execute(
            "SELECT username,psw FROM account WHERE username=? and psw=?",
            (textfield_username.get(), textfield_password.get())
        )
        account = c.fetchone()

        if account is not None:  # tssema recupira heja == il existe
            label_resultat.config(text="Access granted.")  # AFFICHER DU TEXTE
        else:
            register(textfield_username.get(), textfield_password.get())


    def register(username, password):
        conn.execute(
            "INSERT OR REPLACE INTO account (username, psw) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        label_resultat.config(text=f"Registration complete for {username}.")  # AFFICHER DU TEXTE


    # fenetre taena
    Frame = tk.Tk()
    Frame.title("1st challenge")

    # username
    label_username = tk.Label(Frame, text="Username:")  # TEXT TAE USERNAME
    label_username.grid(row=0, column=0, padx=5, pady=5)  # position

    textfield_username = tk.Entry(Frame)  # text field tae username
    textfield_username.grid(row=0, column=1, padx=5, pady=5)  # position

    # password
    label_password = tk.Label(Frame, text="Password:")  # text tae psw
    label_password.grid(row=1, column=0, padx=5, pady=5)  # position

    textfield_password = tk.Entry(Frame, show="*")  # text field tae psw
    textfield_password.grid(row=1, column=1, padx=5, pady=5)  # position

    # button
    button_check = tk.Button(Frame, text="Checki", command=verif)  # executi verif() on click
    button_check.grid(row=2, column=0, padx=5, pady=5)  # position

    # resultat
    label_resultat = tk.Label(Frame, text="")  # text taena initialement ykoun vide
    label_resultat.grid(row=2, column=1, padx=5, pady=5)  # position

    Frame.mainloop()
