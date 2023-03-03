def verif(username, password):
    access = False
    accounts = []

    # access le fichier taena with option r
    with open('database.txt', 'r') as f:
        for line in f:
            # add to a list besh jina sahla
            accounts.append(line.strip().split(','))  # strip() besh nahou les \n et split() besh nsepariw bel ,

    # hnaya nchekiw if exists
    for account in accounts:
        # [ [account 1], [account 2],[...], [account n] ]
        # account = ['username1', 'password1']
        usr = account[0]
        psw = account[1]
        if usr == username and psw == password:
            access = True
            break

    if access:
        print('Access granted')
    else:
        # nzidou h fel fichier taena
        with open('database.txt', 'a') as f:
            f.write(f"{username},{password}\n")
        print(f"New account registered for {username}")


# main program
username = input("Username: ")
password = input("Password: ")

verif(username, password)
