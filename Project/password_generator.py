

#Password Generator Project
import random
from re import S
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

""" #Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#password=""
#for char in range(1,nr_letters+1):
#    password+=random.choice(letters)
#for symb in range(1,nr_symbols+1):
#    password+=str(random.choice(symbols))
#for num in range(1,nr_numbers+1):
#    password+=str(random.choice(numbers))
#
#print(password)
 """

 

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list=[]                                          
for char in range(1,nr_letters+1):                    #| 
    password_list.append(random.choice(letters))      #|         
for symb in range(1,nr_symbols+1):                    #|    Choosing Random letters , symbols and numbers from the list and   
    password_list.append(random.choice(symbols))      #|    putting it into the list i.e password_list[]
for num in range(1,nr_numbers+1):                     #|     
    password_list.append(random.choice(numbers))      #|                  

random.shuffle(password_list)                          #|    shuffleing the password_list[]
password=""                                    #|   
for char in password_list:                     #|     Joining the list and making a password     
    password+=char                             #|      
     
print(f"Your password is : {password}")         

#print password




""" 
#Below Code written by me without watching solution👇
 
letter=random.sample(letters,nr_letters)    #|                    
number=random.sample(numbers,nr_numbers)    #|  Choosing random letters,symbols and numbers                
symbol=random.sample(symbols,nr_symbols)    #|                          
  
k=nr_letters+nr_symbols+nr_numbers
st1=""                             #|          
for s in letter:                   #|                                  
    st1+=s                         #|                                   
st2=""                             #|     Converting it into string and joining them                        
for s in number:                   #|       
    st2+=str(s)                    #|          
st3=""                             #|         
for s in symbol:                   #|               
    st3+=str(s)                    #|                   
password=st1+st2+st3               #|                              
shuffled=random.sample(password,k)                       #|shuffling the password
passw=""
for s in shuffled:
    passw+=s

print(passw) """