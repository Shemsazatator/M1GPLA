# pour calculer les couts d'achats
print("Se referer aux autres fichiers pour certaines valeurs")

QUANTITE_VENDUE = float(input("Quantité vendue: "))
CU_VENDUES = float(input("Cout unitaire de stock: "))
CT_VENDUES = QUANTITE_VENDUE * CU_VENDUES

PRIX_VENTE = float(input("Prix de vente: "))
CU_DISTRIBUTION = float(input("Cout unitaire UO de distribution: "))
CT_DISTRIBUTION = (PRIX_VENTE*QUANTITE_VENDUE)*CU_DISTRIBUTION

tableau = [
    ["","QUANTITE","Prix unitaire","montant"],
    ["Cout de prod des pdts vendus", QUANTITE_VENDUE, CU_VENDUES, CT_VENDUES],
    ["Charges indirectes"],
    ["Centre de distribution", PRIX_VENTE*QUANTITE_VENDUE, CU_DISTRIBUTION, CT_DISTRIBUTION],
    ["Cout de revient des pdts vendus", QUANTITE_VENDUE, (CT_VENDUES+CT_DISTRIBUTION/QUANTITE_VENDUE), (CT_VENDUES+CT_DISTRIBUTION)]
]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))
