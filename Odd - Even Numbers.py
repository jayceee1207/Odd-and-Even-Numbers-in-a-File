#John Carlo Ablay
#BSCPE 1-5
#Assignment 4: Program 1
#April 22, 2023R
print("*********************************************************")
print("READING A FILE WITH NUMBERS")
print("Programmed by: John Carlo Ablay")
print("*********************************************************")
#PSEUDOCODE
#Open a file named "numbers.txt"
file_open = open("numbers.txt", "r")
#Read every line of numbers
read_content = file_open.readlines()
#Create a list where we store all the even numbers
even_nums = []
#Create a list where we store all the odd numbers
odd_nums = []
#Make a for loop for the number file
for number in read_content:
#   convert number into an integer
    integer = int(number)
#   if number is even
    if integer % 2 == 0:
#       append that number into the even numbers list
        even_nums.append(integer)
#   if number is odd
#       append that number into the odd numbers list
#open a file to store all numbers in even numbers list
#open a file to store all numbers in odd numbers list

