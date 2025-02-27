"""
"""
import fltk
import graphique_plateau as pl_graphique
import player
import game
import plateau as pl
import menu as mn


GAME_LOOP = False

if __name__ == '__main__':
    menu_map, choix = mn.main_menu(800)
    tab1, tab2 = pl.fichier(menu_map)
    tab = pl.grille(tab1)
    aventurier, lst_dragons = game.data(tab2)
    chemin = game.intention(tab, (0, 0), lst_dragons, None)
    dico = pl_graphique.dessin_plateau(800, 800,  tab)
    player.position(aventurier['position'], dico)

    if choix =='play':
        fltk.efface_tout()
        GAME_LOOP = True

    while GAME_LOOP:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == "Quitte":
            fltk.ferme_fenetre()

        pl_graphique.dragons_pos(lst_dragons, dico)
        #tab_co_mur = pl_graphique.tab_mur_rotatif(dico)
        #pl_graphique.dessin_mur_rotatif(tab_co_mur)
        #indice = ct.mouse_click(dico, ordonnee_souris(), abscisse_souris())
        indice = pl_graphique.hover_mouse(tab, dico)
        if tev =='Touche':
            nom_touche = fltk.touche(ev)

            if nom_touche == 'space':
                nom_touche = fltk.touche(ev)
                player.deplacement(chemin, dico)

        if indice is not None:
            tab = game.pivoter(tab, indice)
            pl_graphique.redraw_mur(indice, 800, 800, tab)
            #player.change_position(indice, dico)
            #pl_graphique.rotation(indice, dico, dico2)

        fltk.mise_a_jour()
