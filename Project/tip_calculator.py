print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=float(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_tip=bill*tip/100
total_bill=bill+total_tip
people=int(input("How many people to split the bill?"))
print(f"Each person would pay:${round(total_bill/people,2)}")