# Projet de Cryptographie : Implémentation de l'algorithme Miller-Rabin

### Auteurs :
- GEHIN Sandy
- BELUCHE Quentin

### Download
Pour pouvoir afficher le graphique de fin, votre machine doit avoir
la librairie nécessaire, pour télécharger celle-ci il faut simplement
rentrer la commande : "pip3 install matplotlib"

## Explications
Par problème de rapidité nous effectuons un test d'Eval sur les bits
de la taille 128, 256 et 512. Pour changer les tailles de bits à
tester, il faut simplement aller dans le fichier "tests.py" et à la
ligne 100 rajouter les tailles de bits que vous voulez tester.

Un système de Thread a été mis en place pour augmenter la perfomance.

## test.txt
Ce fichier contient une première compilation de notre code.

## Compilation
Pour compiler ce projet et lancer tous les tests, il faut simplement
executer la commande "make test", celle-ci va tester toutes les fonctions
de chaque question et mettre la sortie de ce résultat dans le fichier
"test.txt". Le graphique apparaîtra quand tous les tests se seront terminés.

## Suppression
Pour supprimer le fichier résultat ainsi créé après compilation,
il faut executer la commande "make clean".
