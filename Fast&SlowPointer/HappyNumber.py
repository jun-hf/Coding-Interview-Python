"""
Write a function that can determine that input is a happy number

Design:
def is_happy_number(num):
    slow = num
    fast = num

    while fast != 1:
        slow = square(slow)
        fast = square(square(fast))

        if slow == fast:
            return False
    
    return True

def square(num):

    result = 0
    12 

    12 / 10 = 1
    12 % 10 = 2

    in this case: 1*10 + 2 = 12
    second_element = num / 10
    first_element = num % 10 

    result = second_element * second_element + first_element * first_element



"""
def is_happy_number(num):
    slow = num 
    fast = num 

    while fast != 1:
        slow = square(slow)
        fast = square(square(fast))

        if slow == fast and (slow != 1 and fast != 1):
            return False

    return True

def square(num):
    result = 0
    while num > 0:
        digit = num % 10
        result += digit * digit
        num = num // 10
    
    return result

print(is_happy_number(100))
