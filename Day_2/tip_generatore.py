
print("Welcome to the tip calculator!\n\n")
total = float(input("Enter total amount\n"))
tip_percent = float(input("Enter tip percentage\n"))
final_amount = total + (total*(tip_percent/100))
no_payers = int(input("How many people to split the bill with? \n"))

print(f"Amount for each person is: ${final_amount / no_payers:.2f}")