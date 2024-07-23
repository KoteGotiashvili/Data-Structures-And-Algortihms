from LinkedList import LinkedList
# String reversal using recrussion
def reverse_string(input):
    if not input:
        return ""
    # this goes like that - 1 iteration - hello - [ello] + h, 2 iteration  - [llo] + e continues like that after string is " " back to stack and print reversed
    # In end iteration it goes back to stack and add strings reversed order
    return reverse_string(input[1::]) + input[0]


rev = reverse_string("hello")
str = "hello"
# :: goes to each char in string as you wish, how many steps you want
print(str[0::])
print(rev)


# Is Palindrome

def is_palindrome(string: str) -> bool:
    if len(string) in {0, 1}:
        return True
    leng = len(string) - 1
    if string[0] == string[leng]:
        # this goes like this 1 iteration - aceca then check and after find out equal continiue 2 iteration - cec then stays e and back to call stack and return true in all case
        return is_palindrome(string[1:leng])
    return False


pal = is_palindrome("rracecarr")
str = "racecar"
print(str[0:])
print(pal)


# Number To Binary Representation
def to_binary(num: int, result: str) -> str:
    if num == 0:
        return result
    result = f'{num % 2}' + result
    return to_binary(int(num / 2), result)


bin = to_binary(233, "")
print(bin)


# Natural Sum using recrusion
def print_num(number: int) -> int:
    if number in {0, 1}:
        return number
    return print_num(number - 1) + number


sum = print_num(10)
print(sum)


# Binary Search using recrusion

def binary_search(array: list, left: int, right: int, target: int) -> int:
    if left > right: # does not found
        return -1
    mid = int((right - left) / 2 + left)  # right/2 - left/2 + left = right/2 + left/2 = (right+left)/2
    if array[mid] == target:
        return mid

    if array[mid] > target:  # right half 1,2,3,4
        return binary_search(array, left, mid - 1, target)
    return binary_search(array, mid + 1, right, target)


list = [-1, 5, 7, 8, 10, 50, 100]
res = binary_search(array=list, left=0, right=len(list) - 1, target=100)
print(res)


# Fibonnacci recrusion
def fib(number: int) -> int:
    if number in {0, 1}:
        return number
    return fib(number - 1) + fib(number - 2)  # First should done left side in order to start right side recrusion call


val = fib(5)
print(val)


# Merge Sort Using Recursion - Easy
def merge_sort(array: list):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        # after dividing into sub parts
        i = j = k = 0
        while i < len(right_half) and j < len(left_half):
            if right_half[i] > left_half[j]:  # divided into i and j parts 10,25,12  4,5,6
                array[k] = left_half[j]
                j += 1
            else:
                array[k] = right_half[i]
                i += 1
            k += 1
        while j < len(left_half):
            array[k] = left_half[j]
            j += 1
            k += 1
        while i < len(right_half):
            array[k] = right_half[i]
            i += 1
            k += 1


arr = [10, 123, 32, 346, 45, 568, 87, 654]
merge_sort(arr)
print(arr)

#LinkedList reverse using recursion - in Linkedlist class Done

#




























