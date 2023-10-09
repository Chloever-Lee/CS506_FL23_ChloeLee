#CS 506_PE01_Chloe Lee

print("\n******PE01_problem 1: steps reducing to Zero********")

#take input by the user 
num = input("Type non-negative integer number: ")
num = int(num) #converting to interger from string type
#create a function steps to calculate steps w/ while loop
def steps(num):
    steps =0
    while num:
        if num %2 ==0:
            num= num/2 #even number -divide by 2
        else:
            num = num -1 #odd number - substract 1
        steps += 1
    return steps #return value will be how many steps until value become 0
print(f"{steps(num)} steps") 

print("\n*******PE01_problem 2: ******************") 

#function: calculate to one digit number by summing up each digits 
def oneDigit(num):
    i =0
    while num:
        if num >= 10:
            newNum = num//10 # to make 1 digit number for  10*num
            num = newNum + num%10 #remainder: to sum with 10*num devided by 10
            i = i+ 1 #iteration: while loop
            
        elif num <10:
            return num #if one digit, no need to sum: return as one digit
    
print(oneDigit(38))
print(oneDigit(10))


print("\n*******PE01_problem3 ******************")
#Reverse string

#converting string input to a list 
exp1 = list("hello")
exp2 = list("hannah")

#function revLetter to reverse strings in a list
def revLetter(list):
    list= list[::-1] #slicing letter backward
    return list
   
print(revLetter(exp1)) #display the result w/revLetter()
print(revLetter(exp2)) #display the result w/revLetter() 

        
        


      

  