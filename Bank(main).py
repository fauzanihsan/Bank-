from Bank import *

def ch():
    print("1.Balance","2.Withdraw","3.Deposit")
    inp=input("What do you want:")
    if inp == "balance":
        print("your balance:",balance)
        return main()
    elif inp == "withdraw":
        return withdraw()
    elif inp == "deposit":
        return deposit()
    else:
        main()

def command(inp):
    costumer = 0
    if inp == "add":
        costumer_list.append(Costumer(input("First Name:"),input("Last Name:"),(input("Account:"))))
        costumer += 1
        costumer_list[-1].info()
        return ch()
    elif inp == "transaction":
        return ch()
    elif inp == "check":
        print(balance)
        print(costumer)
        return main()

def main():
    costumer = 0
    balance = 1000000
    while True:
        inp=input("Choose:")
        command(inp)
        la=input("Check again :")
        if la == "no":
            break

    print("Customer:",costumer)

print("Welcome to Bank","\n","1.Add")
costumer_list=[]
balance=1000000
costumer = 0
main()



