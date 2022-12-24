decimal = int(input("Enter a decimal number: "))
octal = 0
ctr = 0
temp = decimal  
 
while(temp > 0):
    octal += ((temp%8)*(10**ctr))  
    temp = int(temp/8)            
    ctr += 1
       
print("Binary of {x} is: {y}".format(x=decimal,y=octal))