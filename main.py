import os


def check_empthy_f(nom):
    if os.path.exists(nom):
        if os.stat(nom).st_size == 0:
            print("Fichier",nom,"est vide")
        else:
            print("Fichier",nom,"est plein")
    else:
        print("Le fichier %s n'existe pas !!",nom)



check_empthy_f("test.txt")