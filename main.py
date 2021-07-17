# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def cal(x, y, operator):
#     return operator(x, y)

# print(cal(4, 8, subtract))

# is_admitted = False

# if(is_admitted):
#     print("Student is Admitted")
# else:
#     print("Student is NOT admitted")

# weather = "sunny"
# if weather == "rain":
#     print("bring umbrella")
# elif weather == "sunny":
#     print("bring sunglasses")
# elif weather == "snow":
#     print("bring gloves")


# > Greater than
# < Lesser than
# >= Greater than or equal to
# <= Lesser than or equal to
# == Is equal to
# != Is not equal to

# n = 1
# while n < 10:
#     n+= 1
#     print(n)

# numbers = [1,2,3,4,5,6,7]
# for number in numbers:
#     print(number)

# number = int(input("Number to check for "))
# if number % 2 == 0:
#     print(f"{number} is an EVEN number")
# else:
#     print(f"{number} is an ODD number")

# def fibonacciGenerator(0):
#     for nu

# A year is a leap year if it is evenly divisible by 4, expect that year is evenly divisble by 100, unless the year is even;y divisible by 400

# year = int(input("Input a year "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("It is a leap year")
#         else:
#             print("It is not leap year")
#     else:
#         print("It is a leap year")
# else:
#     print("It is not a  leap year")

#Pizza Orders
price = 0
print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? s, m or l ")

if size == "s" or "S":
    price += 15
elif size == "m" or "M":
    price += 20
else:
    price += 25

add_pepperoni = input("Do you want pepperoni? y or n ")
if add_pepperoni == "y" or "Y":
    if size == "s" or "S":
        price += 2
    else:
        price += 3
extra_cheese = input("Do you want extra cheese? y or n ")
if extra_cheese == "y" or "Y":
    price += 1

print(f"Your final bill is {price}")