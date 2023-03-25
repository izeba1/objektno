from datetime import date

# inicijalizacija praznog rjecnika kolegij
kolegij = {}

# unos podataka o kolegiju
kolegij["ime"] = input("Unesite ime kolegija: ").upper()
kolegij["ects"] = int(input("Unesite ECTS bodove za kolegij: "))

# unos podataka o datumu ispita
dan = int(input("Unesite dan ispita: "))
mjesec = int(input("Unesite mjesec ispita: "))
godina = int(input("Unesite godinu ispita: "))

datum = date(godina, mjesec, dan)

# inicijalizacija praznog rjecnika ispit
ispit = {}

ispit["datum"] = datum
ispit["kolegij"] = kolegij

# inicijalizacija praznog rjecnika student
student = {}

# unos podataka o studentu
student["ime"] = input("Unesite ime studenta: ").capitalize()
student["prezime"] = input("Unesite prezime studenta: ").capitalize()
student["ispit"] = ispit

print("Student", student["ime"], student["prezime"], "je prijavio ispit iz kolegija", student["ispit"]["kolegij"]["ime"],
      "koji će se održati", student["ispit"]["datum"], end=".")