# pour calculer le seuil de rentabilite
CA = float(input("Chiffre d'affaires: "))
CV = float(input("Couts variables: "))
MCV = CA - CV
CF = float(input("Couts fixes: "))
RESULTAT = MCV - CF

TCA = round((CA/CA*100),2)
TCV = round((CV/CA*100),2)
TMCV = round((MCV/CA*100),2)
TCF = round((CF/CA*100),2)
TRESULTAT = round((RESULTAT/CA*100),2)

tableau = [
    ["", "Valeur", "Taux"],
    ["CA", CA, TCA],
    ["CV", CV, TCV],
    ["MCV", MCV, TMCV],
    ["CF", CF, TCF],
    ["RESULTAT", RESULTAT, TRESULTAT]
]

for ligne in tableau:
    print('\t'.join(str(element) for element in ligne))

SR = CF / (TMCV/100)
print("A partie de " + str(SR) + " euros, l'entreprise generera des benefices")

QUANTITE = float(input("Quantite vendue: "))
SRQTE = (SR / QUANTITE)*10
print("A partie de " + str(SRQTE) + " produits vendus, l'entreprise generera des benefices")

choix = input("(s)aisonnier ou (c)ontinue?")
if choix == 'c':
    POINT_MORT = (SR*360)/CA
elif choix == 's':
    POINT_MORT = (SR*360)/CA
else:
    print("Choix invalide.")

print("A partie du mois " + str(round((POINT_MORT/30),0)))
print("Et du " + str((POINT_MORT-((POINT_MORT/30)*30))+1) + "eme jour, l'entreprise generera des benefices")

MS = CA - SR
print("La marge de sécurité est de " + str(MS) + " euros")
print("cela signifie que l'on vendra " + str(MS) + " euros a partir du moment ou l'on est rentable")

INDICE = MS / CA
print("L'indice est de " + str(INDICE) + " , % de l'annee en cours.")
print("Elle aura donc tant de mois pour devenir rentable (confortable ou non)")
