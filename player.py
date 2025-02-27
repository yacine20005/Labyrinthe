"""_summary_
"""
import fltk

def position(pos, dico):
    """_summary_

    Args:
        pos (_type_): _description_
        dico (_type_): _description_
    """
    file = 'ressources/media/Knight_s.png'
    player_pos = dico[pos]
    fltk.image(player_pos[0]+15, player_pos[1], file, largeur=30, hauteur=50, tag='joueur')

def change_position(pos, dico):
    """_summary_

    Args:
        pos (_type_): _description_
        dico (_type_): _description_
    """
    file = 'ressources/media/Knight_s.png'
    fltk.efface('joueur')
    player_pos = dico[pos]
    fltk.image(player_pos[0] + 15, player_pos[1], file, largeur=30, hauteur=50, tag='joueur')

def deplacement(chemin, dico):
    """_summary_

    Args:
        chemin (_type_): _description_
        dico (_type_): _description_
    """
    file = 'ressources/media/Knight_s.png'
    tab = chemin[0]
    for i in range(len(tab)):
        fltk.efface('joueur')
        player_pos = dico[tab[i]]
        fltk.image(player_pos[0] + 15, player_pos[1], file, largeur=30, hauteur=50, tag='joueur')

def mouse_click(dico, pos_x, pos_y):
    """_summary_

    Args:
        dico (_type_): _description_
        pos_x (_type_): _description_
        pos_y (_type_): _description_

    Returns:
        _type_: _description_
    """
    for key, value in dico.items():
        if value[0] < pos_x < value[2] and value[1] < pos_y < value[3]:
            return key
