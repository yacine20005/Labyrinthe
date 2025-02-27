# Description: Module contenant les fonctions nécessaires à la manipualtion du plateau de jeu
def data(tab):
    """Extrait les données d'une table donnée et renvoie un dictionnaire pour l'aventurier et une liste de dictionnaires pour les dragons.

    Args:
        tab (list): Une table contenant des informations sur l'aventurier et les dragons.

    Returns:
        tuple: Un tuple contenant un dictionnaire pour l'aventurier et une liste de dictionnaires pour les dragons.
    """
    aventurier = {}
    lst_dragon = []
    for i in range(len(tab)):
        if tab[i][0] == 'A':
            aventurier['position'] = tab[i][1]
            aventurier['niveau'] = 1
        else:
            dico = {}
            dico['position'] = (tab[i][1][0], tab[i][1][1])
            dico['niveau'] = tab[i][1][2]
            lst_dragon.append(dico)
    return aventurier, lst_dragon


def pivoter(donjon, pos):
    """Fait pivoter une salle du donjon.

    Args:
        donjon (list): Le donjon représenté sous forme d'une liste
        pos (tuple): La position de la salle à pivoter.

    Returns:
        list: Le donjon mis à jour avec la salle pivotée.
    """
    indice_x, indice_y = pos[0], pos[1]
    tuple_dir = donjon[indice_x][indice_y]
    tuple_dir = tuple_dir[-1:] + tuple_dir[:-1]
    donjon[indice_x][indice_y] = tuple_dir
    return donjon


def connecte(donjon, pos1, pos2):
    """Vérifie si deux positions dans le donjon sont connectées.

    Args:
        donjon (list): Le donjon représenté sous forme d'une liste.
        pos1 (tuple): La première position à vérifier.
        pos2 (tuple): La deuxième position à vérifier.

    Returns:
        bool: True si les deux positions sont connectées, False sinon.
    """
    tuple1 = donjon[pos1[0]][pos1[1]]
    tuple2 = donjon[pos2[0]][pos2[1]]
    if tuple1[1] and tuple2[3]:
        return True
    if tuple1[2] and tuple2[0]:
        return True
    return False


def intention(donjon, position, dragons, visited=None):
    """
    Si position correspond à la position d’un dragon de niveau niveau, répondre
    ([position],niveau) : on a trouvé un chemin trivial pour atteindre un dragon de
    niveau niveau.
    2. Si la position est déjà dans visite, répondre None. Cette position à déjà été considérée, on
    interrompt la recherche.
    3. On ajoute position dans visite.
    4. On lance récursivement la recherche sur chaque position cible connectée à position, et on
    récupère les couples (chemin, niveau) ainsi obtenus.
    5. Si aucune recherche n’a produit un couple (chemin, niveau), on déduit qu’il n’y a pas de
    dragon accessible à partir de la position donnée, et on renvoie None.
    6. Sinon, on récupère le couple (chemin, niveau) de plus haut niveau, et on renvoie ([position]
    + chemin, niveau) : niveau est le niveau du dragon accessible le plus fort, et on a trouvé le
    chemin [position] + chemin pour l’atteindre.
    """
    print(position)
    if visited is None:
        visited = set()

    if position in visited:
        return None
    else:
        visited.add(position)

        # Coordonnées des voisins possibles (haut, droite, bas, gauche)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dir_row, dir_col in directions:
            new_row, new_col = position[0] + dir_row, position[1] + dir_col


            if 0 <= new_row < len(donjon) and 0 <= new_col < len(donjon[0]):

                if connecte(donjon, position, (new_row, new_col)):
                    for dragon in dragons:
                        if (new_row, new_col) == dragon['position']:
                            return ([position, (new_row, new_col)], dragon['niveau'])


                    result = intention(donjon, (new_row, new_col), dragons, visited)

                    if result is not None:
                        return ([position] + result[0], result[1])

        return None
