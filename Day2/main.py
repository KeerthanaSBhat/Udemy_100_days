print("Welcome to the tip calculator!1")
bill = int(input("What was the total bill?"))
tip = int(input("How much tip will give 10,12 or 15"))
total_bill = tip+bill
split_bill = int(input("How many people to split the bill"))
final_bill = round((total_bill/split_bill),2)
print(f"Each person should pay {final_bill}")


