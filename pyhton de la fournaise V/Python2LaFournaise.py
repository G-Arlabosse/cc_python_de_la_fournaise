if "volcan" in open("messagePourSauverLeMonde.txt", "r").read():
    print("Tous aux abris !")

for i in open("livreDeLaNatureEtDesLacs.txt","r").readlines():
    if "l'arbre suspendu" in i:
        print("GPS ACTIVE",i)
        break

pas,avant,gauche,droite = 0,0,0,0
for i in open("desProjectilesEtDesDodos.txt","r").readlines():
    for j in i.split(" "):
        if "arbre" in j:
            avant,pas = avant+10,pas+10
        if "rocher" in j:
            gauche,pas = gauche+5,pas+5
        if "dodo" in j:
            droite,pas = droite+6,pas+6
        if "lac" in j and pas >= 100:
            print(pas,"pas ont été faits")
            if avant >= gauche and avant>= droite:
                print("AVANT")
            if droite >= gauche and droite>= avant:
                print("DROITE")
            if gauche >= avant and gauche>= droite:
                print("GAUCHE")

chiffres = open("lafamilleDodo.txt","r").readline().split(", ")
ids = []
ids = [int(i) for i in chiffres if int(i) not in ids]
ids.sort()
print("LES ID SONT",ids)

ages,majeur,mineur = open("ageDodo.txt", "r").readline().split(", "),0,0
for i in ages:
    if int(i)>=5:
        majeur+=1
    else:
        mineur+=1
print(f"Il y a {mineur} dodos mineurs et {majeur} dodos majeurs")