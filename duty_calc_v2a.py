
# Libraries
#------------------
import math # for square root function
import time # for delays

# Global Variables
active_time = 0.0
active_percent = 0.0
active_power = 0.0
sleep_time = 0.0
sleep_percent = 0.0
sleep_power = 0.0
total_time = 0
values = [['T',0], ['t_Active %',0], ['t_Active ms',0], ['P_Active mW',0], ['P_Sleep mW',0]]

# Displays details of program
def introDisp():
	# Print program details
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
	time.sleep(4)

# Displaying graph non dinamicaly
def dispCycle():
	print("\n\n\n\n")
	print("                     Duty  Cycle  Diagram                  ")
	print("                     --------------------                  \n")
	print("       <--------------------------T----------------------->")
	print("                                                           ")
	print("       <-t_Active>                                         ")
	print("       ###########                                         ")
	print("       #         #                                         ")
	print("########         ######################################### ")
	print("                 <-----------------t_Sleep---------------> ")
	print("\n")

	dispValuesFilled() # display details so far

	print("\n\n")


# Displays a ASCII image of a duty cycle (Dynamic to ratio used)
def dispCycleDyn(act):
	# calculate pulse and sleep segments
	act = int(act/2)
	slp = 50 - act
	slpDash = int((slp/2)+7)

	# calculate pulse graphics
	active = [[],[]]
	sleep = [[],[]]
	for i in range(0, act+1) : active[0].append("#"); active[1].append(" ")
	for i in range(0, slp+1) : sleep[0].append("#"); sleep[1].append("-")

	# Display pulse
	print("\n\nResults :\n")
	print("       <--------------------------T---------------------->")
	print("                                                           ")
	print("       <-t_Active>                                         ")
	print("      ",''.join(active[0][:]))
	print("       #",''.join(active[1][4:]),"#")
	print("########",''.join(active[1][4:]),''.join(sleep[0]))
	print("        ",''.join(active[1][4:]),"<",''.join(sleep[1][slpDash:]),"t_Sleep",''.join(sleep[1][slpDash:]),"> ")

def dispValuesBlank():
	print("|-----------------------------------------------------------------------------|")
	print("| T : ? | t_Active % : ? | t_Active ms : ? | P_Active mw : ? | P_Sleep mw : ? |")
	print("|-----------------------------------------------------------------------------|")

def dispValuesFilled():
	global values
	dispInputs = values
	# Replace with
	for i in range(len(values)): # for each required input
		if values[i][1] == 0.0:
			dispInputs[i][1] = '?'

	dataString = "| T : " + str(dispInputs[0][1]) + " | t_Active % : " + str(dispInputs[1][1])
	dataString += " | t_Active ms : " + str(dispInputs[2][1]) + " | P_Active mw : " + str(dispInputs[3][1])
	dataString += " | P_Sleep mw : " + str(dispInputs[4][1]) + " |"

	dataBox = "|"
	for i in range(0,len(dataString)-2): dataBox += "-"
	dataBox += "|"

	print(dataBox)
	print(dataString)
	print(dataBox)


def valueGetter():
	dispCycle()
	userInputs = [['T',0], ['t_Active %',0], ['t_Active ms',0], ['P_Active mW',0], ['P_Sleep mW',0]]
	print("Please enter for the values below:")

	for i in range(len(userInputs)): # for each required input
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


def calcPowers():
	global active_power
	global sleep_power
	
	active_power = values[3][1]
	sleep_power = values[4][1]

def calcSleep():
	global total_time
	global active_time
	global active_percent
	global sleep_time
	global sleep_percent

	total_time = values[0][1]
	active_percent = values[1][1]
	active_time = values[2][1]

	sleep_time = total_time - active_time
	sleep_percent = 100 - active_percent


def calcPowerAvg():
	global total_time
	global active_time
	global active_percent
	global sleep_time
	global sleep_percent
	global active_percent

	p_avg = ((active_power*active_time) + (sleep_power*sleep_time)) / total_time

	dispCycleDyn(active_percent)
	dispValuesFilled()

	print("\n\n<Average Power> : ", p_avg, "mW")


def looper():
	global values
	values = valueGetter() # get values to claculate with

	calcPowers()
	calcSleep()
	calcPowerAvg()

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