import tkinter as tk
import random as rd


LARGEUR= 500
LONGUEUR= 500
n = 9
Matrice = []


def configuration_aleatoire():
   global Matrice
   for j in range(3):
       col = []
       for i in range(3):
           col.append(0)
       Matrice.append(col)
       
   for col in Matrice:
      for elem in col:
         print(elem, end = " ")
      print()
      
   
 

def affiche_terrain():
    """ Affiche la configuration sur le canvas"""
    for i in range(n):
        for j in range(n):
            label = tk.Label(racine, text = str(Matrice[i][j]))


   
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, width=LARGEUR, height=LONGUEUR)
button1=tk.Button(racine, text='generer',command=configuration_aleatoire)

canvas.grid()
button1.grid()

affiche_terrain()


racine.mainloop()