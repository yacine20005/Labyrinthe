def rotation(indice, dico, dico2):
    i = indice[0]
    j = indice[1]
    pos = dico[indice]
    x1 = pos[0]
    x2 = pos[2]
    y1 = pos[1]
    y2 = pos[3]
    milieu = ((x1 + x2) / 2, (y1 + y2) / 2)
    xa = (x1- milieu[0]) * cos(90) - (y1- milieu[1]) * sin(90) + milieu[0]
    ya = (y1 - milieu[1]) * cos(90) + (x1 - milieu[0]) * sin(90) + milieu[1]
    dico2[indice] = (xa, ya, xa + 40, ya + 40)
    fltk.efface(f'baton{i}{j}')
    fltk.ligne(xa, ya, xa, ya + 40, couleur='red', tag=f'baton{i}{j}')
    
def dessin_mur_rotatif(tab):
    for i in range(len(tab)-1):
        for j in range(len(tab[i])-1):
            fltk.rectangle(tab[i][j][0], tab[i][j][1], tab[i][j][2], tab[i][j][3], 'white', 'white')

def tab_mur_rotatif(dico):
    res = []
    for key, val in dico.items():
        mur_tab = [#(val[0]-20, val[1]+10, val[0], val[1]+20),
                   #(val[2], val[1], val[2]+20, val[1] + 20),
                   (val[2]/2, val[3], val[2]/2 + 20, val[3] + 20)

        ]
        res.append(mur_tab)
        mur_tab = []
    return res