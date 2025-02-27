"""
"""
dico_dir = {"╔" : (False, True, True, False),
            "║ " : (True, False, True, False),
            "╥"  : (False, False, True, False),
            "╠" : (True, True, True, False),
            "╬" : (True, True, True, True),
            "╦" : (False, True, True, True),
            "╚" :  (True, True, False, False),
            "╣" : (True, False, True, True),
            "╩" : (True, True, False, True),
            "╝" : (True, True, False, False),
            "╗" : (False, False, True, True),
            "═" : (False, True, False, True)
            }

def fichier(map_choix):
    """
    Fonction qui permet de lire le fichier contenant le plateau

    :param path: chemin d'accès vers le fichier
    :return:
    """
    res = []
    res2 = []
    file_path = "ressources/maps/" + map_choix + ".txt"
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line[0].isalpha():
                parts = line.split()
                letter = parts[0]
                numbers = tuple(map(int, parts[1:]))
                res2.append((letter, numbers))
            donjon_row = []
            for char in line:

                if char != '\n' and not line[0].isalpha():
                    donjon_row.append(char)
            res.append(donjon_row)
    return res, res2


def grille(tab):
    """_summary_

    Args:
        tab (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = dico_dir[tab[i][j]]
    return tab
