print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n$"))

tip = int(input("How much tip would you like to give in percent? 10, 12, or 15?\n"))

total_people = int(input("How many people to split the bill?\n"))

each_person_pay = (total_bill + (total_bill*tip/100))/total_people

print(f"Each person should pay: ${round(each_person_pay, 2)}")
