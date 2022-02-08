# projet_tas_de_sable

#########################################
# groupe MIASHS 2
# XinLei YANG
# Frederique jennifer NGOMA
# MOANA MAUCLAIRE
# https://github.com/uvsq22106398/projet_tas_de_sable
#########################################

import tkinter as tk

LARGEUR= 500
LONGUEUR= 500

racine = tk.Tk()
racine.title("Configuration aléatoire")

canvas = tk.Canvas(racine, width=LARGEUR, height=LONGUEUR)
canvas.grid()

label1 = tk.label(racine, text = "#")
label1.grid( column=0, row = 0)
label2 = tk.label(racine, text = "#")
label2.grid( column=0, row = 1)
label3 = tk.label(racine, text = "#")
label3.grid( column=0, row = 2)
label4 = tk.label(racine, text = "#")
label4.grid( column=1, row = 0)
label5 = tk.label(racine, text = "#")
label5.grid( column=1, row = 1)
label6 = tk.label(racine, text = "#")
label6.grid( column=1, row = 2)
label7 = tk.label(racine, text = "#")
label7.grid( column=2, row = 0)
label8 = tk.label(racine, text = "#")
label8.grid( column=2, row = 1)
label9 = tk.label(racine, text = "#")
label9.grid( column=2, row = 2)

#def configuration():
    #M=[]
    #for i in range(3):
        #Ligne=[]
        #for j in range(3):
            #Ligne.append(0)
        #M.append(Ligne)
    #return M


button= tk.Button(racine, text= "configurer",font=("helvetica", "20"), command= configuration)
button.grid(column=0, row=1)


racine.mainloop()