from q5 import MillerRabin

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

# Appel de la fonction Test()
Test()
