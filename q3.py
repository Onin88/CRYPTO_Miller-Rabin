import secrets

# Fonction Decomp()
def Decomp(n):

    # Trouver s et d tels que n-1 = 2^s * d
    s = 0 # On initialise s à 0 car il reflétera le nombre de fois où on divise d par 2
    d = n-1 # d * 2^0 = n-1 donc d = n-1

    while d % 2 == 0: # Tant que d est pair
        s+=1 # On incrémente s de 1
        d//=2 # On divise d par 2 jusqu'à ce qu'il soit impair

    return s, d