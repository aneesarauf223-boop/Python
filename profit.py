actual_cost =float(input("please enter the actual price of the product"))
sale_amount=float(input("please enter the sales price"))
if (sale_amount > actual_cost):
    amount= sale_amount - actual_cost
    print("tptal profit= {0}". format (amount))
else:
    print("no profit!!!")
