#Declare and initialize variables
currentAge = 0
currentYear = 0000
yearFuture = 0000

#Promt for input and assign to the proper variables
currentAge = int(input("Please enter your current age: "))
currentYear = int(input("Please enter the current year: "))
yearFuture = int(input("Please enter a future year: "))

#Calculate the age in the future
ageInFuture = currentAge + (yearFuture - currentYear)

#Display the results
print("Your current age is ",currentAge, "in ",currentYear,".")
print("In the year", yearFuture, "you will be", ageInFuture, "years old.")
