"""
"""
import fltk

def menu(dimension):
    """_summary_

    Args:
        dimension (_type_): _description_

    Returns:
        _type_: _description_
    """
    prop = int(dimension/8)
    fltk.rectangle(2*prop, 2*prop, 6*prop, 3*prop, "black")
    fltk.rectangle(2*prop, 4*prop, 6*prop, 5*prop, "black")

    fltk.texte(dimension/2, 2.5*prop, "Jouer", ancrage = "center", police = "VCR OSD Mono")
    fltk.texte(dimension/2, 4.5*prop, "Options", ancrage = "center", police = "VCR OSD Mono")
    #image(largeur = int(dimension/20), hauteur = int(dimension/20), fichier = "Menu/quitter.png",x = largeur_fenetre()-int(prop/4), y = int(prop/4), ancrage = "center")

    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if fltk.abscisse_souris()  > 2*prop and fltk.abscisse_souris() < 6*prop and fltk.ordonnee_souris() > 2*prop and fltk.ordonnee_souris() < 3*prop:
            fltk.rectangle(2*prop, 2*prop, 6*prop, 3*prop, "black", remplissage = "black", tag="rectangle")
            fltk.texte(dimension/2, 2.5*prop, "Jouer", "white", ancrage = "center", tag ="txt",police = "VCR OSD Mono")
        else:
            fltk.efface("rectangle")
            fltk.efface("txt")

        if fltk.abscisse_souris()  > 2*prop and fltk.abscisse_souris() < 6*prop and fltk.ordonnee_souris() > 4*prop and fltk.ordonnee_souris() < 5*prop:
            fltk.rectangle(2*prop, 4*prop, 6*prop, 5*prop, "black", remplissage = "black", tag="rectangle2")
            fltk.texte(dimension/2, 4.5*prop, "Options", "white", ancrage = "center", tag ="txt2",police = "VCR OSD Mono")
        else:
            fltk.efface("rectangle2")
            fltk.efface("txt2")

        if tev == "ClicGauche":
            if fltk.abscisse(ev) > 2*prop and fltk.abscisse(ev) < 6*prop and fltk.ordonnee(ev) > 2*prop and fltk.ordonnee(ev) < 3*prop:
                return 'play'
            elif fltk.abscisse(ev) > 2*prop and fltk.abscisse(ev) < 6*prop and fltk.ordonnee(ev) > 4*prop and fltk.ordonnee(ev) < 5*prop:
                fltk.efface_tout()
                break
        elif tev == 'Quitte':
            break
        fltk.mise_a_jour()
    return 'settings'


def afficher_boutons_options(dimension):
    """_summary_

    Args:
        dimension (_type_): _description_
    """
    prop = int(dimension / 12)

    fltk.rectangle(2 * prop, 2 * prop, 4 * prop, 4 * prop, "black")
    fltk.rectangle(4 * prop, 2 * prop, 6 * prop, 4 * prop, "black")
    fltk.rectangle(6 * prop, 2 * prop, 8 * prop, 4 * prop, "black")
    fltk.rectangle(8 * prop, 2 * prop, 10 * prop, 4 * prop, "black")

    fltk.texte(3 * prop, 3 * prop, "map1", ancrage="center", police="VCR OSD Mono")
    fltk.texte(5 * prop, 3 * prop, "map2", ancrage="center", police="VCR OSD Mono")
    fltk.texte(7 * prop, 3 * prop, "map3", ancrage="center", police="VCR OSD Mono")
    fltk.texte(9 * prop, 3 * prop, "map4", ancrage="center", police="VCR OSD Mono")

    fltk.rectangle(2 * prop, 2 * prop, 4 * prop, 4 * prop, "black", remplissage="black", tag="rectangle1")
    fltk.texte(3 * prop, 3 * prop, "map1", ancrage="center", couleur="white", police="VCR OSD Mono", tag="txt1")

    fltk.rectangle(2 * prop, 6 * prop, 4 * prop, 8 * prop, "black")
    fltk.rectangle(4 * prop, 6 * prop, 6 * prop, 8 * prop, "black")
    fltk.rectangle(6 * prop, 6 * prop, 8 * prop, 8 * prop, "black")
    fltk.rectangle(8 * prop, 6 * prop, 10 * prop, 8 * prop, "black")

    fltk.texte(3 * prop, 7 * prop, "4", ancrage="center", police="VCR OSD Mono")
    fltk.texte(5 * prop, 7 * prop, "6", ancrage="center", police="VCR OSD Mono")
    fltk.texte(7 * prop, 7 * prop, "8", ancrage="center", police="VCR OSD Mono")
    fltk.texte(9 * prop, 7 * prop, "10", ancrage="center", police="VCR OSD Mono")

    fltk.rectangle(2 * prop, 6 * prop, 4 * prop, 8 * prop, "black", remplissage="black", tag="rectangle5")
    fltk.texte(3 * prop, 7 * prop, "4", ancrage="center", couleur="white", police="VCR OSD Mono", tag="txt5")

    fltk.rectangle(4 * prop, 9 * prop, 8 * prop, 10 * prop)
    fltk.texte(dimension / 2, 9.5 * prop, "Jouer", ancrage="center", police="VCR OSD Mono")


def options(dimension):
    """_summary_

    Args:
        dimension (_type_): _description_

    Returns:
        _type_: _description_
    """
    prop = int(dimension/12)

    afficher_boutons_options(dimension)
    my_map = 'map_test'
    bombe = 1

    while True:

        if fltk.abscisse_souris()  > 4*prop and fltk.abscisse_souris() < 8*prop and fltk.ordonnee_souris() > 9*prop and fltk.ordonnee_souris() < 10*prop:
            fltk.rectangle(4*prop, 9*prop, 8*prop, 10*prop, "black", remplissage = "black", tag="rectangle")
            fltk.texte(dimension/2, 9.5*prop, "Jouer", "white", ancrage = "center", tag ="txt", police = "VCR OSD Mono")
        else:
            fltk.efface("rectangle")
            fltk.efface("txt")

        ev = fltk.donne_ev()
        tev= fltk.type_ev(ev)

        if tev == "ClicGauche":
            if fltk.abscisse(ev) > 4*prop and fltk.abscisse(ev) < 8*prop and fltk.ordonnee(ev) > 9*prop and fltk.ordonnee(ev) < 10*prop:
                #Lance le main ici
                fltk.efface_tout()
                break

            if fltk.abscisse(ev) > 2*prop and fltk.abscisse(ev) < 4*prop and fltk.ordonnee(ev) > 2*prop and fltk.ordonnee(ev) < 4*prop:
                effplat()
                fltk.rectangle(2*prop,2*prop,4*prop,4*prop,"black",remplissage="black", tag="rectangle1")
                fltk.texte(3*prop, 3*prop, "5*5", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt1")
                my_map = 'map_test'

            if fltk.abscisse(ev) > 4*prop and fltk.abscisse(ev) < 6*prop and fltk.ordonnee(ev) > 2*prop and fltk.ordonnee(ev) < 4*prop:
                effplat()
                fltk.rectangle(4*prop,2*prop,6*prop,4*prop,"black",remplissage="black", tag="rectangle2")
                fltk.texte(5*prop, 3*prop, "7*7", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt2")
                my_map = 'map2'

            if fltk.abscisse(ev) > 6*prop and fltk.abscisse(ev) < 8*prop and fltk.ordonnee(ev) > 2*prop and fltk.ordonnee(ev) < 4*prop:
                effplat()
                fltk.rectangle(6*prop,2*prop,8*prop,4*prop,"black",remplissage="black", tag="rectangle3")
                fltk.texte(7*prop, 3*prop, "9*9", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt3")
                my_map = 'map3'

            if fltk.abscisse(ev) > 8*prop and fltk.abscisse(ev) < 10*prop and fltk.ordonnee(ev) > 2*prop and fltk.ordonnee(ev) < 4*prop:
                effplat()
                fltk.rectangle(8*prop,2*prop,10*prop,4*prop,"black",remplissage="black", tag="rectangle4")
                fltk.texte(9*prop, 3*prop, "10*10", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt4")
                my_map = 'map4'


            if fltk.abscisse(ev) > 2*prop and fltk.abscisse(ev) < 4*prop and fltk.ordonnee(ev) > 6*prop and fltk.ordonnee(ev) < 8*prop:
                effbombe()
                fltk.rectangle(2*prop,6*prop,4*prop,8*prop,"black",remplissage="black", tag="rectangle5")
                fltk.texte(3*prop, 7*prop, "4", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt5")
                bombe = 1

            if fltk.abscisse(ev) > 4*prop and fltk.abscisse(ev) < 6*prop and fltk.ordonnee(ev) > 6*prop and fltk.ordonnee(ev) < 8*prop:
                effbombe()
                fltk.rectangle(4*prop,6*prop,6*prop,8*prop,"black",remplissage="black", tag="rectangle6")
                fltk.texte(5*prop, 7*prop, "6", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt6")
                bombe = 6

            if fltk.abscisse(ev) > 6*prop and fltk.abscisse(ev) < 8*prop and fltk.ordonnee(ev) > 6*prop and fltk.ordonnee(ev) < 8*prop:
                effbombe()
                fltk.rectangle(6*prop,6*prop,8*prop,8*prop,"black",remplissage="black", tag="rectangle7")
                fltk.texte(7*prop, 7*prop, "8", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt7")
                bombe = 8

            if fltk.abscisse(ev) > 8*prop and fltk.abscisse(ev) < 10*prop and fltk.ordonnee(ev) > 6*prop and fltk.ordonnee(ev) < 8*prop:
                effbombe()
                fltk.rectangle(8*prop,6*prop,10*prop,8*prop,"black",remplissage="black", tag="rectangle8")
                fltk.texte(9*prop, 7*prop, "10", ancrage="center",couleur = "white",police = "VCR OSD Mono", tag="txt8")

        elif tev == 'Quitte':
            break
        
        fltk.mise_a_jour()
    return my_map, 'play'


def effplat():
    """_summary_
    """
    fltk.efface("rectangle1")
    fltk.efface("txt1")
    fltk.efface("rectangle2")
    fltk.efface("txt2")
    fltk.efface("rectangle3")
    fltk.efface("txt3")
    fltk.efface("rectangle4")
    fltk.efface("txt4")

def effbombe():
    """_summary_
    """
    fltk.efface("rectangle5")
    fltk.efface("txt5")
    fltk.efface("rectangle6")
    fltk.efface("txt6")
    fltk.efface("rectangle7")
    fltk.efface("txt7")
    fltk.efface("rectangle8")
    fltk.efface("txt8")

def main_menu(dimension):
    """_summary_

    Args:
        dimension (_type_): _description_

    Returns:
        _type_: _description_
    """
    map_name = 'map_test'
    choix = menu(dimension)
    if choix == 'settings':
        plateau, choix = options(dimension)
        return plateau, choix
    if choix == 'play':
        return map_name, choix


DIMENSION = 800
fltk.cree_fenetre(DIMENSION, DIMENSION)
