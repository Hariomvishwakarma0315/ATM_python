amount = 40000
print("WELCOME TO XYZ BANK ATM ")
print("check your current balance press: 1")
print("deposite for press: 2")
print("withdrow for press: 3")
x = int(input("enter the number"))

match x:

    case 1:
        print("the current balance is: ",amount)

    case 2:
        a= int(input("enter the amount for deposite: "))
        b= amount + a
        print("now your current balance is: ",b)

    case 3:
        c = int(input("enter the withdrow amount"))
        if(amount < c):
            print("insufficient balance")
        d = amount - c
        print("now your current balance is: ",d)

    case _:
        print("enter a valid number")
