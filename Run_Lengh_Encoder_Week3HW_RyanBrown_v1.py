# Program : Run_Lengh_Encoder_Week3HW_RyanBrown_v1



# Libraries
#------------------
import math # for square root function
import time # for delays

# Global Variables
#------------------
segmented = []
compressed = []
compressed_bin = []
comp_cols = 0
comp_ind = 0 # compressed array index
num_last = None
seg_count = -1
seg_last = None
repeat_count = 1
quant_max = 0
buff = ''

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

# Print menu
print("\n\n")
print("  Please Select An Option  ")
print("|#########################|")
print("|   Week   2   Homework   |")
print("|#########################|")
print("|  1  | Lecture Example 1 |")
print("|-----|-------------------|")
print("|  2  | Lecture Example 2 |")
print("|-----|-------------------|")
print("|  3  | Homewrk Example 1 |")
print("|-----|-------------------|")
print("|  4  | Homewrk Example 2 |")
print("|-----|-------------------|")
print("|  5  | Test Example 1    |")
print("|-----|-------------------|")
print("|   Week   3   Homework   |")
print("|#########################|")
print("|  6  | Homewrk Example 1 |")
print("|-----|-------------------|")
print("|  7  | Homewrk Example 2 |")
print("|-----|-------------------|")
print("|  8  | Homewrk Example 3 |")
print("|-----|-------------------|")
print("|  9  | Homewrk Example 4 |")
print("|-----|-------------------|")
print("|  10 | Homewrk Example 5 |")
print("|-----|-------------------|")
print("\n\n")

# Set defualt option value
option = 0

# Make sure valid input taken
while option not in range(1,11):
    option = input("Enter An Number > ")
    #option = 5
    try:
        option = int(option)
    except Exception as e:
        print("Please select a valid option \n")
        option = 0


# Assign correct original value to menu option
original = [] # reset original value buffer
# Replace with switch/case like method
if option == 1:
    original = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1]
if option == 2:
    original = [1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1]
if option == 3:
    original = [1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0]
if option == 4:
    original = [1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1]
if option == 5:
    original = [1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0]
if option == 6:
    original = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1]
if option == 7:
    original = [1,0,1,0,1,0,1,0,1,0,1,0,1,0]
if option == 8:
    original = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1]
if option == 9:
    original = [1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]
if option == 10:
    original = [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]



# Custom Functions
#-----------------


# Split original input into segments
def segment(val):
    # Global variables
    global segmented
    global seg_count

    # Check if number seen before
    if val != num_last:
        if val != None:
            print("Segmented : ", segmented) # print diagnostic info
            segmented.append([val])
            seg_count += 1
    else:
        segmented[seg_count].append(val)


# Calculate quantity of each number (in segment)
def quantity(val,numb):
    # Global variables
    global compressed
    global quant_max
    seg_quant = len(segmented[val])
    compressed.append([numb,seg_quant])
    print("numb: ",numb," | Quantity in seg: ", compressed[val][1])

    # Update maximum quantity discovered
    if seg_quant > quant_max:
        quant_max = seg_quant

    # print diagnostic info
    print("Quant max : ", quant_max, "\n")

    
# Convert compressed output to binary    
def toBin(val,numb):
    # Global variables
    global compressed
    global compressed_bin

    # Convert to binary
    numb = format(numb, 'b').zfill(1)
    quant = format(compressed[val][1], 'b').zfill(bitsize)

    # Add to result buffer
    compressed_bin.append([numb,quant])
    # print diagnostic info
    print("numb: ",numb," | Quantity in seg (binary) : ", compressed_bin[val][1])



#                                      Main Program
#                                     --------------

# Print original message
print("\n\nOriginal : ", original,"\n")


# Segment Original Message
#--------------------------
print("\n\n<<<Segmenting>>>\n")
time.sleep(1)

# Loop through each value
for num in original:
    segment(num)

    # update last num
    num_last = num

# Print calculated segments
print("\nSegmented (Finished) : ", segmented)



# Calculate Quantities (within segemnts)
#---------------------------------------
seg_count = 0 # reset counter
print("\n\n<<<Quantity Checking>>>\n")
time.sleep(1)

# Loop throuygh each segment
for seg in segmented:
    print("Seg: ",seg)
    numb = seg[0]
    quantity(seg_count,numb)

    # update last seg
    seg_count += 1


# Calculate Quantity Bit Size
#----------------------------
seg_count = 0 # reset counter
print("\n\n<<<Calculating Bit lenght>>>\n")
time.sleep(1)


# Initialise bit size variables
bitsize = 0
size = False
count = 0
#quant_max = 8 # Diagnostic variable

# Loop through powers until suiatble size found
while (size == False): #
    power = math.pow(2,count) # Calculate power
    
    print("power :", power, " count : ", count) # print diagnostic data
    
    if (power) > quant_max: # Compatible bit size found
        bitsize = count
        break # Exit loop

    # update count value
    count += 1

# Print calculated bit size
print("Max Quantity : ", quant_max)
print("Bit size (Quantity): ", bitsize)


# Calculate Answer Into Binary Form
#-----------------------------------
print("\n\n<<<Converting To Binary>>>\n")
time.sleep(1)

# For each segment
for seg in segmented:
    numb = seg[0] # Take number value
    toBin(seg_count,numb) # call binary conversion function

    # update last seg
    seg_count += 1


# Process and display results
#----------------------------
print("\n\n<<<Result>>>\n")
time.sleep(1)

# Display binary conversion results
print("Compressed : ", compressed)
print("Compressed (Binary) : ", compressed_bin)

# Clear result variable buffers
original_string = ""
original_count = 0
compressed_string = ""
compressed_count = 0


# for each element in original message
for el in original:
    original_string += str(el) # convert to string and add to output string
    original_count += 1 # update count of original message 


# for each element in compressed message
for el in compressed_bin:
    for inner_el in el:
        compressed_string += str(inner_el)
        compressed_count += len(inner_el)
        #print("el: ", el, " el lenght ", len(el), " total lengh ", compressed_count)

# print output values and lengh
print("\nOriginal :            ", original_string, " Lenght : ", original_count)
print("Compressed (Binary) : ", compressed_string, " Lenght : ", compressed_count)


# Calculate Compression Rattio
#-----------------------------------
comp_ratio = compressed_count / original_count # compression ratio

# Displayu compression ratio
print("\nCompression Ratio :   ", comp_ratio)


# Display compression outcome (e.g. better or worse than original lengh)
if comp_ratio > 1:
    print("Compressed version is longer : WORSE\n")

if comp_ratio == 1:
    print("Compressed version is same lenght: EQUAL\n")

if comp_ratio < 1:
    print("Compressed version is shorer : BETTER\n")



# END OF PROGRAM
#---------------
time.sleep(1) # small delay
# keep text on screen to make it readable (prevent immidiate program closure)
input("Press 'ENTER' Key To Exit") # wait for enter key to end program




# Auther : Ryan Brown
# cmoss-electronics.com 



