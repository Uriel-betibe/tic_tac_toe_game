# tic tac toe game
# by @uriel


tableau = {"A": " ", "B": " ", "C": " ", "D": " ", "E": " ", "F": " ", "G": " ", "H": " ", "I": " "}
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
dejaJouer = []

def check():
    if player == 1:
        signe = "x"
        # verification horizontal
        if (tableau["A"] == signe and tableau["B"] == signe and tableau["C"] == signe) or (tableau["D"] == signe and tableau["E"] == signe and tableau["F"] == signe) or (tableau["G"] == signe and tableau["H"] == signe and tableau["I"] == signe):
            return 1
        # verification vertical
        if (tableau["A"] == signe and tableau["D"] == signe and tableau["G"] == signe) or (tableau["B"] == signe and tableau["E"] == signe and tableau["H"] == signe) or (tableau["C"] == signe and tableau["F"] == signe and tableau["I"] == signe):
            return 1
        # verification diagonal
        if (tableau["A"] == signe and tableau["E"] == signe and tableau["I"] == signe) or (tableau["C"] == signe and tableau["E"] == signe and tableau["G"] == signe):
            return 1
        return 0
    else:
        signe = "o"
        # verification horizontal
        if (tableau["A"] == signe and tableau["B"] == signe and tableau["C"] == signe) or (
                tableau["D"] == signe and tableau["E"] == signe and tableau["F"] == signe) or (
                tableau["G"] == signe and tableau["H"] == signe and tableau["I"] == signe):
            return 2
        # verification vertical
        if (tableau["A"] == signe and tableau["D"] == signe and tableau["G"] == signe) or (
                tableau["B"] == signe and tableau["E"] == signe and tableau["H"] == signe) or (
                tableau["C"] == signe and tableau["F"] == signe and tableau["I"] == signe):
            return 2
        # verification diagonal
        if (tableau["A"] == signe and tableau["E"] == signe and tableau["I"] == signe) or (
                tableau["C"] == signe and tableau["E"] == signe and tableau["G"] == signe):
            return 2
        return 0



print("A|B|C")
print("-+-+-")
print("C|D|E")
print("-+-+-")
print("F|G|H")
print("******************************")


player = 1    # initilisation du joueur 1
nbCoups = 0  # on compte le nombre de coups pour quae quand toute les case sont pleines on arrete le jeu
play = True

while play:
    print(tableau["A"] + "|" + tableau["B"] + "|" + tableau["C"])
    print("-+-+-")
    print(tableau["D"] + "|" + tableau["E"] + "|" + tableau["F"])
    print("-+-+-")
    print(tableau["G"] + "|" + tableau["H"] + "|" + tableau["I"])
    print("******************************")

    playerAction = True
    while playerAction == True:
        if player == 1:
            choice = input("ou voulez vous jouez player 1-X: ")
            if (choice in choices) and (choice not in dejaJouer):
                tableau[choice] = "x"
                resultat = check()
                player = 2
                dejaJouer.append(choice)
                playerAction = False
            else:
                print("mauvaise entré rééssayer")
        elif player == 2:
            choice = input("ou voulez vous jouez player 2-O: ")
            if (choice in choices) and (choice not in dejaJouer):
                tableau[choice] = "o"
                resultat = check()
                player = 1
                dejaJouer.append(choice)
                playerAction = False
            else:
                print("mauvaise entré, rééssayer")

    nbCoups += 1
    if nbCoups == 9 or resultat != 0:
        if resultat == 1:
            print("player 1 Win !!")
        if resultat == 2:
            print("player 2 win !!")
        play = False

# todo implémenter un mode joueur solo contre l'ordinateur
# todo ajouter une interface visuel avec TKinter

