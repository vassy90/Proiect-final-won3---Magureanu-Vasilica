import random
import sys

imaginea_spanzuratorii = [r"""
 +----+
 ||  ||
     ||
     ||
     ||
     ||
=======""",
                          r"""
 +----+
 ||  ||
 ()  ||
     ||
     ||
     ||
=======""",
                          r"""
 +------+
 ||    ||
 ()    ||
 ||    ||
       ||
       ||
=========""",
                          r"""
 +------+
 ||    ||
 ()    ||
/||    ||
       ||
       ||
=========""",
                          r"""
 +--------+
 ||      ||
 ()      ||
/||\     ||
         ||
         ||
===========""",
                          r"""
 +----------+
 ||        ||
 ()        ||
/||\       ||
/          ||
           ||
=============""",
                          r"""
 +------------+
 ||          ||
 ()          ||
/||\         ||
/  \         ||
             ||
==============="""]

categorie = "Animale salbatice"
cuvinte = ['ALIGATOR', 'ARICI', 'BABUIN', 'BURSUC', 'CANGUR', 'CERB', 'DIHOR', 'ELEFANT', 'ELAN', 'GHEPARD', 'GORILA',
           'HIENA', 'HIPOPOTAM', 'IEPURE', 'JAGUAR', 'LEU', 'LILIAC', 'MAIMUTA', 'PUMA', 'RINOCER', 'TIGRU', 'URS',
           'VULPE', 'ZEBRA']


def main():
    litere_gresite = []
    litere_corecte = []
    cuvantul_secret = random.choice(cuvinte)
    while True:
        deseneaza_spanzuratoarea(litere_gresite, litere_corecte, cuvantul_secret)
        litera_introdusa = litera_introdusa_de_jucator(litere_gresite + litere_corecte)

        if litera_introdusa in cuvantul_secret:
            litere_corecte.append(litera_introdusa)
            if all([litera_secreta in litere_corecte for litera_secreta in cuvantul_secret]):
                print(f'Da! Cuvantul secret este: "{cuvantul_secret}"')
                print('Ati castigat! :)')
                break
        else:
            litere_gresite.append(litera_introdusa)
            if len(litere_gresite) == len(imaginea_spanzuratorii) - 1:
                deseneaza_spanzuratoarea(litere_gresite, litere_corecte, cuvantul_secret)
                print('Ai ramas fara vieti! :(')
                print(f'Cuvantul secret era: "{cuvantul_secret}"')
                break


def deseneaza_spanzuratoarea(litere_gresite, litere_corecte, cuvantul_secret):
    # Deseneaza spanzuratoarea.
    print(imaginea_spanzuratorii[len(litere_gresite)])
    print(f'Categoria este: {categorie}')
    print()
    print("Litere gresite: ", end="")
    if len(litere_gresite) != 0:
        print(" ".join(litere_gresite))
    else:
        print('Nici o litera gresita.')
    print()

    spatii_libere = ['_'] * len(cuvantul_secret)

    for i in range(len(cuvantul_secret)):
        if cuvantul_secret[i] in litere_corecte:
            spatii_libere[i] = cuvantul_secret[i]

    print(' '.join(spatii_libere))


def litera_introdusa_de_jucator(litera_deja_introdusa):
    # Functia preia o litera valida de la utilizator.
    while True:
        print('Ghiceste o litera.')
        litera_introdusa = input('> ').upper()

        if len(litera_introdusa) != 1:
            print('Va rog sa introduceti o singura litera.')
        elif litera_introdusa in litera_deja_introdusa:
            print('Ati introdus deja acesta litera. Va rog sa alegeti din nou.')
        elif not litera_introdusa.isalpha():
            print('Va rog sa introduceti o LITERA.')
        else:
            return litera_introdusa


if __name__ == '__main__':
    try:
        main()
    except EOFError:   # folosim EOFError(Ctrl + D) in loc de KeyboardInterrupt(Ctrl + C) pentru a functiona in consola
                       # run a Pycharm-ului
        sys.exit()
