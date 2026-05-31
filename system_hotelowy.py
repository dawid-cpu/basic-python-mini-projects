pokoje = []
goscie = []
rezerwacje = []

def dodaj_pokoj():
    try:
        numer = int(input("numer pokoju: "))
    except ValueError:
        print("blad - tylko cyfry")
        return
    if numer <= 0:
        print("numer musi byc wiekszy od 0")
        return
    typ = input("typ pokoju: ")
    if len(typ) == 0:
        print("puste pole")
        return
    try:
        cena = float(input("cena pokoju: "))
    except ValueError:
        print("blad - tylko liczby")
        return
    if cena <= 0:
        print("cena musi byc wieksza od 0")
        return
    pokoje.append({"numer": numer, "typ": typ, "cena": cena, "dostepnosc": True})
    print("dodano pokoj")

def dodaj_goscia():
    imie = input("podaj imie: ")
    if len(imie) == 0:
        print("puste pole")
        return
    nazwisko = input("podaj nazwisko: ")
    if len(nazwisko) == 0:
        print("puste pole")
        return
    email = input("podaj email: ")
    if len(email) == 0:
        print("puste pole")
        return
    if "@" not in email:
        print("nieprawidlowy email")
        return
    telefon = input("podaj telefon: ")
    if len(telefon) == 0:
        print("puste pole")
        return
    if not telefon.isdigit():
        print("telefon tylko cyfry")
        return
    if len(telefon) != 9:
        print("telefon musi miec 9 cyfr")
        return
    goscie.append({"imie": imie, "nazwisko": nazwisko, "email": email, "telefon": telefon})
    print("dodano goscia")

def dodaj_rezerwacje():
    try:
        id = int(input("podaj id rezerwacji: "))
    except ValueError:
        print("blad - tylko cyfry")
        return
    imie = input("podaj imie: ")
    if len(imie) == 0:
        print("puste pole")
        return
    nazwisko = input("podaj nazwisko: ")
    if len(nazwisko) == 0:
        print("puste pole")
        return
    data_od = input("data od (dd-mm-rrrr): ")
    if len(data_od) == 0:
        print("puste pole")
        return
    data_do = input("data do (dd-mm-rrrr): ")
    if len(data_do) == 0:
        print("puste pole")
        return
    rezerwacje.append({"id": id, "imie": imie, "nazwisko": nazwisko, "dataod": data_od, "datado": data_do, "status": True})
    print("dodano rezerwacje")

def anuluj_rezerwacje():
    try:
        szukane_id = int(input("podaj id rezerwacji: "))
    except ValueError:
        print("blad - tylko cyfry")
        return
    znaleziono = False
    for rezerwacja in rezerwacje:
        if rezerwacja["id"] == szukane_id:
            rezerwacja["status"] = False
            print("anulowano rezerwacje")
            znaleziono = True
    if not znaleziono:
        print("nie znaleziono rezerwacji")

def szukaj_wolne():
    znaleziono = False
    for pokoj in pokoje:
        if pokoj["dostepnosc"] == True:
            print(pokoj)
            znaleziono = True
    if not znaleziono:
        print("brak wolnych pokoi")

def szukaj_zajete():
    znaleziono = False
    for pokoj in pokoje:
        if pokoj["dostepnosc"] == False:
            print(pokoj)
            znaleziono = True
    if not znaleziono:
        print("brak zajetych pokoi")

def szukaj_goscia():
    imie = input("imie: ")
    if len(imie) == 0:
        print("puste pole")
        return
    nazwisko = input("nazwisko: ")
    if len(nazwisko) == 0:
        print("puste pole")
        return
    telefon = input("telefon: ")
    if len(telefon) == 0:
        print("puste pole")
        return
    znaleziono = False
    for gosc in goscie:
        if gosc["imie"].lower() == imie.lower() and gosc["nazwisko"].lower() == nazwisko.lower() and gosc["telefon"] == telefon:
            print(gosc)
            znaleziono = True
    if not znaleziono:
        print("nie znaleziono goscia")

while True:
    print("\n1. Dodaj pokoj")
    print("2. Dodaj goscia")
    print("3. Dodaj rezerwacje")
    print("4. Anuluj rezerwacje")
    print("5. Wolne pokoje")
    print("6. Zajete pokoje")
    print("7. Szukaj goscia")
    print("8. Wyjdz")
    wybor = input("wybierz: ")
    if wybor == "1":
        dodaj_pokoj()
    elif wybor == "2":
        dodaj_goscia()
    elif wybor == "3":
        dodaj_rezerwacje()
    elif wybor == "4":
        anuluj_rezerwacje()
    elif wybor == "5":
        szukaj_wolne()
    elif wybor == "6":
        szukaj_zajete()
    elif wybor == "7":
        szukaj_goscia()
    elif wybor == "8":
        break
    else:
        print("zly wybor")