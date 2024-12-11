print("Hello, welcome to the Expense tracker!")
print("log your Expenses")

expenses= []
while True:
    try: 
        amount = float(input("Enter how much you spent"))
        if amount <= 0:
            print("Invalid number")
            continue
        break
    except ValueError:
        print("Please enter a number.")

print("Categories: 1) Food  2) Transport  3) Entertainment  4) Bills  5) Other")
while True:
    category = input("Choose a category by typing 1, 2, 3, 4, or 5: ")
    if category == "1":
        category_name = "Food"
        break
    elif category == "2":
        category_name = "Transport"
        break
    elif category == "3":
        category_name = "Entertainment"
        break
    elif category == "4":
        category_name = "Bills"
        break
    elif category == "5":
        category_name = "Other"
        break
    else:
        print("The category you choose isn't available.") 
        description = input("Enter a short description of the expense: ")
        expenses.append({"amount": amount, "category": expenses,"description": description} )
print("Expense logged successfully!")      

print("Expense Summary")
if not expenses:
    print("No expenses recorded yet.")
else:
    total_spent = sum(expense["amount"] for expense in expenses)
    print(f"Total Amount Spent: ${total_spent:.2f}")

    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    
    print("Amount Spent by Category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")
    
    print("All Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ${expense['amount']:.2f} - {expense['category']} - {expense['description']}")

print("Thank you for using the Simple Expense Tracker!")