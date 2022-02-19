name=input(" please enter your name")
print(f" hello {name}")
print("enter your choice")
print("1 addition")
print("2 subtraction")
print("3 multiplication")
print(" 4 division")
print(" 5 modulus")
choice=input("enter your choice:")
n1=int(input("enter first choice"))
n2=int(input("enter second choice"))
if choice=="1":
    print(n1, "+",n2,"=",(n1+n2))
elif choice=="2":
    print(n1, "-",n2,"=",(n1-n2))
elif choice=="3":
    print(n1, "*" ,n2,"=", (n1*n2))
elif choice=="4":
    if n2==0:
        print("number can't be divided by 0")
    else:
        print(n1, "/" ,n2,"=", (n1/n2))
elif choice=="5":
    if n2=="0":
        print("number can't be divided by 0")
    else:
        print(n1, "%" ,n2,"=", (n1%n2))
else:
    print("invalid input")
    

    


