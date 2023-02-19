print("Se referer aux autres fichiers pour certaines valeurs")
QUANTITE = float(input("Quantité de matière: "))

choix = input("Prix unitaire(U) ou prix total(T) ?")

if choix == 'U':
    PU = float(input("Prix unitaire: "))
    PT = PU * QUANTITE
    UOU = float(input("Prix UO unitaire: "))
    TOU = UOU * QUANTITE
elif choix == 'T':
    PT = float(input("Prix total: "))
    PU = PT / QUANTITE
    TOU = float(input("Prix UO total: "))
    UOU = TOU / QUANTITE
else:
    print("Choix invalide.")

tableau = [
    ["Charges directes"],
    ["Produit", "Quantite", "Prix unitaire", "Prix total"],
    ["Achat du produit", QUANTITE, PU, PT],
    ["Charges indirectes"],
    ["Centre d'approvisionnement", QUANTITE, UOU, TOU],
    ["Cout d'achat", QUANTITE, PU + UOU, PT + TOU]

]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))
