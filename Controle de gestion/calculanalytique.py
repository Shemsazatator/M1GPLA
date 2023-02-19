# pour calculer les couts d'achats
print("Se referer aux autres fichiers pour certaines valeurs")

QUANTITE_VENDUE = float(input("Quantité vendue: "))
PRIX_VENTE = float(input("Prix de vente: "))

CU_REVIENT = float(input("Cout unitaire de revient: "))

tableau = [
    ["","QUANTITE","Prix unitaire","montant"],
    ["Chiffre d'affaires", QUANTITE_VENDUE, PRIX_VENTE, (QUANTITE_VENDUE * PRIX_VENTE)],
    ["- cout de revient", QUANTITE_VENDUE, CU_REVIENT, (CU_REVIENT * QUANTITE_VENDUE)],
    ["Resultat analytique", QUANTITE_VENDUE, (((QUANTITE_VENDUE * PRIX_VENTE) - (CU_REVIENT * QUANTITE_VENDUE))/QUANTITE_VENDUE), ((QUANTITE_VENDUE * PRIX_VENTE) - (CU_REVIENT * QUANTITE_VENDUE))]
]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))
