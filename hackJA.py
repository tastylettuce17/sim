import os
import time
import random
import turtle

from turtle import *
###START OF FUNCTIONS###

score = 0

def bufChoice():
	ch = random.choice(["'There's nothing to thank me for...'", "She loved him so much. He was just as real as everybody else.", "So she lives, for a silhouette. - narrator", "Each day filled with a new adventure, your eyes twinkling against the shine of the sun, face gleaming, and my entire vision flooded with cherry blossoms.", "we gradually slipped our way into each other's hearts, that's just one of the mysterious ways of love"])
	print(ch)

def score(sco):
	tot = sco+tot

def mainMenu():
	os.system('cls')
	
	print("")
	print("")
	print("")
	print("")
	print("")
	print("                                           The Simulation")
	print("                                                      ")
	print("                                                      ")
	print("                                                      ")
	time.sleep(0.9)
	print("                                      a. Main Menu")
	time.sleep(0.1)
	print("                                      b. Chapters")
	time.sleep(0.1)
	print("                                      c. Info")
	time.sleep(0.1)
	print("                                      d. Quit")
	
	inp = input()
	
	if inp == "b":
		Chapters()
		
	elif inp == "c":
		Start()
		
	elif inp == "a":
		mainMenu()
		
	else:
		Quit()

def game1():

	#os.startfile("game1.py")
	#time.sleep(8)
	score = 0
	
	#print(score)
	#food = str(random.choice(['tmaoot', 'daebr','geg','ratdusc','ltteeuc','seeche','rrybertwsa','pebyrrars','eta','fecfoe','aspe','nbanaas','cocohteal','tolaeg',]))
	print("\n\n\n\n Grocery Unscrambling :))")
	
	print("\n\n Unscramble the food items below and keep track of your points!")
	
	ans1 = str(input("\ntmaoot: "))
	print("")
	if ans1 == "tomato":
		score = score +1
	else:
		print("wrong")
	
	ans2 = str(input("\ndaebr: "))
	print("")
	if ans2 == "bread":
		score = score +1
	else:
		print("wrong")
		
	ans3 = str(input("\ngeg: "))
	print("")
	if ans3 == "egg":
		score = score +1
	else:
		print("wrong")
		
	ans4 = str(input("\nratdusc: "))
	print("")
	if ans4 == "custard":
		score = score +1
	else:
		print("wrong")
		
	ans5 = str(input("\nltteeuc: "))
	print("")
	if ans5 == "lettuce":
		score = score +1
	else:
		print("wrong")
	s = str(score)
	
	print("Your score is: "+ s)
	
	
def game2():
	#os.startfile("game2.py")
	#time.sleep(8)
	os.system("cls")
	print("A list of books will appear. Do your best to memorize them, then write down the way they were arranged.")
	
	print("\nThe Little Prince")
	
	print("\nAlgebra and Trig, Second Edition")
	
	print("\nUnderstanding the Machine")
	
	print("\nAttack on Titan: Volume 2")
	
	print("\nThe Grapes of Wrath")
	
	print("\nCrime and Punishment")
	
	time.sleep(0.5)
	
	os.system("cls")

	print("Write the names of the following books in order: ")	
	print("\nThe Grapes of Wrath, Attack on Titan: Volume 2, Algebra and Trig, Second Edition, Understanding the Machine, The Little Price, Crime and Punishment")
	
	ord = str(input("\n\n"))
	
	if ord == "the little price, algebra and trig, second edition, understanding the machine, attack on titan: volume 2, the grapes of wrath, crime and punishment":
		print("Correct! Your score is 5")
	
def game3():
	os.startfile("game3.py")
	time.sleep(8)
	
def game4():
	os.startfile("game4.py")
	time.sleep(8)
	
def game5():
	os.startfile("game5.py")
	time.sleep(8)
	
def game6():
	os.startfile("game6.py")
	time.sleep(8)
	
def game7():
	os.startfile("game7.py")
	time.sleep(8)
	
def game8():
	os.startfile("game8.py")
	time.sleep(8)
	
def game9():
	os.startfile("game9.py")
	time.sleep(8)
	
def game10():
	os.startfile("game10.py")
	time.sleep(8)
	
def lilBuffer():
	print(".")
	time.sleep(0.1)
	print(".")
	time.sleep(0.1)
	print(".")
	time.sleep(0.1)

def chapter0():
	
	print("")
	print("")
	print("")
	print("")
	print("")
	print("                                      	   The Simulation ")
	print("")
	print("")
	print("                          A mini console game by Deepti Rao and Misha Patel")
	print("                                                  .       ")
	time.sleep(0.1)
	print("                                                  .       ")
	time.sleep(0.1)
	print("                                                  .       ")
	time.sleep(0.2)
	print("                         A story told through poems and user interaction.")
	print("                                                      ")
	
	c = str(input("Continue?"))
	if c == "y" or c == "yes":
		Chapters()
	else:
		mainMenu()
	

def prol():
	os.startfile("IsabellasLullaby.mp3")
	print("I wonder where he is now...")
	time.sleep(0.3)
	print("\nIt hurts, not knowing what to do. It hurts being out of place.")
	input()
	print("\nNo matter how hard we try to distance ourselves, no matter how far you've gone, you can't escape. \nA thread is there tying you back to your past. The thinnest strin, invisible to the eye, holding the strongest pull on a being.")
	time.sleep(.2)
	print("\nIsn't it so hard, not knowing how the world works...?")
	time.sleep(.2)
	print("\nDoesn't it hurt sometimes, knowing there's so much more?\n\n")
	input()
	lilBuffer()
	print("\n\nHands entangled, I wonder if I'll ever get a moment like this again.")
	time.sleep(.2)
	print("\nYou turn towards me and smile.")
	input()
	print("\nWhat else is there to say?")
	time.sleep(.2)
	print("\nI think I love you. I think I always will.")
	time.sleep(.2)
	print("\nI look away, a smile on my face.")
	input()
	print("\nThe sunset shimmers down on the earth beneath it.")
	time.sleep(.2)
	print("\nEncased in honey, the world glows to its finest.")
	time.sleep(.2)
	print("\nA magnificent sight, then a cold wind blows.")
	time.sleep(.2)
	print("\nAs if warning us, there's much more to the world we know.")
	time.sleep(.2)
	lilBuffer()
	lilBuffer()
	
	c = str(input("Continue?"))
	if c == "y" or c == "yes":
		Chapters()
	else:
		mainMenu()
	

def chapter1():

	os.startfile("QuietHours.mp3")
	print("")
	print("Hair swaying with the wind, I let my arms out, and tilt my head back.")
	time.sleep(0.1)
	print("")
	print("The crisp air polluted with lies and unjust fill me as I breathe once more.")
	time.sleep(0.1)
	print("")
	print("'What a disgusting place,' I say, as I lie down on a bed of diamonds and lilies.")
	time.sleep(0.1)
	print("")
	print("I let my eyes close once more, saying goodbye once more, encasing myself in darkness.")
	time.sleep(0.1)
	print("")
	print("A blackness more pleasant than here.")
	print("")
	
	lilBuffer()
	
	print("")
	
	name = str(input("Please enter your name: "))
	
	print("")
		
	lilBuffer()
		
	print("")
	
	print("Thank you.")
	
	print("")
		
	lilBuffer()
		
	print("")
	
	time.sleep(0.5)
	os.system('cls')
	
	print("She looks at the list in her hand.")
	
	print("")
		
	lilBuffer()
		
	print("")
	
	print("So many groceries...")
	
	game1()
	
	#time.sleep(8)

	c = str(input("Continue?"))
	if c == "y" or c == "yes":
		Chapters()
	else:
		mainMenu()
	
	
	
	
	
	
def chapter2():
		print("")
		print("I see him in my dreams sometimes...")
		time.sleep(0.1)
		print("")
		print("In a place so tranquil, the lack of light warms me.")
		time.sleep(0.1)
		print("")
		print("He never talks, the man in the black suit, with his back towards me, looks at the window.")
		time.sleep(0.1)
		print("")
		print("Together, we look out the window, gazing at the stars.")
		time.sleep(0.1)
		print("")
		print("The light blinds me, yet I continue to watch,")
		print("")
		print("For I fear that he'll disappear again when my eyes close.")
		print("")
		
		lilBuffer()
		
		print("")
		
		print("Groceries done.")
		
		print("Let's rearrange some books.")
		
		print("")
		print("")
		
		print("A list of books will appear. Do your best to memorize them, then write down the way they were arranged.")
		
		game2()
		
		time.sleep(0.5)
		os.system('cls')
		
		print("She looks at the list in her hand.")
		
		print("")
			
		lilBuffer()
			
		print("")
		
		print("So many groceries...")
		
		game1()
		
		#time.sleep(8)
	
		c = str(input("Continue?"))
		if c == "y" or c == "yes":
			Chapters()
		else:
			mainMenu()
	
def chapter3():
	print("")
	print("It's hard to look people in the eyes nowadays.")
	input()
	print("")
	print("I feel so lost.")
	time.sleep(0.1)
	print("")
	print("Everybody seems to know what they're doing, they're so happy,")
	time.sleep(0.1)
	print("")
	print("And sad,")
	time.sleep(0.1)
	print("")
	print("And angry,")
	print("")
	print("And they hold hands and they read books and strive to be the best they possibly can be,")
	print("")
	print("Why can't I?")
	input()
	print("Why is this so hard?")
	print("I open my mouth, yet I can't speak.")
	input()
	print("My hand shakes as someone approaches me.")
	print("So I let go of everything.")
	print("That way, nothing more is expected of me.")
	input()
		
	lilBuffer()
	os.system("cls")
	
	i = str(input("Type in: 'Does it pain you'"))
	if i == "Does it pain you":
		print("...")
		print("Maybe it does.")
		print("Who knows.")
		print("Look outside, " + name + ", how many clouds did you see?")
		clouds = str(input(" "))
		if clouds == "5":
	 		print("How wonderful, so did I. So wonderful.")
	 		print("...")
	 		print("Am I getting better? At opening up...and expressing my feelings to others?")
	 		isShe = str(input(""))
	 		if isShe == "yes":
	 			print("...")
	 			print("Thank you.")
	 			print("I must go now.")
	 		else:
	 			print("...")
	 			print("I see.")
	 			print("I must go now.")
		else:
	 		print("Oh. My apologies...")
	 		print("I must go now.")
	 
	
	print("")
	
	lilBuffer()
	
	print("")
	
	c = str(input("Continue?"))
	if c == "y" or c == "yes":
		Chapters()
	else:
		mainMenu()
#def chapter4():
#def chapter5():
#def chapter6():
#def chapter7():
#def chapter8():
#def chapter9():
#def chapter10():
#def chapter11():
#def chapter12():

		
def Chapters():
	os.system('cls')
	os.startfile("IsabellasLullaby.mp3")
	
	
	
	time.sleep(0.9)
	print("")
	time.sleep(0.3)
	print("                                        ")
	time.sleep(0.3)
	print("                                        ")
	time.sleep(0.3)
	print("The sleeping hill awaits the pure green,")
	time.sleep(0.3)
	print("")
	time.sleep(0.3)
	print("The feeling calls that spring will soon be here pristine.")
	time.sleep(0.3)
	print("")
	time.sleep(0.3)
	print("I let the entire sky flower in my sight")
	time.sleep(0.3)
	print("")
	time.sleep(0.3)
	print("I let the world behind me spin...")
	time.sleep(0.6)
	
	print("")
	print("")
	print("")
	print("")
	
	print("// . . . C H A P T E R S")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print(".")
	time.sleep(0.5)
	print("")
	time.sleep(0.5)
	print("")
	time.sleep(0.5)
	print(" 0.  Introduction")
	time.sleep(0.2)
	print(" 1.  Prologue")
	time.sleep(0.2)
	print(" 2.  Chapter 1: ")
	time.sleep(0.2)
	print(" 3.  Chapter 2: ")
	time.sleep(0.2)
	print(" 4.  Chapter 3: ")
	time.sleep(0.2)
	print(" 5.  Chapter 4: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 6.  Chapter 5: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 7.  Chapter 6: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 8.  Chapter 7: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 9.  Chapter 8: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 10. Chapter 9: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 11. Chapter 10: STILL IN PROGRESS")
	time.sleep(0.2)
	print(" 12. Epilogue: STILL IN PROGRESS")
	
	
	Start()

def Quit():
	
	os.system('cls')
	
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print("// . . . E X I T I N G")
	exit()
	
def Start():
	
	startimp = input()
	
	os.startfile("blankNoise.mp3")
	
	if startimp == "0":
		buffer()
		#Introduction()
		chapter0()
		
	elif startimp == "1":
		buffer()
		prol()
		
	elif startimp == "2":
		buffer()
		chapter1()
		
	elif startimp == "3":
		buffer()
		chapter2()
		
	elif startimp == "4":
		buffer()
		chapter3()
		
	elif startimp == "5":
		buffer()
		print("in progress")
		#chapter4()
		
	elif startimp == "6":
		buffer()
		print("in progress")
		#chapter5()
		
	elif startimp == "7":
		buffer()
		print("in progress")	
	
	elif startimp == "8":
		buffer()
		print("in progress")
		
	elif startimp == "9":
		buffer()
		print("in progress")
		
	elif startimp == "10":
		buffer()
		print("in progress")
		
	elif startimp == "11":
		buffer()
		print("in progress")
		
	elif startimp == "12":
		buffer()
		print("in progress")
		
	else:
		print("")
		print("Not a valid option")
		
def buffer():
	
	os.system('cls')
	print("// . . . S T A R T I N G")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	bufChoice()
	#print("// . . . you will not be able to exit this game once you start, or unless you've earned privileges...")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.2)
	print(".")
	time.sleep(0.9)
	
	os.system('cls')









###MAIN###

os.system('cls')
	
print("")
print("")
print("")
print("")
print("")
print("                                           The Simulation")
print("                                                      ")
print("                                                      ")
print("                                                      ")
time.sleep(0.9)
print("                                      a. Main Menu")
time.sleep(0.1)
print("                                      b. Chapters")
time.sleep(0.1)
print("                                      c. Info")
time.sleep(0.1)
print("                                      d. Quit")

inp = input()

if inp == "b":
	Chapters()
	
elif inp == "c":
	print("c")
	chapter0()
	
elif inp == "a":
	mainMenu()
	
else:
	Quit()
	
