# pour calculer la fiche des stocks
print("Se referer aux autres fichiers pour certaines valeurs")

# partie stock
STOCK = float(input("Quantité en stock: "))
PT_STOCK = float(input("Prix total: "))
CUMP_STOCK = PT_STOCK / STOCK

# partie achat
ACHAT = float(input("Quantité achetée: "))
COUT_ACHAT = float(input("Cout d'achat: "))
PT_ACHAT = COUT_ACHAT * ACHAT

PRODUCTION = float(input("Quantité pour production: "))
PU_PROD = ((PT_ACHAT + PT_STOCK) / (STOCK + ACHAT))
PT_PROD = -PRODUCTION * PU_PROD

tableau = [
    ["Entrées / Sorties"],
    ["", "Quantite", "Prix unitaire", "Prix total"],
    ["Stock en date", 0, 0, 0], #deja ici donc rien ne rentre rien ne sort
    ["Achats", ACHAT, COUT_ACHAT, PT_ACHAT],
    ["Production", -PRODUCTION, PU_PROD, PT_PROD]
]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))

tableau = [
    ["Stock Final"],
    ["", "Quantite", "Prix total", "CUMP"],
    ["Stock en date", STOCK, PT_STOCK, (PT_STOCK/STOCK)],
    ["Achats", (STOCK + ACHAT), (PT_ACHAT + PT_STOCK), ((PT_ACHAT + PT_STOCK) / (STOCK + ACHAT))],
    ["Production", ((STOCK + ACHAT)-PRODUCTION), ((PT_ACHAT + PT_STOCK) + (PT_PROD)), (((PT_ACHAT + PT_STOCK) + (PT_PROD)) / ((STOCK + ACHAT)-PRODUCTION))]
]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))
