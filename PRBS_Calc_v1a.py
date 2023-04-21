

# Libraries
#------------------
import math # for square root function
import time # for delays

# Global Variables
#------------------
values = [['Fc (MHz)',0], ['X1^...',0], ['X2^...',0], ['N',0], ['Df (Hz)',0]]




# Print program details
#----------------------
print("\n\n")
print("|##########|###################|")
print("| Title:   | Homework Week 2   |")
print("|----------|-------------------|")
print("| Subject: | Data Compression  |")
print("|----------|-------------------|")
print("| Topic:   | Run Lenght Coding |")
print("|##########|###################|")
print("| Auther:  | Ryan Brown        |")
print("|##########|###################|")
print("\n\n")
print ("Program starting is 4 seconds...\n\n")
time.sleep(1)



def dispExample():
	print("\n\n\n\n")
	print("<Example>")
	print(" -------")
	print("")
	print("           <x1 Xor x2>       ")
	print("         -----(+)--------    ")
	print("         |     |        |    ")
	print("         |     |        |    ")
	print("         |     |        |    ") 
	print("   clk---|----[1][2][3][4][5]")
	print("                             ")
	print(" Vals: [1:1][2:0][3:1][4:0][5:1]")
	print("")
	print(" Characteristic Equation:")
	print("     Y = 1 (+) x^1 (+) x^4")
	print("")
	dispValuesBlank()



def dispValuesBlank():
	print("")
	print("|----------------------------------------------------|")
	print("| Fc MHz : ? | X1^ : ? | X2^ : ? | N : ? | Df Hz : ? |")
	print("|----------------------------------------------------|")
	print("")
	print("")



def dispValuesFilled():
	global values
	dispInputs = values
	# Replace with
	for i in range(len(values)): # for each required input
		if values[i][1] == 0.0:
			dispInputs[i][1] = '?'

	dataString = "| Fc MHz : " + str(dispInputs[0][1]) + " | X1^ : " + str(dispInputs[1][1])
	dataString += " | X2^ : " + str(dispInputs[2][1]) + " | N : " + str(dispInputs[3][1])
	dataString += " | Df Hz : " + str(dispInputs[4][1]) + " |"

	dataBox = "|"
	for i in range(0,len(dataString)-2): dataBox += "-"
	dataBox += "|"

	print("")
	print(dataBox)
	print(dataString)
	print(dataBox)
	print("")
	print("")


def valueGetter():
	dispExample()
	userInputs = [['Fc (MHz)',0], ['X1^...',0], ['X2^...',0], ['N',0], ['Df (Hz)',0]]
	print("Please enter for the values below:")

	for i in range(len(userInputs)-2): # for each required input. Last two not used here
		# Validate input as number
		acceptable = False # reset
		while acceptable == False:
			# Print question
			print("\n#", i+1, ": ", userInputs[i][0])
			# Get answer -> into buffer
			inputBuf = input("> ")

			# Validate (if can be conerted to float = pass)
			try:
				userInputs[i][1] = float(inputBuf)
				acceptable = True
			except Exception:
				print("Please select a valid option \n")

	return userInputs



def looper():
	global values

	values = valueGetter() # get values to claculate with

	dispValuesFilled()


	time.sleep(2)
	run_q = input("\nRun Again ? Y/N")

	if run_q == "Y":
		return True

	return False



# Allows for a clean end of the program without sudden closure
def end():
	# END OF PROGRAM
	#---------------
	time.sleep(1) # small delay
	# keep text on screen to make it readable (prevent immidiate program closure)
	print("\n\nYou have reached the end of this program...")
	input("Press 'ENTER' Key To Exit") # wait for enter key to end program


# Main function of the program
def main():
	#introDisp() # display intro

	runCont = True

	while runCont: # infinate loop
		runCont = looper() # where infinate loop code lives, returns whther to keep running

	end()

if __name__ == '__main__':
	main()