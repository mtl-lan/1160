# Check if the boston housing dataset file path is really a file.
# If it is print "I have a file to process", otherwise print "Boo, no file for me."
# Read the boston housing dataset file
# Print the dataset line by line
# Modify this script by printing each line as a list of values.
# Example: The line:abc,cde,efg,1,2,3
# In the source dataset should become: ['abc','cde','efg','1','2','3']
import os.path

data_path = "/home/rebecca/PycharmProjects/python-notebook/housing.data"

if os.path.isfile(data_path):
    print("I have a file to process")

    with open(data_path) as f:
        for line in f:
            print(line, end="")
    print("\n")

    print("Now, let's print each line as a list of values: \n")

    with open(data_path) as f:
        for line in f:
            print(line.split())
else:
    print("Boo, no file for me")
    exit(1)



