#arithmetic operators in python
# + addition, - substraction, * multiplication, / division , ()parenthesis.
# ** exponenation that shows power to something
# % modulus returns the remainder 
# // integer divison that retuns values rounded off to the nearest integer regardless of being a positive or negative

#examples 
# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print( (23+32+64)/ 3 )    # answer is 39.66
#In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. 
#One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.
#How many tiles are needed?
#You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
# Fill this in with an expression that calculates how many tiles are needed.
a = 9*7
b = 5*7
ab = (a + b)
print(ab)

# Fill this in with an expression that calculates how many tiles will be left over.
pack = 17*6
tiles = pack - ab
print(tiles)

#Variables and assignment operators
#examples
#this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall - (rainfall * 0.1)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume  = reservoir_volume + rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume + (reservoir_volume * 0.05)
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume - (reservoir_volume * 0.05)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - 2.5e5 
# print the new value of the reservoir_volume variable
print(reservoir_volume)
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
print (crs_per_rab)
#Write code to compare these densities. 
# Is the population of San Francisco more dense than that of Rio de Janeiro? 
# Print True if it is and False if not.
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
if san_francisco_pop_density > rio_de_janeiro_pop_density:
    print(True)
else:
    print(False)
#Why do you think Python uses == for checking equality rather than =?  because = is used to assign a variable.
#how to use single strings in one line of code.
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)  #3415 and tropical fruit count is a string.

#you’re going to use what you’ve learned about strings to write a logging message for a server.

#You’ll be provided with example data for a user, the time of their visit and the site they accessed. 
# You should use the variables provided and the techniques you’ve learned to print a log message 
# like this one (with the username, url, and timestamp replaced with values from the appropriate variables):
#Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"
# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username +" accessed the site " + url +  " at "  +  timestamp + ".")

#Use string concatenation and the len() function to find the length of a certain movie star's actual full name.
#  Store that length in the name_length variable. 
# Don't forget that there are spaces in between the different parts of a name!
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
name_length = len(given_name) + len(middle_names) + len(family_name) + 2
#todo: calculate how long this name is
# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

#We've just used the len function to find the length of strings. 
#What does the len function return when we give it the integer 835 instead of a string? 
#ypeError: object of type 'int' has no len(), which alludes to the fact that len only works on a "sequence 
# (such as a string, bytes, tuple, list, or range) 
# or a collection (such as a dictionary, set, or frozen set)," as per the Python documentation.
#casting, changing one data type to another
#you’ll need to change the types of the input and output data in order to get the result you want.
#Calculate and print the total sales for the week from the data provided. 
# Print out a string of the form "This week's total sales: xxx", 
#where xxx will be the actual total of all the numbers. 
# You’ll need to change the type of the input data in order to calculate that total.
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
total = str(total)
print("This week's total sales are : " + total)

#using methods .format()
print("Mohammed has {} balloons".format(27)) #output Mohammed has 27 balloons
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action)) #output Does your dog bite?
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics")) #output Maria loves math and statistics
# practice questionson string method
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
#What is the length of the string variable verse?
#What is the index of the first occurrence of the word 'and' in verse?
#What is the index of the last occurrence of the word 'you' in verse?
#What is the count of occurrences of the word 'you' in the verse?
#Version 1 of how to answer
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")
print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
#version 2 of how to answer
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")
message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."
length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')
print(message.format(length, first_idx, last_idx, count))

#Data Structures 
#Data structures are containers that organize and group data types together in different ways.

#Lists and Membership operators.
#A list contains square brackets and are separated by commas. They also contain quotes as in the case of strings.
#Examples of lists

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
print (month[0])
print(month [-1]) 
#Lists are called when using their indexes. Python uses zero based indexing, 
#this means that in indexing we always start using zero and not one hence when we call index zero in months you get the output as January
#The negative number is used to call the last item on the index and -2 is used to call the second last number etc.

#Slice and dice in lists
#When using slicing, it is important to remember that the lower index is inclusive and the upper index is exclusive.
print(month[:6]) #This print all the months from 0-5 which is Jan till June
print(month[6:]) #This prints a list of elements from July to the last month.

#Lists supports the len function, indexing and slicing.
#In lists when you use the lenth function it will return the number of elements it holds, in a string it will return the number of characters it has.

print(len(month))

#Membership operators are In and not in.
#In evaluates if object on the left side is included in object on the right side.
#not in evaluates if object on the left side is not included in object on the right side.

#more examples
list_of_colors = ['red', 'maroon', 'purple', 'green']
print(list_of_colors[1:2]) #The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.
print(list_of_colors[:2])  #To start at the beginning 
print(list_of_colors[1:]) #to get all items in the list

#In and not in can be used in boolean. Boolean is a type that returns either true or false.
print('this' in 'this is a string')
print('isa' in  'this is a string')

#Mutability and order
#Mutability is whether or  not we can change an object once its created.
#Lists are mutable while strings are immutable.

list_of_cars = ['cadillac', 'porsche','ford']
list_of_cars [0] = 'bimmer'
print(list_of_cars)

#key things to look out for is whether data types are ordered or mutable
#Order is about whether the position of an element in the object can be used to access the element. Both strings and lists are ordered.

#Quick Question 1
#Use list indexing to determine how many days are in a particular month based on the integer variable month, 
#and store that value in the integer variable num_days. For example, if month is 8, 
#num_days should be set to 31, since the eighth month, August, has 31 days.
#Remember to account for zero-based indexing!

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
#use list indexing to determine the number of days in month
number_of_days = days_in_month[month - 1] #you can use this as the solution
num_days = days_in_month[-5] #this can also be used as a solution. There are many ways this can be done.
print(num_days)
print(number_of_days)

#Quick Question 2
#Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[7:10])  #This can be used as the solution but it does not use negative.
print (eclipse_dates[-3:])

#Useful functions of a list.
#sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.
#min() returns the smallest element in a list
#max() returns the greatest element of the list
#len() returns how many elements are in a list.

#Useful functions of a list 2
#Join is a string method that takes a list of strings as an argument, 
#and returns a string consisting of the list elements joined by a separator string.
# '/n' new line

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

#Using a hyphen
name = "-".join(["García", "O'Kelly"])
print(name)

#Append method adds items to a list.
alphabets= ['a', 'b', 'c', 'd']
alphabets.append('z')
print(alphabets)

#Quick question 1 len, max, min and  lists.
#What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#Quick question 2  sorted, join and lists. 
#What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

#Quick question 3 Append and list
#What would the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
#NB Data structures are containers that include different dat types. A list is a data structure. All data structures are data types.
#NB list are ordered and mutable










