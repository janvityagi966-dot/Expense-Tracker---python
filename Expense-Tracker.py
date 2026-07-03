print("******Welcome to Expense Tracker******")
print("Here You Can Manage Your All Expenses Efficiently")
ExpensesList=[]
while(True):
    print("======MENU=======")
    print("1. ADD EXPENSE")
    print("2. VIEW ALL EXPENSES")
    print("3. VIEW TOTAL EXPENSE")
    print("4. Exit")
    choice=int(input("Enter Your Choice..."))
    #Add Expense
    if(choice==1):
        date=input("Enter Date of Expense: ")
        category=input("Enter type of Expense(like Food,Clothes,Insurance,Education,Others): ")
        Description=input("Enter More Details: ")
        Amount=float(input("Enter the Amount: "))   
        Expense={ "Date":date,
                 "category":category,
                 "Description":Description,
                 "Amount":Amount
                 }     
        ExpensesList.append(Expense)
        print("\n *****Expense added Successfully****")
        #View all Expenses
    elif(choice==2):
        if(len(ExpensesList)==0):
            print("No Expenses")
        else:
            print("*****Here are given all your Expenses*****")
            count=1
            for EachExpense in ExpensesList:
                print(f"Expense Number {count} -> Date: {EachExpense['Date']}, Category: {EachExpense['category']}, Description: {EachExpense['Description']}, Amount: {EachExpense['Amount']}")
                count += 1
        #View total Expense
    elif(choice==3):
        total=0
        for EachExpense in ExpensesList:
            total=total+EachExpense["Amount"]
        print("Total Expense=",total)
    #Exit
    elif(choice==4):
        print("****Thanks for using our System****")
        break
    else:
        print("=====Invalid Choice,Try Again=====")
        
        
                
                
