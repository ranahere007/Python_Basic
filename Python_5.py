#Simple Calculator


print("Sum- 1 Subtract- 2 Division- 3 Product- 4")


user=int(input("Choose which operation you want to operate:"))

st=int(input("Enter 1st number: "))
nd=int(input("Enter 2nd number: "))
         
if  user==1:
    print("Summation is ",st+nd)
elif user==2:
    print("Subtraction is ",st-nd)

elif user==3:
    print("Division is ",st/nd)
elif user==4:
    print("Product is ",st*nd)
else :
    print("Invalid input")
         



