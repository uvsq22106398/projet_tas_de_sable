
#######################
# import des librairies
import tkinter as tk
import random as rd


############################
# Définition des constantes
LARGEUR=100
LONGUEUR= 100

############################
# Definition des variables globale
list3 = []



############################
# Boucles

for i in range(9):
    a = rd.randint(1,9)
    list3.append(a)


#######################
# fonctions


#def configuration():
   # Matrice = []
    #for j in range(3):
       #col = []
       #for i in range(3):
           #col.append(0)
       #Matrice.append(col)

    #for col in Matrice:
         #for elem in col:
            #print(elem, end = " ")
         #print()



#######################
# programme principal
# définition des widgets
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, width=LARGEUR, height=LONGUEUR)
canvas.grid()
label1 = tk.Label(racine, text=str(list3[0]))
label2 = tk.Label(racine, text=str(list3[1]))
label3 = tk.Label(racine, text=str(list3[2]))
label4 = tk.Label(racine, text=str(list3[3]))
label5 = tk.Label(racine, text=str(list3[4]))
label6 = tk.Label(racine, text=str(list3[5]))
label7 = tk.Label(racine, text=str(list3[6]))
label8 = tk.Label(racine, text=str(list3[7]))
label9 = tk.Label(racine, text=str(list3[8]))

list2 = [label1,label2,label3,label4,label5,label6,label7,label8,label9]
def refresh_court():
    for i in range(9):
        b = rd.randint(1, 9)
        list2[i].config(text=str(b))



button1=tk.Button(racine, text='generer',command=refresh_court())

# placement des widgets
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=1, column=0)
label5.grid(row=1, column=1)
label6.grid(row=1, column=2)
label7.grid(row=2, column=0)
label8.grid(row=2, column=1)
label9.grid(row=2, column=2)
button1.grid(row=3, column=1)

# boucle principale
racine.mainloop()