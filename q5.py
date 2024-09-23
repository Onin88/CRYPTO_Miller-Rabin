from q4 import ExpMod
from q3 import Decomp
import secrets

#Implémentation de l'algorithme de Miller-Rabin
def MillerRabin(n, cpt):
    # Effectue cpt itérations de Miller-Rabin sur n
    for _ in range(cpt):

        # Décomposition de n - 1 = 2^s * d avec d impair
        s, d = Decomp(n)

        # Génère un nombre aléatoire entre 1 et n-1 exclus
        a = secrets.randbelow(n - 2) + 2

        # Calcul de a^d mod n
        b = ExpMod(n, a, d)

        #Si b === 1 (mod n) ou b === -1 (mod n)
        if b == 1 or b == -1:
            return 1 # On ne peut rien dire et on arrête

        i = 1
        while i <= s:
            b = ExpMod(n, a, (d*2)**i)
            if b == -1:
                return 1 # On ne peut rien dire et on arrête
            else:
                if b == 1:
                    return 0 # Le nombre est composé
            i+=1

        return 0 # Le nombre est composé