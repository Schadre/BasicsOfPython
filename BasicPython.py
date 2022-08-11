# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name():
    prompt = "Enter Username: "
    username = input(prompt)
    return f"Hello, {username}!"
print(hello_name())
                
  

# Question 2
# Write a python function, first_odds that prints 
# the odd numbers from 1-100

def first_odds():
    for numbers in range(100):
        if numbers % 2 == 0:
            continue
        else:
            print(numbers)
print(first_odds())
                
  

# Question 3
# Please write a Python function, max_num_in_list 
# to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)
print(max_num_in_list([1,2,3,4,5,6,7]))
                
  

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100,
#  unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(2000))
  

# Question 5
# Write a function to check to see if all numbers in list 
# are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))
print(is_consecutive([0, 1, 2, 3, 4, 5]))
