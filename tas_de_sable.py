#########################################
# groupe MIASHS TD01
# David DAULASIM
# Adama KOUNDOUL
# Rina Andrianina RASOLONJATOVO
# Amélie COTTANCIN
# https://github.com/uvsq22000463/projet_tas_de_sable
#########################################

import random
import tkinter as tk
"creation de la fenêtre racine"
racine=tk.Tk() 
canevas = tk.Canvas(racine,height=500,width=500)
canevas.grid()
P =[]
P1 =[]
P2 = []
N=int(input("choisir un nombre")) #variable qui permet de choisir la couleur d'une case#
N1=int(input("choisir un nombre"))#variable qui permet de choisir la couleur d'une case#
N2=int(input("choisir un nombre"))#variable qui permet de choisir la couleur d'une case#
def alea() :
 "fonction qui colorie une case aleatoirement"
 global P
 
 l = random.randint(0,3) 
 if l ==0:
     "0 code pour la couleur bleu"
     canevas.create_rectangle((151,199),(189,150),fill="blue")
 elif l ==1 :
     "1 code pour la couleur cyan"
     canevas.create_rectangle((151,199),(189,150),fill="cyan")
 elif l==2 :
     "2 code pour la couleur yellow"
     canevas.create_rectangle((151,199),(189,150),fill="yellow")
 elif l==3 :
     "3 code pour la couleur orange"
     canevas.create_rectangle((151,199),(189,150),fill="orange")
 l1=random.randint(0,3)
 if l1==0:
     canevas.create_rectangle((191,150),(276,199),fill="blue")
 elif l1==1:
     canevas.create_rectangle((191,150),(276,199),fill="cyan")
 elif l1==2 :
     canevas.create_rectangle((191,150),(276,199),fill="yellow")
 elif l1==3 :
     canevas.create_rectangle((191,150),(276,199),fill="orange")
 l2=random.randint(0,3)
 if l2==0 :
     canevas.create_rectangle((277,150),(350,200),fill="blue")
 elif l2==1 :
     canevas.create_rectangle((277,150),(350,200),fill="cyan")
 elif l2==2 :
     canevas.create_rectangle((277,150),(350,200),fill="yellow")
 elif l2==3 :
     canevas.create_rectangle((277,150),(350,200),fill="orange")
 l3=random.randint(0,3)
 if l3==0 :
     canevas.create_rectangle((151,200),(189,292),fill="blue")
 elif l3==1 :
     canevas.create_rectangle((151,200),(189,292),fill="cyan")
 elif l3==2 :
     canevas.create_rectangle((151,200),(189,292),fill="yellow")
 elif l3==3 :
     canevas.create_rectangle((151,200),(189,292),fill="orange")
 l4=random.randint(0,3)
 if l4 ==0:
     canevas.create_rectangle((190,200),(275,294),fill="blue")
 elif l4==1:
     canevas.create_rectangle((190,200),(275,294),fill="cyan")
 elif l4==2 :
     canevas.create_rectangle((190,200),(275,294),fill="yellow")
 elif l4==3 :
     canevas.create_rectangle((190,200),(275,294),fill="orange")
 l5=random.randint(0,3)
 if l5 ==0:
     canevas.create_rectangle((277,199),(349,295),fill="blue")
 elif l5==1:
     canevas.create_rectangle((277,199),(349,295),fill="cyan")
 elif l5==2 :
     canevas.create_rectangle((277,199),(349,295),fill="yellow")
 elif l5==3 :
     canevas.create_rectangle((277,199),(349,295),fill="orange")
 l6=random.randint(0,3)
 if l6 ==0:
     canevas.create_rectangle((150,293),(189,350),fill="blue")
 elif l6==1 :
    canevas.create_rectangle((150,293),(189,350),fill="cyan")
 elif l6==2 :
     canevas.create_rectangle((150,293),(189,350),fill="yellow")
 elif l6==3 :
     canevas.create_rectangle((150,293),(189,350),fill="orange")
 l7=random.randint(0,3)
 if l7==0 :
     canevas.create_rectangle((191,295),(275,350),fill="blue")
 elif l7==1 :
      canevas.create_rectangle((191,295),(275,350),fill="cyan")
 elif l7==2 :
     canevas.create_rectangle((191,295),(275,350),fill="yellow")
 elif l7==3 :
   canevas.create_rectangle((191,295),(275,350),fill="orange")
 l8=random.randint(0,3)
 if l8==0 :
     canevas.create_rectangle((275,350),(350,295),fill="blue")
 elif l8==1 :
     canevas.create_rectangle((275,350),(350,295),fill="cyan")
 elif l8==2 :
     canevas.create_rectangle((275,350),(350,295),fill="yellow")
 elif l8==3 :
     canevas.create_rectangle((275,350),(350,295),fill="orange")
 P.extend([l,l1,l2,l3,l4,l5,l6,l7,l8])
 
def centre() :
 "fonction qui colorie differement les cases du centre et du bord" 
 global P1
 "pas besoin de if pour les cases du bords"
 canevas.create_rectangle((151,199),(189,150),fill="blue")
 if N==0 :
     canevas.create_rectangle((191,150),(276,199),fill="blue")
 elif N==1 :
     canevas.create_rectangle((191,150),(276,199),fill="cyan")
 elif N==2 :
     canevas.create_rectangle((191,150),(276,199),fill="yellow")
 elif N==3 :
     canevas.create_rectangle((191,150),(276,199),fill="orange")
 canevas.create_rectangle((277,150),(350,200),fill="blue")
 canevas.create_rectangle((151,200),(189,292),fill="blue")
 if N1==0 :
     canevas.create_rectangle((190,200),(275,294),fill="blue")
 elif N1==1 :
     canevas.create_rectangle((190,200),(275,294),fill="cyan")
 elif N1==2:
     canevas.create_rectangle((190,200),(275,294),fill="yellow")
 elif N1==3 :
     canevas.create_rectangle((190,200),(275,294),fill="orange")
 canevas.create_rectangle((277,199),(349,295),fill="blue")
 canevas.create_rectangle((150,293),(189,350),fill="blue")
 if N2==0:
  canevas.create_rectangle((191,295),(275,350),fill="blue")
 elif N2==1:
     canevas.create_rectangle((191,295),(275,350),fill="cyan")
 elif N2==2 :
     canevas.create_rectangle((191,295),(275,350),fill="yellow")
 elif N2==3 :
     canevas.create_rectangle((191,295),(275,350),fill="orange")
 canevas.create_rectangle((275,350),(350,295),fill="blue")
 P1.extend([0,N,0,0,N1,0,0,N2,0])
 print(P1)
def meme() :
 "fonction qui colorie les cases de la meme couleur"
 "rappel 3 code pour la couleur orange"
 global P2
 canevas.create_rectangle((151,199),(189,150),fill="orange")
 canevas.create_rectangle((191,150),(276,199),fill="orange")
 canevas.create_rectangle((277,150),(350,200),fill="orange")
 canevas.create_rectangle((151,200),(189,292),fill="orange")
 canevas.create_rectangle((190,200),(275,294),fill="orange")
 canevas.create_rectangle((277,199),(349,295),fill="orange")
 canevas.create_rectangle((150,293),(189,350),fill="orange")
 canevas.create_rectangle((191,295),(275,350),fill="orange")
 canevas.create_rectangle((275,350),(350,295),fill="orange")
 P2.extend([3,3,3,3,3,3,3,3,3])  
 print(P2)
"bouton qui appelle la fonction alea"
bouton1 = tk.Button(racine,text="aléatoire",command=alea) 
bouton1.grid(row=3,column=3)
"bouton qui appelle la fonction meme"
bouton2= tk.Button(racine,text="Max Table",command=meme)
bouton2.grid(row=1,column=0)
"bouton qui appelle la fonction centre"
bouton3=tk.Button(racine,text="pile centrée",command=centre)
bouton3.grid(row=1,column=2)
meme()
centre()
alea()
Pn=P+P1+P2
print(Pn)
def plus() :
 "fonction qui additionne 2 configurations :random et centre"
 global Pn
 if Pn[0]+Pn[9]==0 :
     canevas.create_rectangle((151,199),(189,150),fill="blue")
 elif Pn[0] +Pn[9]==1:
   canevas.create_rectangle((151,199),(189,150),fill="cyan")
 elif Pn[0] + Pn[9] ==2:
     canevas.create_rectangle((151,199),(189,150),fill="yellow")
 elif Pn[0]+Pn[9]==3 :
     canevas.create_rectangle((151,199),(189,150),fill="orange")
 else :
     canevas.create_rectangle((151,199),(189,150),fill="white")
 if Pn[1]+Pn[10]==0 :
   canevas.create_rectangle((191,150),(276,199),fill="blue")
 elif Pn[1]+Pn[10]==1:
     canevas.create_rectangle((191,150),(276,199),fill="cyan")
 elif Pn[1] +Pn[10]==2 :
     canevas.create_rectangle((191,150),(276,199),fill="yellow")
 elif Pn[1]+Pn[10]==3:
     canevas.create_rectangle((191,150),(276,199),fill="orange")
 else :
     canevas.create_rectangle((191,150),(276,199),fill="white")
 if Pn[2]+Pn[11] ==0 :
     canevas.create_rectangle((277,150),(350,200),fill="blue")
 elif Pn[2]+Pn[11] ==1 :
     canevas.create_rectangle((277,150),(350,200),fill="cyan")
 elif Pn[2]+Pn[11] ==2 :
     canevas.create_rectangle((277,150),(350,200),fill="yellow")
 elif Pn[2]+Pn[11] ==3 :
     canevas.create_rectangle((277,150),(350,200),fill="orange")
 else :
     canevas.create_rectangle((277,150),(350,200),fill="white")
 if Pn[3]+Pn[12] ==0 :
     canevas.create_rectangle((151,200),(189,292),fill="blue")
 elif Pn[3]+Pn[12] ==1 :
     canevas.create_rectangle((151,200),(189,292),fill="cyan")
 elif Pn[3]+Pn[12] ==2 :
     canevas.create_rectangle((277,150),(350,200),fill="yellow")
 elif Pn[3]+Pn[12] ==3 :
     canevas.create_rectangle((277,150),(350,200),fill="orange")
 else :
     canevas.create_rectangle((277,150),(350,200),fill="white")
bouton4= tk.Button(racine,text="adi alea et centre",command=plus) 
bouton4.grid(row=1,column=3)  
racine.mainloop()
