import random

print ("""Bienvenido al Juego BlackJack \n El Juego consiste en pedir cartas, si al retirarte, tu suma es menor a 21, ¡Ganas!.
""")

ListaNumeros = []

def GeneradorNumeroAleatorio():
 print("\nTu Carta Vale: ")
 NumeroAleatorio = random.randint(1, 13)
 ListaNumeros.append(NumeroAleatorio)
 print(NumeroAleatorio)

def Juego():
  ListaNumeros.clear()
  jugar = True
  while jugar == True:
    print("\n ¿Quieres Pedir una carta?" + " y / n ")
    eleccion = input()
    if eleccion =="y":
      GeneradorNumeroAleatorio()
      jugar = True
    elif eleccion == "n":
      jugar = False
      GanadorOperdedor()
      

def GanadorOperdedor():
  total = sum(ListaNumeros)
  print (("Tu suma es: ") + str(total))
  if total > 21:
   print ("Lo siento, perdiste")
   PreguntaNuevoJuego()
  elif total <= 21:
   print ("¡Ganaste!")
   PreguntaNuevoJuego()

def PreguntaNuevoJuego(): 
  jugar1 = True
  while jugar1 == True:
    print("\n ¿Quieres jugar de nuevo?" + " y / n ")
    eleccion = input()
    if eleccion =="y":
      Juego()
    elif eleccion == "n":
      jugar1 = False
      print ("\n Muchas Gracias por Jugar, Que vuelvas Pronto \n")
    break

Juego()


"""
while eleccion =="y":

TopeIntentos = 10

  for i in range(TopeIntentos):
    GeneradorNumeroAleatorio()

    NuevaCarta = Y
    print("Ingresa Y para Nueva Carta")

    
    SumaCartas = int(input())
    ListaNumeros.append(random.randint(1, 13))
    print(Lista)

  else

else:
  print("fin")


print("\n¡Genial! Tu primer numero es: ")

SumanCartas = int(input())

if nuevo_juego == 1:
 print("inicio del juego")
else nuevo_juego == 0:
 print ("Gracias por Jugar")
si

no

y()


import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

def play_again():
    again = raw_input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print ("Bye!")
	    exit()

def total(hand):
    total = 0
    for card in hand:
	    if card == "J" or card == "Q" or card == "K":
	        total+= 10
	    elif card == "A":
	        if total >= 11: total+= 1
	    elif total+= 11:
	    elif:
	    total += card
    return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_hand, player_hand):
	clear()
	print "The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
	print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print "Congratulations! You got a Blackjack!\n"
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print "Sorry, you lose. The dealer got a blackjack.\n"
		play_again()

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print "Congratulations! You got a Blackjack!\n"
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print "Sorry, you lose. The dealer got a blackjack.\n"
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print "Sorry. You busted. You lose.\n"
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)			   
		print "Dealer busts. You win!\n"
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
   		print "Sorry. Your score isn't higher than the dealer. You lose.\n"
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)			   
		print "Congratulations. Your score is higher than the dealer. You win\n"		

def game():
	choice = 0
	clear()
	print "WELCOME TO BLACKJACK!\n"
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	while choice != "q":
		print "The dealer is showing a " + str(dealer_hand[0])
		print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
		blackjack(dealer_hand, player_hand)
		choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
		clear()
		if choice == "h":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "s":
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "q":
			print "Bye!"
			exit()
	
if __name__ == "__main__":
   game()

import random

TopeIntentos = 10
ListaNumeros = ()

NuevoJuego = int(input())

if NuevoJuego == 1:

  SumaCartas = 0

  for i in range(TopeIntentos):
    
    NuevaCarta = Y
    print("Ingresa Y para Nueva Carta")

    
    SumaCartas = int(input())
    ListaNumeros.append(random.randint(1, 13))
    print(Lista)

else:
  print("fin")

"""