# =====================================================================================================================
# Programme qui demande à un utilisateur de choisir un polygone et la
# longueur d'un coté,
# puis trancer la figure géométrique
# =====================================================================================================================

# importation des bibliotheques
import turtle
import time
import bcolors
# figures authorisées
figures = ["1", "2", "3", "4", "5", "6"]

#-----------------------------------------------------------------------------------------------------------------------
# fonction qui affiche le menu et qui retourne le choix de l'utilisateur
#-----------------------------------------------------------------------------------------------------------------------

def userchoice():
    print("|=======================================================|")
    print("|   PROGRAMME DE TRACAGE DES FIGURES GEOMETRIQUES       |")
    print("|=======================================================|")
    print("| 1-Tracer un Triange isocèle                           |")
    print("| 2-Tracer un Carré                                     |")
    print("| 3-Tracer un rectangle                                 |")
    print("| 4-Tracer un Cercle                                    |")
    print("| 5-Tracer un Cube                                      |")
    print("| 6-Tracer un hexagone                                  |")
    print("|=======================================================|")
    option = input("Veuillez choisir une option : ")
    return option

#-----------------------------------------------------------------------------------------------------------------------
# fonction qui permet de revenir au menu principal à chaque fois tant que la condition n'est pas verifiée
#-----------------------------------------------------------------------------------------------------------------------

def userdraw():
    while True:
        usdr = input("Voulez-vous faire un autre dessin ? O|N : ")
        if usdr == "1" or usdr == "O" or usdr == "o":
            rejouer()

        elif usdr == "2" or usdr == "N" or usdr == "n":
            print("|=======================================================|")
            print("INFO : AU REVOIR ET A LA PROCHAINE                      |")
            print("|=======================================================|")
            exit()
        else:
            print()


#-----------------------------------------------------------------------------------------------------------------------
# fonction qui initialise la fenetre pour un nouveau dessin
#-----------------------------------------------------------------------------------------------------------------------

def initwindows():
    fenetre = turtle.Screen()
    time.sleep(5)
    fenetre.clear()
    fenetre.title("VIDE")


#-----------------------------------------------------------------------------------------------------------------------
# fonction qui dessine un triangle
#-----------------------------------------------------------------------------------------------------------------------

def drawtriangle():
    while True:
        try:
            cote = int(input("Entrer la longueur du coté : "))
            break
        except ValueError:
            print(f"{bcolors.bcolors.WARNING}\nWARNING : Votre reponse est incorrecte, veuillez entrer un nombre !{bcolors.bcolors.RESET}")
            print()
    # tracer le triangle
    fenetre = turtle.Screen()
    fenetre.bgcolor("black")
    fenetre.title("DESSINER UNE TRIANGLE")
    stylo = turtle.Turtle()
    stylo.color("green")

    for _ in range(3):
        stylo.forward(cote)
        stylo.left(120)


# ----------------------------------------------------------------------------------------------------------------------
# fonction qui dessine un carré
#-----------------------------------------------------------------------------------------------------------------------

def drawsquarre():
    while True:
        try:
            cote = int(input("Entrer la longueur du coté : "))
            break
        except ValueError:
            print(f"{bcolors.bcolors.WARNING}\nWARNING : Votre reponse est incorrecte, veuillez entrer un nombre !{bcolors.bcolors.RESET}")
            print()

    fenetre = turtle.Screen()
    fenetre.bgcolor("black")
    fenetre.title("DESSINER UN CARRE")
    stylo = turtle.Turtle()
    stylo.color("green")

    for _ in range(4):
        stylo.forward(cote)
        stylo.left(90)


# ----------------------------------------------------------------------------------------------------------------------
# Fonction qui dessine un rectangle
#-----------------------------------------------------------------------------------------------------------------------

def drawrectangle():
    while True:
        try:
            longueur = int(input("Entrer la longueur : "))
            largeur = int(input("Entrer la largeur : "))
            break
        except ValueError:
            print(f"{bcolors.bcolors.FAIL}\nERROR : Votre reponse est incorrecte, la longueur et la largeur doivent etre des nombres !! {bcolors.bcolors.RESET}")
            print()

    fenetre = turtle.Screen()
    fenetre.bgcolor("black")
    fenetre.title("DESSINER UN RECTANGLE")
    stylo = turtle.Turtle()
    stylo.color("green")

    if largeur < longueur:

        for _ in range(4):
            stylo.forward(longueur)
            stylo.left(90)
            stylo.forward(largeur)
            stylo.left(90)

    else:
        for _ in range(4):
            stylo.forward(largeur)
            stylo.left(90)
            stylo.forward(longueur)
            stylo.left(90)


# ----------------------------------------------------------------------------------------------------------------------
# fonction du dessine un cercle en fonction du rayon entré
#-----------------------------------------------------------------------------------------------------------------------

def drawcircle():
    while True:
        try:
            rayon_cercle = int(input("Entrer le rayon du cercle : "))
            break
        except ValueError:
            print(f"{bcolors.bcolors.FAIL}\nERROR : Votre reponse est incorrecte, le rayon d'un cercle doit etre un nombre !! {bcolors.bcolors.RESET}")
            print()

    fenetre = turtle.Screen()
    fenetre.bgcolor("black")
    fenetre.title("DESSINER UN CERCLE")
    stylo = turtle.Turtle()
    stylo.color("green")
    stylo.circle(rayon_cercle)


# ----------------------------------------------------------------------------------------------------------------------
# Fonction qui dessine un cube
# -----------------------------------------------------------------------------------------------------------------------

def drawcube():
    while True:
        try:
            arrete = int(input("Entrer la longueur de l'arrete : "))
            break
        except ValueError:
            print(f"{bcolors.bcolors.FAIL}\nERROR : Votre reponse est incorrecte, l'arrete d'un cube est un nombre !! {bcolors.bcolors.RESET}")
            print()

    fenetre = turtle.Screen()
    fenetre.bgcolor("black")
    fenetre.title("DESSINER UN CUBE 3D")
    stylo = turtle.Turtle()
    stylo.color("green")

    # premier carré
    for _ in range(4):
        stylo.forward(arrete)
        stylo.left(90)
    # on se deplace vers le bas à gauche
    stylo.goto(arrete/2, arrete/2)

    # carré arrière
    for _ in range(4):
        stylo.forward(arrete)
        stylo.left(90)

    # on se deplace vers le bas à droite
    stylo.goto(3*arrete/2, arrete/2)
    stylo.goto(arrete, 0)

    # on se deplace vers le haut à droite
    stylo.goto(arrete, arrete)
    stylo.goto(3*arrete/2, 3*arrete/2)

    # on se deplace vers le haut, puis à gauche
    stylo.goto(arrete/2, 3*arrete/2)
    stylo.goto(0, arrete)


# ----------------------------------------------------------------------------------------------------------------------
# fonction qui dessine un hexagone
# ----------------------------------------------------------------------------------------------------------------------

def drawhexagone():
    while True:
        try:
            cote = int(input("Entrer la longueur du cote : "))
            break
        except ValueError:
            print(f"{bcolors.bcolors.FAIL}\nERROR : Votre reponse est incorrecte, veuillez rentrer un nombre !! {bcolors.bcolors.RESET}")
            print()

    fenetre = turtle.Screen()
    fenetre.bgcolor("black")
    fenetre.title("DESSINER UN HEXAGONE")
    stylo = turtle.Turtle()
    stylo.color("green")

    for _ in range(6):
        stylo.forward(cote)
        stylo.left(300)


# -----------------------------------------------------------------------------------------------------------------------
# fonction qui permet de dessiner un polygone selon le choix
# -----------------------------------------------------------------------------------------------------------------------
def rejouer():
    ch = userchoice()
    if ch in figures:

        # Option 1 dessine un triangle equilatéral
        if ch == "1":
            drawtriangle()
            initwindows()

        # Option 2 dessine un carré
        elif ch == "2":
            drawsquarre()
            initwindows()

        # Option 2 dessine un rectangle
        elif ch == "3":
            drawrectangle()
            initwindows()

        # Option 3 dessine un cercle
        elif ch == "4":
            drawcircle()
            initwindows()

        # Option 4 dessine un cube 3D
        elif ch == "5":
            drawcube()
            initwindows()

        # Option 6 dessine un hexagone
        elif ch == "6":
            drawhexagone()
            initwindows()
        userdraw()
    else:
        userdraw()


# appel de la fonction pour dessiner
rejouer()
