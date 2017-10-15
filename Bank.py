import random
class Costumer(object):
    def __init__(self,firstname,lastname,account):
        self.firstname=firstname
        self.lastname=lastname
        self.account=account
    def info(self):
        print("First Name:",self.firstname,"\nLast Name:",self.lastname,"\nAccount:",self.account)

class Bank(object):
    def __init__(self):
        self.costumer=[]
        self.numcostume=[]

def withdraw():
    global balance
    inp=int(input("How many do you want to withraw:"))
    withdraw = balance - inp
    print("Your Money:",withdraw)
    return balance
def deposit():
    global balance
    inp = int(input("How many do you want to deposit:"))
    deposit = balance + inp
    print("Your Money:",deposit)
    return balance
