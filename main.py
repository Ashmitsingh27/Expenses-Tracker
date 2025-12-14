# Expense Tracker Project

expensesList = [] # list of expends in the form of Dictionary
print("WELCOME TO EXPENSE TRACKER : ")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Amount")
    print("4. Exit")

    choice = int (input("Please Enter Your Choice : "))

    #ADD Expense
    if(choice == 1):
        date = input("Enter the Date:- ")
        category = input("Enter the Category?(Food, Travel, Books, Courses):- ")
        description = input("Enter the Details descsription:- ")
        amount = float(input("Enter the Amount:- "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE Expense is added Successfully")

#2. View all expenses
    if(choice == 2):
        if(len(expensesList)==0 ):
            print("No Expenses Added , Add a Expenses First")
        else:
            print("======Your All Expenses is here =======")
            count= 1
            for eachexpend in expensesList:
                print(f"Expend Number {count} -> {eachexpend["date"]}, {eachexpend["category"]}, {eachexpend["description"]}, {eachexpend["amount"]}")
                count = count+1

# 3. VIEW Total Spending 
    elif choice ==3:
        total =0
        for eachexpend in expensesList:
            total = total + eachexpend["amount"]

            print("\n TOTAL SPENDING = ", total)

 # 4. EXIT
    elif choice == 4:
        print("Thank You for Using My System ")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")

            




