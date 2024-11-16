print("welcome to the tip calculater")

bill = input("what was the total bill?")
float_bill = float(bill)

tip = input("how much tip whould u like to give? 10, 12, or 15?")
int_tip = int(tip)
people = input("how many people to split the bill?")
int_people = int(people)

tipPerPerson = ((int_tip * float_bill) / 100)
totalBill = ((tipPerPerson + float_bill) / int_people) 

print("each persone should pay:" + str(round(totalBill,2)))