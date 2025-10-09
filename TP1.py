import random
import math
import time

# méthode 1: chiffre par chiffre
# trouver la partie entiere
def racine_chiffre_par_chiffre(nombre):
    partie_entiere = 0
    partie_decimale = 6

    if nombre < 0:
        raise ValueError("nombre negatif")
    if nombre == 0:
        return 0.0
    while (partie_entiere + 1) ** 2 <= nombre:
        partie_entiere += 1
    resultat = float(partie_entiere)

    # le calcul des decimales chiffre par chiffre
    facteur = 10
    for _ in range(partie_decimale):
    # Essayer chaque chiffre de 0 à 9 pour cette position décimale
        meilleur_chiffre = 0.0
        for chiffre in range(10):
            essai = resultat + chiffre / facteur
            if essai ** 2 <= nombre:
                meilleur_chiffre = chiffre
            else:
                break

        resultat += meilleur_chiffre / facteur
        facteur *= 10

    return resultat

print(racine_chiffre_par_chiffre(8))

# methode 2 dichotomie
def racine_dichotomie(n, precision_decimales=6):
    if n < 0 :
        raise ValueError("nombre negatif")
    if n == 0:
        return 0.0

    # Intervalle initial
    bas, haut = (0, n) if n >= 1 else (n, 1)
    precision = 10 ** (-precision_decimales)
    i = 0

    # Boucle principale
    while (haut - bas) > precision:
        i += 1
        milieu = (bas + haut) / 2

        # Affichage des bornes à chaque étape
        print(f"la boucle {i} : bas = {bas:.6f}, haut = {haut:.6f}, milieu = {milieu:.6f}")

        if milieu ** 2 < n:
            bas = milieu
        else:
            haut = milieu

    racine = (bas + haut) / 2
    return round(racine, precision_decimales)


resultat = racine_dichotomie(8)
print(f"\nRésultat final {resultat}")

#comparaison des performances
def comparaison_performances():
    nombre_appels = 100 000
    nombre_aleatoire = (random.randint(10, 100 000) for _ in range(nombre_appels))

    resultat = {}

# test méthode 1
debut = time.monotonic_ns()
for nombre in nombres_aleatoire :
    racine_chiffre_par_chiffre(nombre)
fin = time.monotonic_ns()
temps_total1 = fin - debut
temps_moyen1 = (fin - debut) / nombre_appels




