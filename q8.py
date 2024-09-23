from q7 import Eval
import time
import matplotlib.pyplot as plt
import concurrent.futures

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
    b = [128, 256, 512]

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