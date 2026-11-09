
#Declare and initialize variables
squarefeetland = 0
acresland = 0

#Declare and initialize constant
SQUARE_FEET_PER_ACRES = 43560

#Prompt for input and assign to the proper variables
squarefeetland = float(input("Please enter the total square feet in a tract of land: "))

#Perform Calculation
acresland = round(squarefeetland / SQUARE_FEET_PER_ACRES,4)

print("Your land size is" ,squarefeetland, "square feet.")
print("That is equivalent to" ,acresland, "acres of land.")