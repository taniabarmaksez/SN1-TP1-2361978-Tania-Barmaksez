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
print(f"Résultat final {resultat}")

#comparaison des performances

nombre_appels= 100000
nombre_aleatoire = (random.randint(10, 100000) for _ in range(nombre_appels))

# test méthode 1
debut = time.monotonic_ns()
for nombre in nombre_aleatoire :
    racine_chiffre_par_chiffre(nombre)
fin = time.monotonic_ns()
temps_total1 = fin - debut
temps_moyen1 = (fin - debut) / nombre_appels

# test méthode 2
debut = time.monotonic_ns()
for nombre in nombre_aleatoire :
    racine_dichotomie(nombre)
fin = time.monotonic_ns()
temps_total2 = fin - debut
temps_moyen2 = (fin - debut)/ nombre_appels



# test méthode 3 math.sqrt
debut = time.monotonic_ns()
for nombre in nombre_aleatoire :
    math.sqrt(nombre)
fin = time.monotonic_ns()
temps_total3= fin - debut
temps_moyen3 = (fin - debut) / nombre_appels



print("Résultats des performances :")
print(f" Méthode 1 (chiffre par chiffre) : Temps total = {temps_total1:2f} ms, Temps moyen = {temps_moyen1:5f} ms")
print(f" Méthode 2 (dichotomie) : Temps total = {temps_total2:2f} ms , Temps moyen =  {temps_moyen2:5f} ms")
print(f" Méthode 3 (math.sqrt) : Temps total = {temps_total3:2f} ms , Temps moyen= {temps_moyen3:5f} ms ")

# méthode 1 généraliser a une n-ieme
def racine_n_chiffre_par_chiffre(nombre, base):
    partie_entiere = 0
    partie_decimale = 6

    if nombre < 0:
        raise ValueError("nombre négatif")
    if nombre == 0:
        return 0.0

    # Trouver la partie entière
    while (partie_entiere + 1) ** base <= nombre:
        partie_entiere += 1
    resultat = float(partie_entiere)

    # Calcul des décimales chiffre par chiffre
    facteur = 10
    for _ in range(partie_decimale):
        meilleur_chiffre = 0.0
        for chiffre in range(10):
            essai = resultat + chiffre / facteur
            if essai ** base <= nombre:
                meilleur_chiffre = chiffre
            else:
                break
        resultat += meilleur_chiffre / facteur
        facteur *= 10

    return resultat

# méthode 2 généraliser a une racine n-ieme
def racine_n_dichotomie(n, base, precision_decimales=6):
    if n < 0:
        raise ValueError("nombre négatif")
    if n == 0:
        return 0.0

    bas, haut = (0, n) if n >= 1 else (n, 1)
    precision = 10 ** (-precision_decimales)

    while (haut - bas) > precision:
        milieu = (bas + haut) / 2

        if milieu ** base < n:
            bas = milieu
        else:
            haut = milieu

    racine = (bas + haut) / 2
    return round(racine, precision_decimales)


# affichez les résultats pour la racine carrée, cubique et quatrieme de 8, 9, 81 et 123
print("Résultats avec racine_n_chiffre_par_chiffre :")
print("Racine carrée :")
print("racine carrée de 8 =", racine_n_chiffre_par_chiffre(8, 2))
print("racine carrée de 9 =", racine_n_chiffre_par_chiffre(9, 2))
print("racine carrée de 81 =", racine_n_chiffre_par_chiffre(81, 2))
print("racine carrée de 123 =", racine_n_chiffre_par_chiffre(123, 2))


print("Résultats avec racine_n_chiffre_par_chiffre :")
print("Racine cubique :")
print("racine cubique de 8 =" , racine_n_chiffre_par_chiffre (8, 3))
print("racine cubique de 9 =", racine_n_chiffre_par_chiffre (9, 3))
print("racine cubique de 81 =", racine_n_chiffre_par_chiffre (81, 3))
print("racine cubique de 123 =", racine_n_chiffre_par_chiffre (123, 3))


print("Résultat avec racine_n_chiffre_par_chiffre : ")
print("Racine quatrieme :")
print("racine quatrieme de 8 = " , racine_n_chiffre_par_chiffre(8, 4))
print("racine quatrieme de 9 = " , racine_n_chiffre_par_chiffre(9, 4))
print("racine quatrieme de 81 = ", racine_n_chiffre_par_chiffre(81, 4))
print("racine quatrieme de 123 = " , racine_n_chiffre_par_chiffre(123, 4))

print("Résultat avec racine_n_dichotomie :")
print("Racine carrée :")
print("racine carrée de 8 =", racine_n_dichotomie(8, 2))
print("racine carrée de 9 =", racine_n_dichotomie(9, 2))
print("racine carrée de 81 =", racine_n_dichotomie(81, 2))
print("racine carrée de 123 =", racine_n_dichotomie(123, 2))

print("Résultat avec racine_n_dichotomie :")
print("Racine cubique :")
print("racine cubique de 8 =" , racine_n_dichotomie(8, 3))
print("racine cubique de 9 =", racine_n_dichotomie(9, 3))
print("racine cubique de 81 =", racine_n_dichotomie (81, 3))
print("racine cubique de 123 =", racine_n_dichotomie (123, 3))

print("Résultat avec racine_n_dichotomie :")
print("Racine quatrieme :")
print("racine quatrieme de 8 = " , racine_n_dichotomie(8, 4))
print("racine quatrieme de 9 = ", racine_n_dichotomie(9, 4))
print("racine quatrieme de 81 = " , racine_n_dichotomie(81, 4))
print("racine quatrieme de 123 = " , racine_n_dichotomie(123, 4))


