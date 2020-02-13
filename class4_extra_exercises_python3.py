# The environment
print(type(1))
print(type(3.14))
print(type("Big Data!"))
print(type('Big Data!'))
print(type(True))
print(type(False))
print(type([1,2,"intruder",3]))

print(help(True))

# Numbers
## Write an equation that uses division, multiplication, an exponent, subtraction
# and an addition that is equal to 42.5.
# Assign the result to the variable result and print it.

result = 2**5 + 4*4 - 8 + 2.5
print(result)

# Strings
my_str = 'big data'
## 1. Given the string big data give two commands that can print d.
print(my_str[4])
print(my_str[-4])

## 2.Given the string big data give two commands that can print g da

print(my_str[2:6])
print(my_str[2:-2])

## 3. Reverse the string big data in two different ways
print(my_str[::-1])

rvsd_str = ''
for cha in my_str:
    rvsd_str = cha + rvsd_str
print(rvsd_str)

## Given the strings big and data, produce the string big data
str2 = "big and data"
print(str2[:3] + str2[-5:])

# Booleans
## 1. Can you write an expression that evaluates if a string is a palyndrome? i.e. 'abba' should be True and 'rock' should be False.
def evalu_str(my_str):
    return my_str[::-1] == my_str

print(evalu_str("abba"))
print(evalu_str("rock"))

# Lists
## 1. Can you replace big data with BIG DATA in the list ['a',2,['b',4,5,'big data']]
my_list = ['a',2,['b',4,5,'big data']]
my_list[2][3] = "BIG DATA"
print(my_list)

##2. What’s the difference between [1,2,3] + [4] and [1,2,3].append(4)
a = [1,2,3]
b = [4]

print(a+b) # string concatenate will create a new string, wont modify the origins.
print(a)
print(a.append(4)) # append method add the elements in place and don't return value.
print(a)

## 3. Find the unique elements in the list [3,333,333,3,3,3333,3,3333,333,3,333333,3]
my_list = [3,333,333,3,3,3333,3,3333,333,3,333333,3]
print(set(my_list))

## 4. Return all elements between(non-inclusive) 4 and 8 on the list [1,2,3,4,5,6,7,8,9]
print([1,2,3,4,5,6,7,8,9][4:7])

## 5. Return the element nested in the list [1,2,'a','b',[0,0,'nested'],5,'c']
print([1,2,'a','b',[0,0,'nested'],5,'c'][4][2])

## 6. Count the occurrences of token on the list ['rat','dog','cat','token','elephant','token','token']

from collections import Counter
word_counts = Counter(['rat','dog','cat','token','elephant','token','token'])
print(word_counts)

# Using Scripts

# Write another script called hello_script.py. It should take one number as input.
# If the number is equal to 42 print Right answer to everything.
# If the number is not 42 print wrong answer.
# If the input is not a number print Sorry, invalid input, expecting number.


try:
    input_num = int(input("Provide a number: "))
    if input_num == 42:
        print("Right answer to everything!")
    else:
        print("Wrong answer!")
except ValueError:
    print("Sorry, invalid input, expecting number!")


# Flow Control with Conditionals
## A script that receives two numbers and prints the lesser of two numbers
# if both numbers are odd, but prints the greater one if one or both numbers are even!
def number_classifier(num1, num2):
    assert type(num1) == int, "Only integer can be accepted"
    assert type(num2) == int, "Only integer cna be accepted"
    if num1 % 2 != 0 and num2 % 2 != 0:
        print(min(num1,num2))
    else:
        print(max(num1,num2))

## A script that receives two parameters and prints True
# if the sum of both is 50 or if one of the integers is 20.
# If not, prints False
def num_machine(num1,num2):
    return num1+num2 == 50 or num1 == 20 or num2 == 20
# Loops
## A script that prints the integers from 1 to 100.
# For multiples of three print “Fizz” instead , and
# for the multiples of five print “Buzz”. For numbers which are multiples of both
# print “FizzBuzz” - done in homework 4 - advanced

## Can you find the maximum or minimum integer value in a list.
target_list = [1,2,3,4,5,6,7,8,9]
num_max = max(target_list)
num_min = min(target_list)
print(num_max)
print(num_min)

## If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
total = 0
n = 1
while True:
    if n % 3 == 0 or n % 5 == 0:
        total+=n
    n+=1
    if n >= 1000:
        break
print(total)

total1 = 0
for n in range(1, 1001):
    if n % 3 == 0 or n % 5 == 0:
        total1 += n

print(total1)

# Error
# Write a script that can convert a string into an int and
# print its value and type on the console.
# If the value can’t be converted print: bad string {} couldn't be cast to int,
# correctly formatting the message.

def str_convertor(target_str):
    try:
        if int(target_str):
            print(int(target_str))
            print(type(target_str))
    except ValueError:
            print(f"bad string {target_str} couldn't be cast to int")

# Files
# Open and print the titanic train.csv file.
# Prefix the line by Male: and Female: according to the gender of the person.
# Output the prefixed text and output the final count for each.

male_num = 0
female_num = 0

file_path = "/home/rebecca/PycharmProjects/python-notebook/titanic_train.csv"
with open(file_path) as f:
    for line in f.readlines():
        if "male" in line.split(","):
            print("Male: " + line )
            male_num += 1
        elif "female" in line.split(","):
            print("Female: " + line)
            female_num += 1

print(male_num)
print(female_num)

# Fetching Files in the web and cloud
'''
Let’s also take a look of how to obtain files from urls and APIs
In Big Data, the cloud is often used as a good storage option due to its size scalability, high level of data resilience and availability
'''
# Write a script that downloads the dataset
# http://donnees.ville.montreal.qc.ca/dataset/5829b5b0-ea6f-476f-be94-bc2b8797769a/
# resource/c6f482bf-bf0f-4960-8b2f-9982c211addd/download/interventionscitoyendo.csv
# to your local computer using the techniques seen in the examples.

import urllib.request
print("Beginning file download with urllib...")
url = "http://donnees.ville.montreal.qc.ca/dataset/5829b5b0-ea6f-476f-be94-bc2b8797769a/resource/c6f482bf-bf0f-4960-8b2f-9982c211addd/download/interventionscitoyendo.csv"
urllib.request.urlretrieve(url, "/home/rebecca/interventionscitoyendo.csv" )

# Writing Files

'''
Write a script capable of reading all the lines of a csv file
It should then validate that each line has the same number of values as the header, any lines with a different number of values as the headers should be saved in a separate list
Write back to the same directory a “clean” version of the file
Write another file containing only the “invalid” lines of the file
'''

clean_list = []
invalid_list = []

file_to_read = "/home/rebecca/1.csv"
file_to_write_clean = "/home/rebecca/2.csv"
file_to_write_invalid = "/home/rebecca/3.csv"

def file_cleaner(file_path):
    with open(file_path) as f:
        header = f.readline()
        clean_list.append(header)
        invalid_list.append(header)
        for line in f.readlines():
            if len(line.split(",")) == len(header.split(",")):
                clean_list.append(line)
            else:
                invalid_list.append(line)

file_cleaner(file_to_read)

with open(file_to_write_clean, "w") as f:
    f.writelines(clean_list)

with open(file_to_write_invalid, "w") as f:
    f.writelines(invalid_list)

