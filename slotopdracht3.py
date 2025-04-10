def teken_bord(bord):
    print(bord[0] + " | " + bord[1] + " | " + bord[2])
    print("---------")
    print(bord[3] + " | " + bord[4] + " | " + bord[5])
    print("---------")
    print(bord[6] + " | " + bord[7] + " | " + bord[8])

bord = [" "] * 9

for beurt in range(6):
    if beurt % 2 == 0:
        speler = "X"
    else:
        speler = "O"

    for i in range(9):
        if bord[i] == " ":
            bord[i] = speler
            break

    teken_bord(bord)
    print()
