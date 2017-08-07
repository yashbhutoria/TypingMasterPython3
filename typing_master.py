#!/usr/bin/python3
import time
import os


"""
to provide a flash screen in the begining and
to display input file and give prompt for typing in
"""

class color:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def splashScreen():
	#splash screen for two seconds
	print(color.HEADER + "Welcome to Typing Tutor 1.0 by Yash Bhutoria" + color.ENDC)
	time.sleep(2)
	os.system("clear")	

def displayContentOf(fileName):
	# to display file content
	try:
		toType = open(fileName,"r")
		print(color.OKBLUE + toType.read() + color.ENDC )
		print(color.BOLD + "\nTYPE_THE_ABOVE_GIVEN_TEXT\n" + color.ENDC)
		toType.close()
	except:
		print(color.FAIL+ "Error File Not Found" + color.ENDC)

def takeInput():
	#Creating a new file for user input
	userInputFile = open("userInput.txt","w")
	while(True):
		curLine = input()
		if(curLine == "#end"):
			break
		userInputFile.write(curLine + "\n")
	userInputFile.close()

#provide analysis to the user


def analyse(totalTime):
	
	toType = open("testPara.txt","r")
	correctList = toType.read().replace("\n"," ").split(" ")
	userInput = open("userInput.txt","r")
	enteredList = userInput.read().replace("\n"," ").split(" ")
	
	#startin incorrect from -1 to compensate for last #end
	incorrect = -1
	
	#Here leastRange is used to avoid out of bounds error
	leastRange = min(len(enteredList),len(correctList)) 

	for i in range(leastRange):
		if(correctList[i] == enteredList[i]):
			print( color.OKGREEN + enteredList[i] + color.ENDC,end=" ")
		else:
			print( color.FAIL+ enteredList[i] + color.ENDC,end=" ")
			incorrect += 1
		if(i%10 == 0 & i != 0):
			print()

	# now the remaining part of text will be checked
	# any extra text or less is considerd to be an incorrect entry
	difference = abs( len(enteredList) - len(correctList) +  1)
	incorrect += difference
	

	if(len(enteredList) < len(correctList) - 1):
		for i in range(difference,len(correctList)):
			print(color.FAIL + correctList[i] + color.ENDC ,end=" ")
			if(i%10 == 0 & i != 0):
				print()			

	print(color.BOLD+"\nShowing Stats in 5 Seconds"+color.ENDC)
	time.sleep(5)
	os.system("clear")
	accuracyPercent = ((len(correctList) - incorrect)/len(correctList))*100
	print(color.HEADER+"___________________________________________"+color.ENDC)
	print("Accuracy :",accuracyPercent,"%")
	print("WPM : ",len(enteredList)/(totalTime/60))
	print(color.HEADER+"___________________________________________"+color.ENDC)



#Main Program

splashScreen()
displayContentOf("testPara.txt")

#record Starting Time
startingTime = time.time()

takeInput()

#calculate total time
finalTime = time.time()
totalTime = finalTime - startingTime
analyse(totalTime)

	




