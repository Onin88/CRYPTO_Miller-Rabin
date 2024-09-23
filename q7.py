import secrets
from q5 import MillerRabin

def Eval(b, cpt):
    count = 0

    # Tirer au hasard un nombre n de b bits
    n = secrets.randbits(b)
    
    # Tant que (MillerRabin(n, cpt) = composé)
    while MillerRabin(n, cpt) == 0:
        count+=1
        # Tirer au hasard un nombre n de b bits
        n = secrets.randbits(b)
    print("Nombre de répétitions pour b =", b, ":", count)
    return count