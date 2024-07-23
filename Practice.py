from typing import Set, Any
#1 Done
def single_number(nums:list) -> int:
    # List where is numbers and there is only one which occurs once find this
    # [1,1,2,2,3,3,4,5,4]
    duplicates = []
    # Two pointer
    for k in range(len(nums) -1 ):
        if nums[k] == nums[k+1]:
            duplicates.append(nums[k])
    answer = list(set(nums) - set(duplicates))
    return answer[0]


num = [1,1,2,2,3,3,11,4,4,5,5,8,8]
res = single_number(num)
print(res)


#2 Done
# 1,5,10,20,50
def min_split(money):
    #return minimum amount of  1,5,10,20,50 to get money
    # return minimum amount of monets to get money
    # 139 - 50, 50, 20, 10, 5, 1, 1, 1, 1
    list = [50, 20, 10, 5, 1]
    count = 0
    for i in range(len(list)):
        while money >= list[i]:
            money = money - list[i]
            count+=1

    return count


min = min_split(149)
print(min)

#3 Done
# list contains whole numbers, write function which returns minimum whole number which is greater than zero and not in this list
def not_contains(array: list) -> int:
    # [-1,1,1,-1,2,5,6,7,5,12]
    # 0> first check [1,1,2,5,6,7,5,12]
    positive_numbers=[i for i in array if i>0]
    min=99999
    # minimum which is not in this list - second check is 3 - go whole array and find minimum
    for num in positive_numbers:
        if num < min:
            min=num

    # then check if there is something greater than that minimum if not return minimum + 1, otherwise update minimum until find
    positive_not_in_list=0
    count = 1
    for i in range(len(positive_numbers) - 1):
        if positive_numbers[i] == min+count:
            count += 1
            positive_not_in_list=min+count
    return positive_not_in_list

    # number which is not in the list and is minimum
    # Any Better Solution - ?
    # turn into set - remove duplicates - more memory allocation - con - possibly less array to iterate if duplicates

arr=[1,2,3,4,5,6,-1,-57,1,5,7,8,2]
notin = not_contains(arr)
print(notin)

#4 - Do in kutaisi
# There is two binary string return sum of them
def binary_sum(a:str,b:str) -> str:
    # example a="1010" b="1011" sum is "10101"
    # 1010
    # 1011
    # 10101
    # 1 -> convert to number, find sum, return binary - easier
    # 2 -> find patterns - hard
    pass

# 5
# There is floor we can go on ther by 1 or 2 step - count all possible steps in n-floor
# n= 1, 1 variation
# n =2, 2 variation
# n = 3 - 1,1,1 - 1,2 - 2,1 - 3 variation
# n = 4 - 1,1,1,1 -2,2 - 1,2,1 - 2, 1, 1 - 1,1,2 - 5 variation
# n = 5 - 1,1,1,1,1 - 2,2,1 - 1,2,2 - 1,1,1,2 - 1,1,2,1 - 1,2,1,1 - 2,1,1,1 - 7
# sum up given number n using 1,2 seperately
def count(n:int) -> int:
    if n in {1,2,3}:
        return n
    steps = [1, 2]
    count = 0
    # sum up different variation of 1,2 given n
    pass











