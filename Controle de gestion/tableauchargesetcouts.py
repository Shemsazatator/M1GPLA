print("Entrons les valeurs des repartitions primaires")
ADM = float(input("Valeur administration: "))
GMAT = float(input("Valeur gestion du matériel: "))
PRESTAC = float(input("Valeur prestations connexes: "))
APPRO = float(input("Valeur approvisionnement: "))
CPROD1 = float(input("Valeur centre de prod 1: "))
CPROD2 = float(input("Valeur centre de prod 2: "))
CPROD3 = float(input("Valeur centre de prod 3: "))
DISTRIBUTION = float(input("Valeur distribution: "))
###
print("Maintenant les valeurs des repartitions secondaires (comment sera repartie les valeurs des centres auxiliaires dans les centres principaux")
ADMAPPRO = float(input("%age des frais admin en appro: "))
GMATAPPRO = float(input("%age des frais de gestion de materiel en appro: "))
PRESTACAPPRO = float(input("%age des frais de prestac en appro: "))

ADMCPROD1 = float(input("%age des frais admin en centre de prod 1: "))
GMATCPROD1 = float(input("%age des frais de gestion de materiel en centre de prod 1: "))
PRESTACCPROD1 = float(input("%age des frais de prestac en centre de prod 1: "))

ADMCPROD2 = float(input("%age des frais admin en centre de prod 2: "))
GMATCPROD2 = float(input("%age des frais de gestion de materiel en centre de prod 2: "))
PRESTACCPROD2 = float(input("%age des frais de prestac en centre de prod 2: "))

ADMCPROD3 = float(input("%age des frais admin en centre de prod 3: "))
GMATCPROD3 = float(input("%age des frais de gestion de materiel en centre de prod 3: "))
PRESTACCPROD3 = float(input("%age des frais de prestac en centre de prod 3: "))

ADMDISTRIBUTION = float(input("%age des frais admin en distribution: "))
GMATDISTRIBUTION = float(input("%age des frais de gestion de materiel en distribution: "))
PRESTACDISTRIBUTION = float(input("%age des frais de prestac en distribution: "))
###
print("Quelles sont les natures d'unités d'oeuvres des services ?")
UOAPPRO = input("UO des appros: ")
UOCPROD1 = input("UO du centre de prod 1: ")
UOCPROD2 = input("UO du centre de prod 2: ")
UOCPROD3 = input("UO du centre de prod 3: ")
UODISTRIBUTION = input("UO de la distrib: ")
###
NBUOAPPRO = float(input("Nombre d'UO des appros: "))
NBUOCPROD1 = float(input("Nombre d'UO du centre de prod 1: "))
NBUOCPROD2 = float(input("Nombre d'UO du centre de prod 2: "))
NBUOCPROD3 = float(input("Nombre d'UO du centre de prod 3: "))
NBUODISTRIBUTION = float(input("Nombre d'UO de la distrib: "))
###
tableau = [
    ["centres auxiliaires"],
    ["Repartition primaire", "ADM", "G MAT", "PRESTAC"],
    ["Repartition primaire", ADM, GMAT, PRESTAC],
    ["Administratif", -ADM, 0, 0],
    ["Gestion personnel", 0, -GMAT, 0],
    ["Presta connexes", 0, 0, -PRESTAC],
    ["Repartition secondaire", 0, 0, 0]
]

for ligne in tableau:
    for element in ligne:
        print(element, end='\t')
    print()

tableau = [
    ["centres principaux"],
    ["Repartition primaire", "APPRO", "CENTRE PROD 1", "CENTRE PROD 2", "CENTRE PROD 3", "DISTRIB"],
    ["Repartition primaire", APPRO, CPROD1, CPROD2, CPROD3, DISTRIBUTION],
    ["Administratif", (ADMAPPRO/100)*ADM, (ADMCPROD1/100)*ADM, (ADMCPROD2/100)*ADM, (ADMCPROD3/100)*ADM, (ADMDISTRIBUTION/100)*ADM],
    ["Gestion du personnel", (GMATAPPRO/100)*GMAT, (GMATCPROD1/100)*GMAT, (GMATCPROD2/100)*GMAT, (GMATCPROD3/100)*GMAT, (GMATDISTRIBUTION/100)*GMAT],
    ["Prestations connexes", (PRESTACAPPRO/100)*PRESTAC, (PRESTACCPROD1/100)*PRESTAC, (PRESTACCPROD2/100)*PRESTAC, (PRESTACCPROD3/100)*PRESTAC, (PRESTACDISTRIBUTION/100)*PRESTAC],
    ["Repartition secondaire",(APPRO + ((ADMAPPRO/100)*ADM) + ((GMATAPPRO/100)*GMAT) + ((PRESTACAPPRO/100)*PRESTAC)), (CPROD1 + ((ADMCPROD1/100)*ADM) + ((GMATCPROD1/100)*GMAT) + ((PRESTACCPROD1/100)*PRESTAC)), (CPROD2 + ((ADMCPROD2/100)*ADM) + ((GMATCPROD2/100)*GMAT) + ((PRESTACCPROD2/100)*PRESTAC)), (CPROD3 + ((ADMCPROD3/100)*ADM) + ((GMATCPROD3/100)*GMAT) + ((PRESTACCPROD3/100)*PRESTAC)), (DISTRIBUTION + ((ADMDISTRIBUTION/100)*ADM) + ((GMATDISTRIBUTION/100)*GMAT) + ((PRESTACDISTRIBUTION/100)*PRESTAC))]
]

for ligne in tableau:
    for element in ligne:
        print(element, end='\t')
    print()

tableau = [
    ["Nature d'UO", UOAPPRO, UOCPROD1, UOCPROD2, UOCPROD3, UODISTRIBUTION],
    ["Nombre d'UO", NBUOAPPRO, NBUOCPROD1, NBUOCPROD2, NBUOCPROD3, NBUODISTRIBUTION],
    ["Cout par UO", (APPRO + ((ADMAPPRO/100)*ADM) + ((GMATAPPRO/100)*GMAT) + ((PRESTACAPPRO/100)*PRESTAC))/NBUOAPPRO, (CPROD1 + ((ADMCPROD1/100)*ADM) + ((GMATCPROD1/100)*GMAT) + ((PRESTACCPROD1/100)*PRESTAC))/NBUOCPROD1, (CPROD2 + ((ADMCPROD2/100)*ADM) + ((GMATCPROD2/100)*GMAT) + ((PRESTACCPROD2/100)*PRESTAC))/NBUOCPROD2, (CPROD3 + ((ADMCPROD3/100)*ADM) + ((GMATCPROD3/100)*GMAT) + ((PRESTACCPROD3/100)*PRESTAC))/NBUOCPROD3, (DISTRIBUTION + ((ADMDISTRIBUTION/100)*ADM) + ((GMATDISTRIBUTION/100)*GMAT) + ((PRESTACDISTRIBUTION/100)*PRESTAC))/NBUODISTRIBUTION]
]

for ligne in tableau:
    for element in ligne:
        print(element, end='\t')
    print()
