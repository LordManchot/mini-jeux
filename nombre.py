from math import *
from random import *
print("Lordmanch0t présente")
yn=input('Bienvenue au jeu du nombre à deviner. Expliquer les règles ? (Y/N)')
if yn == "N":
    print("Très bien. Tu dois trouver un nombre entre 0 et 1000")
elif yn == "Y":
    print("Tu dois trouver un nombre entre 0 et 1000.")
    print("Tu as le droit à un nombre d'essais de ton choix.")
else :
    print("VEUILLEZ SÉLECTIONNER UNE RÉPONSE VALIDE. TANT PIS.")
# et c'est parti ! #
s = randint(0,1000)
e = input("Combien d'essais ?")
print('Tu as', int(e), "essais.")
while int(e)>0:
	n=input('Entrer un nombre :')
	if int(n) > int(s):
		print('Moins')
	elif int(n) < int(s) :
		print('Plus')
	else:
		print(" YEEEPEEE !!! C'était bien le nombre", s)
	e = int(e)-1
	print('il te reste', int(e), "essais.")
if int(e)==0:
  print("Perdu ! Le bon nombre était", int(s),".")
