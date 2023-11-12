#CS506_FL23_PE02_Chloe Lee
#problem1. check if N and its double exist
print("\t**** problem 1 ****")
#arrys
arr1 =[10,2,5,3]
arr2 =[7,1,14,11]
arr3 =[3,1,7,11]

#funtion to check if number's own double exist, not number itself
# double: x = 2y in any elements in the list
def checkDouble(arr):
    for i in range(len(arr)): #for loop- x
        for j in range(len(arr)):  #for loop -y
            if i != j:      # has to be different numbers between x and y
                if arr[i] == 2 * arr[j]:  # if statement: x = 2y
                    print("true")
                    return
    else: 
        print("false")  # display the result when x!= 2y or x=y in a for loopsS
 
    
checkDouble(arr1)
checkDouble(arr2)
checkDouble(arr3)

#problem2: remove duplicates from sorted array
#do not allocate extra space for another array, 
#must do by modifiying the input array: O(1) extra memory
print("\t**** problem 2****")
#list to be processed by the funtion bellow
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]


#removeDuplicate() function 
def removeDuplicates(nums):
    #for loop to iterate : i , j to compare values
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)-1): 
            j = i+1
            if nums[i] == nums[j] : #delete same values in a list with loop
                del nums[i]
        if nums.count(i)>1: #delete if there are same values in a list
            del nums[i]  
#call funtion:removeDuplicate                                   
    print(f"After remove duplicate of array : {nums}")
    print(f"The length after removing duplicate: {len(nums)}")
    print(" ")
    return 

print(f"nums1: {nums1}")
print(f"nums2: {nums2}")

#calling the function
removeDuplicates(nums1)
removeDuplicates(nums2)

#problem3.Sort tuples
print("\n\t**** problem3 ****")
input = [('452',10),('256',5),('100',20),('135',15)]
print("Input: ", input)
#function sorting()
def sorting(tup):
    #lambda function can take any number of argument, but only have one expression
    """syntax: lambda arguments: epxression"""
    tup.sort(key =lambda a: a[1]) 
    print("Sorting")
    return tup
print("Output: ", sorting(input))


#problem4:find unique values in a dictionary
print("\n\t**** problem4 ****")
sample = [{"V": "S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},
          {"VII":"S005"},{"V":"S009"},{"VII":"S007"}]

print(f"Original data: {sample}")

unique_val =[]
for dict in sample: #type: dictionary
    for val in dict.values(): 
        if val not in unique_val:
            unique_val.append(val)
print("Unique Values in sample: ")
print(unique_val)   #result would be a list type []

#tried w/ different approach to solve as result type {} -set
myset =set()
for i in sample:
    myset1 = set(i.values())
    myset |= myset1
     
print(myset) # result type {'set'} 
print(type(myset))
print(sorted(myset)) #sorted() function changes result to a list
    
    


        
        
        

    
   





   
    
    

