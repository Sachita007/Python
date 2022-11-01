print("Welcome to rollercoaster!")
hight=int(input("Enter your hight in cm: "))
#Asking for hight.
if hight>120 :
    print("You Can ride the rollercoaster.")
    #Asking for  age.
    age=int(input("What is your age in in years? "))
    #Cheaking for age rang in which they belongs.
    if age<12:
        print("Child ticket are $5.")
        bill=5
    elif age<=18:
        print("Youth ticket are  $7")
        bill=7
    else :
        print ("Adult ticket are &12.")
        bill=12
    
    #Taking Input to take Photo or not.

    want_photo=input("Do you want photo? yes or no?")

    #Adding extra $3 to bill
    if want_photo=="yes":
        print("Pay extra $3.")
        bill+=3
    print(F"Your total bill is ${bill}")
else:
    print("You cannot ride the rollercoaster.")
