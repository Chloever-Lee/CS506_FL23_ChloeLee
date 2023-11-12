#CS506_FL23_PE03: Chloe Lee

#problem1. Implement strStr()
def strStr(haystack,needle): 
    length = len(needle)
    while len(needle) >= 0:
        for i in range(len(haystack)):
            if haystack[i:i+length] == needle: 
             return i
            #will return string in for loop, if give needle is in haystack
            
            elif needle[i] in haystack[i]:
                return -1  
            #will return -1 in case only part of needle is in haystack          
        if needle == '':
            return 0
            #will return 0 , if needle is null
    else:
        return None
            

print(f"output1: {strStr('hello', 'll')}")
print(f"output2: {strStr('aaaaa','bba')}")
print(f"output3: {strStr('','')}")

""" 
Title: LeetCode: Imlement strStr()
Author:CodersCat
Date: 2022
Code Version:3
Availiability: https://coderscat.com/leetcode-implement-strstr 
"""


#problem2.Valid Anagram
print("\n")
def determine(s,t): #determine() to sort first , then compare.
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    #After sorting, 2 anagrams should have same values
    if sorted_s == sorted_t:
        print("Anagram: true")
    else:
        print("Anagram: false")

#calling determine() 
example1 = determine(s="anagram", t="nagaram")
example2 = determine(s ="cat", t= "car")

print("\n")
#problem3.longest common prefix

template1 = ["flower", "flow", "flight"]
template2 = ["dog", "racecar", "car"]

def prefix(temp):  
    if len(temp) !=0:
        #iterate: i and j to find prefix and compare
        for i in range(len(temp[0])):
            pre = temp[0][i]
            for j in range(len(temp)):
                if i == len(temp[j]) or temp[j][i] != pre:
                    return temp[0][0:i]
            #if there is no value in pre(''), return w/ ""
                if pre =='' or None:
                    return ""
    else:
        return ""
    
print(prefix(template1))
print(prefix(template2))
#however , return value "" is not showing up.#
#Could you tell me why?

print("\n")

#problem4.Adding numbers

while True:
   #iterate until input is 'q'
    print("Enter 'q' to quit")
    n = input("Enter a number: ") 
    if n == 'q':
        break  #to exit while loop
    #try..except statement: 
    #when input is number -try & error will be when input is string -execpt
    try: 
        n = int(n)  
        print("Yay,a number!")
    except ValueError:
        print("Boo, not a number! ")
print("Test complete")


