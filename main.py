#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n£")
tip = input("What percentage tip would you like to give?\n")
people = input("How many people to split the bill?\n")
tip_multiplier = 1 + (int(tip)/100)

each_pay = ((float(bill)/int(people)) * tip_multiplier)
# each_pay_2dp = round(each_pay, 2)
each_pay_2dp = "{:.2f}".format(each_pay)

print(f"Each person will pay £{each_pay_2dp}.")