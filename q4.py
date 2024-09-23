import secrets

#Exponentiation modulaire
def ExpMod(n, a, t):
    # On initialise la variable b à 1
    b = 1

    # On convertit t en binaire
    t = bin(t)[2:]

    # On parcourt chaque bit de t
    for i in t:
        # On met à jour le résultat
        b = (b * b) % n
        # Si le bit est égal à 1
        if i == '1':
            # On calcule b = b * a mod n
            b = (b * a) % n

    # On renvoie b
    return b