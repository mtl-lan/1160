# Write another Python script that separates all values
# in the list [1,2,3,4,5,6,7,8,9] in two other lists.
# One resulting list should contain all even numbers and
# the other should contain all odd numbers.

# Method 1 - for loop
my_list = [1,2,3,4,5,6,7,8,9]
even_list = []
odd_list = []

for num in my_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(f"EvenList: {even_list}")
print(f"OddList: {odd_list}")


# Method 2 - List Comprehensions
even_list = [num for num in my_list if num % 2 == 0]
odd_list = [num for num in my_list if num % 2 != 0]
print(f"EvenList: {even_list}")
print(f"OddList: {odd_list}")

