# pour calculer les couts d'achats
print("Se referer aux autres fichiers pour certaines valeurs")
print("Attention aux natures des UO !")

QUANTITE_MP = float(input("Quantité de matières 1eres: "))
PU_MP = float(input("cout de prod de matières 1eres: "))
PT_MP = QUANTITE_MP * PU_MP

QUANTITE_MOD = float(input("temps total de main d'oeuvre: "))
PU_MOD = float(input("tarif heure main d'oeuvre: "))
PT_MOD = QUANTITE_MOD * PU_MOD

QUANTITE_CPROD1 = float(input("quatite UO centre prod1: "))
PU_CPROD1 = float(input("Cout UO centre prod1: "))
PT_CPROD1 = QUANTITE_CPROD1 * PU_CPROD1

QUANTITE_CPROD2 = float(input("quantite UO centre prod2: "))
PU_CPROD2 = float(input("Cout UO centre prod2: "))
PT_CPROD2 = QUANTITE_CPROD2 * PU_CPROD2

QUANTITE_CPROD3 = float(input("quantite UO centre prod3: "))
PU_CPROD3 = float(input("Cout UO centre prod3: "))
PT_CPROD3 = QUANTITE_CPROD3 * PU_CPROD3

tableau = [
    ["Charges directes"],
    ["","QUANTITE","Prix unitaire","montant"],
    ["Cout d'achat matières 1eres", QUANTITE_MP, PU_MP, PT_MP],
    ["Main d'oeuvre directe", QUANTITE_MOD, PU_MOD, PT_MOD],
    ["Charges indirectes"],
    ["Centre de prod 1", QUANTITE_CPROD1, PU_CPROD1, PT_CPROD1],
    ["Centre de prod 2", QUANTITE_CPROD2, PU_CPROD2, PT_CPROD2],
    ["Centre de prod 3", QUANTITE_CPROD3, PU_CPROD3, PT_CPROD3],
    ["Cout de production","Quantite produite", "montant total / quantité produite", (PT_MP + PT_MOD + PT_CPROD1 + PT_CPROD2 + PT_CPROD3)]
]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))
