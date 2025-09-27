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
def racine_dichotomie(nombre):
    precision_decimal = 0.000001
    if nombre < 0:
        raise ValueError("nombre negatif")
    if nombre == 0:
        return 0.0

    # Déterminer l'intervalle initial
    if nombre >= 1:  # Si nombre ≥ 1 : intervalle initial = [0, nombre]
        bas = 0
        haut = nombre
    else:  # Si 0 < nombre < 1 : intervalle initial = [nombre, 1]
        bas = nombre
        haut = 1

    # Réduction de l'intervalle de moitié
    while (haut - bas) > precision_decimal:
        milieu = (bas + haut) / 2
        if milieu ** 2 < nombre:
            bas = milieu
        else:
            haut = milieu

    resultat = (bas + haut) / 2
    return resultat

print(racine_dichotomie(8))
