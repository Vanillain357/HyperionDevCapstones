# this program helps the user calculate the total worth of their investment or the monthly repayment on a bond

# import the math library
import math

# print out a menu that will let the user decide if they want to calculate the future value of their investment or their monthly bond repayments
# the user can select either "investment" or "bond" which will take them to the relevant section
# the options are not case sensitive
# I tried using \t at first, but it didn't give me the desired output, so I found f{:<n} on a geeks4geeks post which creates a left aligned "colum"'
print("Choose either \'investment\' or \'bond\' from the menu below to proceed:\n\n"
	+ f"{'investment' :<15} - to calculate the amount of interest you'll earn on an investment.\n"
	+ f"{'bond' :<15} - to calculate the aount you'll have to pay on a home loan each month\n"
)

# get the user's input and cast it to lowercase to avoid any capitalization issues
calc_type = input(": ").lower()
	
# a conditional statement breaks the program into invest, bond, and error situations
# if "calc_type" is investment the user will be prompted for an initial investment amount, an interest rate, an investment period, 
# as well as whether they will be earning simple or compound interest 
if (calc_type == "investment"):
	initial_investment = int(input("\nHow much money will you be ivesting? "))
# the interest rate gets devided by 100 to turn it into a percentage
	interest_rate = float(input("What is the interest rate? (in %): "))/100
	period = int(input("How many years will you be investing the mony for? "))
# the user input for the type of interest is not case sensitive
	interest = input("Will you be earning \'simple\' or \'compound\' interest? ").lower()

# the user is prompted to enter either "simple" or "compound" as the type of interest
# if the user selects "simple" the total value of the investment is calculated as A = p*(1+r*t) and rounded to 2 decimal places
	if (interest == "simple"):
		total = round(initial_investment * (1 + interest_rate * period), 2)
# if the user selects "compound" the value is calculated as A = p*(1+r)**t and rounded to 2 decimals
	elif (interest == "compound"):
		total = round(initial_investment * (1 + interest_rate) ** period , 2)
# if the user inputs something else an error message is displayed
	else:
		print("Sorry, please check that you have spelled your selection correctly and try again.")

#if the user inputs one ofthe correct options it will output a sentence telling them the total value of their invstment 
	if (interest == "simple") or (interest == "compound"):
		print(f"After {period} years at a {interest} interest rate of {interest_rate*100}%, your investment will be worth R{total}!")

# if the users selects "bond" from the menu they will be prompted for the current value of the house, the interest rate, and the period over which they will pay it off
elif (calc_type == "bond"):
	value = int(input("\nWhat is the current value of the house? "))
# the interest rate is devide by 100 to make it a percentage and by 12 to make it monthly
	interest_rate =float(input("What is the fixed interest rate? (in %): "))/(100*12)
	period = int(input("Over how many months would you like to pay off the bond? "))

# the monthly interest is calculated as x = (i*P)/(1-(1+i)**(-n))
	total = round(interest_rate * value / (1 - (1 + interest_rate) ** (-period)), 2)
	
# a sentence is printed giving the user their monthly repaymnet	
	print(f"To pay off a bond of R{value} in {period} months at an interest rate of {interest_rate*100*12}, your monthly repayments would be R{total}.")

# if the user does not select a valid option from the menu a error is displayed
else:
	print("Sorry, please check that you have spelled your selection correctly and try again.")