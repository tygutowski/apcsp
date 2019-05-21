money = []
num = 1
def getTotal():
    num = input("How many times?")
    num = int(num)
    for x in range(num):
        temp = input("")
        temp = float(temp[1:])
        money.append(temp)
def getChange():
    for x in range(len(money)):
        cash = (money[x] * 100)
        quarters = (cash/25)
        cash %= 25
        dimes = (cash/10)
        cash %= 10
        nickles = (cash/5)
        cash %= 5
        pennies = cash 
        print ("{}{} {} {} {} {} {} {} {} {}".format("$",money[x],"\nQuarters=",int(quarters),"\nDimes=",int(dimes),"\nNickles=",int(nickles),"\nPennies=",int(pennies)),"\n")
getTotal()
getChange()
