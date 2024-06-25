while True:
    h = input("Jeżeli chcesz zakończyć program to wpisz quit. Jeżeli nie, prosze wprowadź hasło: ")
    if h == "KursPythona123!":
        print("Dostęp przyznany!")
        break
    elif h == "quit":
        print("Kończę działanie programu!")
        break
    else:
        print("Hasło niepoprawne! Spróbój ponownie!")
