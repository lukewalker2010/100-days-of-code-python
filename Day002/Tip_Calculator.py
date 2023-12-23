#Tip Calculator

print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $")
tip_percent = input("What percetage tip would you like to give? 10, 12, or 15? ")
people_total = input("How many people to split the bill? ")

bill_total = float(bill_total)
tip_percent = float(tip_percent)
people_total = int(people_total)


total_per_person = (bill_total + (bill_total * (tip_percent / 100))) / people_total

print(f"Each person should pay ${total_per_person:.2f}")