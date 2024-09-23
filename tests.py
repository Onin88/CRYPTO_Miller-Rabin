from q3 import Decomp
import secrets
from q4 import ExpMod
from q5 import MillerRabin
from q7 import Eval
import concurrent.futures
import time
import matplotlib.pyplot as plt


def Test_Decomp():

    # Tester la fonction sur 10000 valeurs différentes
    for _ in range(10000):
        n = secrets.randbelow(100000)

        if n % 2 != 0:
            n+=1
        s, d = Decomp(n)
        if(n - 1 != 2**s*d):
            print("La fonction Decomp a échoué sur n = ", n, "avec s = ", s, "et d = ", d)
    print (" ------------------ TEST DE LA FONCTION DECOMP ------------------ \n")
    print ("Tests réussis\n")
    print (" ----------------------------------------------------------------\n")

# Appel de la fonction Test()
Test_Decomp()


def Test_ExpMod():
    for _ in range(10000):
        
        a = secrets.randbelow(100000)
        n = secrets.randbelow(100000)
        t = secrets.randbelow(100000)

        if(ExpMod(n, a, t) != pow(a, t, n)):
            print("La fonction ExpMod a échoué sur n = ", n, "avec a = ", a, "et t = ", t)
    print (" ------------------ TEST DE LA FONCTION EXPMOD ------------------ \n")
    print ("Tests réussis\n")
    print (" ----------------------------------------------------------------\n")

# Appel de la fonction Test_ExpMod()
Test_ExpMod()


#Fonction Test()
def Test():
    #Utilisez votre fonction pour tester les 3 nombres suivants (´ecrits en hexad´ecimal).
    #Dites si chaque nombre est pseudo-premier ou compos´e avec cpt = 20.
    print("Nombre pseudo-premier ou composé avec cpt = 20 : \n")

    n1_hex = (
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
        "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        "E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF"
    )

    print("n1_hex : ", MillerRabin(int(n1_hex, 16), 20))

    n2_hex = (
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEC4FFFF"
        "FDAF00000000000000000000000000000000000000000000"
        "00000000000000000000000000000000000000000002D9AB"
    )

    print("n2_hex : ", MillerRabin(int(n2_hex, 16), 20))

    n3_hex = (
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
        "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
        "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381"
        "FFFFFFFFFFFFFFFF"
    )

    print("n3_hex : ", MillerRabin(int(n3_hex, 16), 20))
    print("\n")

# Appel de la fonction Test()
Test()


def evaluate_single_size(i, compteur):
    results = []
    for j in range(compteur):
        results.append(Eval(i, 20))
        print("compteur =", j)
    moyenne_groupe = sum(results) / compteur
    print("Moyenne pour b =", i, ":", moyenne_groupe)
    return moyenne_groupe

def TestEval():
    start_time = time.time()

    # Tableau des nombre de bits à tester
    b = [128, 256, 512] #, 1024, 2048, 4096

    # Répeter 100 fois la fonction pour chaque valeur
    compteur = 100

    # Initialiser un tableau pour stocker les moyennes
    moyennes = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(evaluate_single_size, i, compteur): i for i in b}

        for future in concurrent.futures.as_completed(futures):
            i = futures[future]
            try:
                moyenne_groupe = future.result()
                moyennes.append(moyenne_groupe)  # Ajouter la moyenne au tableau des moyennes
            except Exception as e:
                print(f"Une exception s'est produite pour b = {i}: {e}")

    # Imprimer ou utiliser le tableau des moyennes
    print("Moyennes des groupes de 100 résultats :", moyennes)

    # Plotting the graph
    plt.plot(b, moyennes, marker='o')
    plt.xlabel('Taille en bits du nombre')
    plt.ylabel('Moyenne sur les 100 tests sur les 6 tailles de bits différentes')
    plt.title('Évolution de la moyenne du nombre de répétitions en fonction de la taille du nombre')
    plt.grid(True)
    plt.show()

    end_time = time.time()
    execution_time = end_time - start_time
    print("Temps d'exécution de la fonction TestEval() :", execution_time, "secondes")

TestEval()