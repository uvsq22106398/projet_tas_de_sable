# projet_tas_de_sable

#########################################
# groupe MIASHS 2
# XinLei YANG
# Frederique jennifer NGOMA
# MOANA MAUCLAIRE
# https://github.com/uvsq22106398/projet_tas_de_sable
#########################################


import tkinter as tk
import random as rd

LARGEUR= 100
LONGUEUR= 100

racine = tk.Tk()
racine.title("Tas de sable")

canvas = tk.Canvas(racine, width=LARGEUR, height=LONGUEUR)
canvas.grid()

label1 = tk.Label(racine, text='x')
label2 = tk.Label(racine, text='x')
label3 = tk.Label(racine, text='x')
label4 = tk.Label(racine, text='x')
label5 = tk.Label(racine, text='x')
label6 = tk.Label(racine, text='x')
label7 = tk.Label(racine, text='x')
label8 = tk.Label(racine, text='x')
label9 = tk.Label(racine, text='x')


def configuration():
    Matrice = []
    for j in range(3):
       col = []
       for i in range(3):
           col.append(0)
       Matrice.append(col)

    for col in Matrice:
         for elem in col:
            print(elem, end = " ")
         print()


button= tk.Button(racine, text= "configurer",font=("helvetica", "20"), command= configuration)
button.grid(column=1, row=3)
label1.grid(column=0,row=0)
label2.grid(column=1,row=0)
label3.grid(column=2,row=0)
label4.grid(column=1,row=0)
label5.grid(column=1,row=1)
label6.grid(column=1,row=2)
label7.grid(column=2,row=0)
label8.grid(column=2,row=1)
label9.grid(column=2,row=2)







#label1 = tk.Label(racine, text='x')
#label2 = tk.Label(racine, text='x')
#label3 = tk.Label(racine, text='x')
#label4 = tk.Label(racine, text='x')
#label5 = tk.Label(racine, text='x')
#label6 = tk.Label(racine, text='x')
#label7 = tk.Label(racine, text='x')
#label8 = tk.Label(racine, text='x')
#label9 = tk.Label(racine, text='x')

list2 = [label1,label2,label3,label4,label5,label6,label7,label8,label9]
list3 = []

for i in range(9):
    a = rd.randint(1,9)
    list3.append(a)


#def generer_terrain():

    #for i in range(9):
        #list2[i].config(text=str(list3[i]))
    

#button1=tk.Button(racine, text='generer',command=generer_terrain)
#label1.grid(column=0,row=0)
#label2.grid(column=1,row=0)
#label3.grid(column=2,row=0)
#label4.grid(column=0,row=1)
#label5.grid(column=1,row=1)
#label6.grid(column=2,row=1)
#label7.grid(column=0,row=2)
#label8.grid(column=1,row=2)
#label9.grid(column=2,row=2)
#button1.grid(column=3,row=0)



racine.mainloop()