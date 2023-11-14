import math
# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def min_to_sec(min):
    return min*60

def hrs_to_sec(hrs):
    return hrs*min_to_sec(60)

def hrs_to_min(hrs):
    return hrs*60

def day_to_sec(days):
    return days*hrs_to_sec(24)

def day_to_hrs(days):
    return days*24

# - How many Hours are in the month of June? 
# print(day_to_hrs(30))
# - How many Minutes are in the month of August?
# print(hrs_to_min(day_to_hrs(31)))
# Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
# print(hrs_to_min(day_to_hrs(365)))


#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def middle_letter(string):
    string_length = len(string)
    if string_length%2==0:
        return "no middle"
    else:
        #round_down(string_length/2) --> index of the string that we want to return
        # index = math.floor(string_length/2)
        return string[math.floor(string_length/2)]

print(middle_letter("abcefgh"))
print(middle_letter("aaaa"))


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def hide_cc_number (ccn):
    ccn_string = str(ccn)
    # for index in range(0,len(ccn_string)-4): 
    #     ccn_string[index] = "*" 
    # return ccn_string

    str_start = ""
    str_end = ""

    for index in range(0,len(ccn_string)-4):
        str_start += "*"
    for index in range(len(ccn_string)-4, len(ccn_string)):
        str_end += ccn_string[index]
    
    return str_start + str_end

# str1 = first portion of the ccn

print(hide_cc_number(5555555555555555))

def hide_credit_card(credit_card_num):    
    return '*' * (len(credit_card_num)-4) + credit_card_num[-4:]
print(hide_credit_card("5555555555555555"))


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

statuses = {
    "John": "online",
    "Paul": "online",
    "George": "online",
    "Ringo": "offline"
}

def online_count (dict):
    online_counter = 0
    for value in dict:
        if dict[value] == "online":
            # online_counter = online_counter+1
            online_counter+=1
    return online_counter
print(online_count(statuses))

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------
def discount(price,perc):
    return price*(1-perc/100)
print(discount(100,20))

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse



# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

#  c = sqrt(a^2+b^2)

def hypotenouse(a,b):
    return math.sqrt(a**2 + b**2)
print(hypotenouse(3,4))

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def fib(first, second):
    sequence = [first, second]
    for num in range(2,12):
        sequence.append(sequence[num-1]+sequence[num-2]) #explicitly calls the location

    return sequence
print(fib(0,1))

def get_fibonacci(num1, num2):
    nums = [num1, num2]
    for i in range(9):    
        nums.append(nums[-2]+nums[-1]) # calls relative to the end of the list
    return nums
print(get_fibonacci(4, 5))