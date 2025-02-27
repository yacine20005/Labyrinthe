# Description: Module qui gère l'affichage du plateau de jeu et des dragons
import fltk

def dessin_plateau(long ,larg, tab):
    """Dessine le plateau de jeu.

    Args:
        long (int): La longueur du plateau.
        larg (int): La largeur du plateau.
        tab (list): Le tableau représentant le plateau.

    Returns:
        dict:
    """
    x: float = long / 4
    y: float = larg / 4

    dico = {}
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j][0]:
                fltk.rectangle(x, y, x + 40, y + 10, 'white', 'black', tag=f'rec{i}{j}')
                dico[(i, j)] = (x, y, x + 40, y + 10)

            if tab[i][j][1]:
                fltk.rectangle(x + 40, y, x + 50, y + 40, 'white', 'black', tag=f'rec{i}{j}')
                dico[(i, j)] = (x + 40, y, x + 50, y + 40)

            if tab[i][j][2]:
                fltk.rectangle(x, y + 40, x + 40, y + 50, 'white', 'black', tag=f'rec{i}{j}')
                dico[(i, j)] = (x + 40, y, x + 50, y + 40)

            if tab[i][j][3]:
                fltk.rectangle(x, y, x + 10, y + 40, 'white', 'black', tag=f'rec{i}{j}')
                dico[(i, j)] = (x + 40, y, x + 50, y + 40)

            x += 60
            if j == len(tab[i]) - 1:
                x = fltk.largeur_fenetre() / 4
                y += 40
    return dico

def hover_mouse(tab, dico):
    """Fonction qui permet de détecter la case survolée par la souris.

    Args:
        tab (list): La liste représentant le plateau de jeu.
        dico (dict): Le dictionnaire contenant les coordonnées des cases.

    Returns:
        tuple: Un tuple représentant les coordonnées de la case survolée.
    """
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            x, y = dico[(i, j)][0], dico[(i, j)][1]
            if x < fltk.abscisse_souris() < x + 60 and y < fltk.ordonnee_souris() < y + 40:
                return (i, j)

def redraw_mur(indice, long ,larg, tab):
    """Redessine un mur sur le plateau.

    Args:
        indice (tuple): Les coordonnées de l'indice du mur à redessiner.
        long (int): La longueur du plateau.
        larg (int): La largeur du plateau.
        tab (list): Le tableau représentant le plateau.

    Returns:
        None
    """
    i, j = indice[0], indice[1]
    fltk.efface(f'rec{i}{j}')
    dessin_plateau(long ,larg, tab)

def dragons_pos(lst, dico):
    """Place les images des dragons sur le plateau.

    Args:
        lst (list): Liste des dragons avec leurs positions.
        dico (dict): Dictionnaire des positions des cases du plateau.
    """
    file = 'ressources/media/Dragon_s.png'
    for i in range(len(lst)):
        lst_indice = lst[i]['position']
        pos = dico[lst_indice]
        fltk.image(pos[0]+15, pos[1], file,  largeur=30, hauteur=50, tag = f'dragon{i}')
