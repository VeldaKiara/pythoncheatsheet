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

#Tuples
#Tuples is another  container.
#It's a data type for immutable ordered sequences of elements. 
#They are often used to store related pieces of information.
#A good example is shown below.

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

#Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices.
#Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.
#Tuples can also be used to assign multiple variables in a compact way.
# A tuple is an immutable, ordered data structure that can be indexed and sliced like a list. 
# Tuples are defined by listing a sequence of elements separated by commas, optionally contained within parentheses: 
#Example

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

#Tuple unpacking is used to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.
#In our case if we will not use deimansions directly we can shorten it like this.

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

#NB Parentheses are optional when making tuples, and programmers frequently omit them if parentheses don't clarify the code.

#sets
#A set is a data type for mutable unordered collections of unique elements. 
#One application of a set is to quickly remove duplicates from a list.

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

#Lists have square brackets, tuples have brackets and sets have curly brackets.
#Sets support the in operator the same as lists do. 
#You can add elements to sets using the add method, and remove elements using the pop method, similar to lists.
#Although, when you pop an element from a set, a random element is removed.
#Remember that sets, unlike lists, are unordered so there is no "last element".
#A set is a mutable data structure - you can modify the elements in a set with methods like add and pop. A set is an unordered data structure, so you can't index and slice elements like a list; there is no sequence of positions to index with!

#ne of the key properties of a set is that it only contains unique elements. 
#So even if you create a new set with a list of elements that contains duplicates, Python will remove the duplicates when creating the set automatically.
#An example is shown below.

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

#Other operations you can perform with sets include those of mathematical sets. 
#Methods like union, intersection, and difference are easy to perform with sets, and are much faster than such operators with other containers.

#Dictionaries.
#A dictionary is a mutable data type that stores mappings of unique keys to values. They use curly brackets but when adding items use square brackets.
#Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. 
#It's not necessary for every key to have the same type! We can look up values or insert new values in the dictionary using square brackets that enclose the key.
#We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. 
#Dicts have a related method that's also useful, get. 
#get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.
#Which of the following statements about dictionaries are true? 
#A dictionary is a mutable data structure.Can be indexed using keys. its keys are unique.
#Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary.

print("carbon" in elements)
print(elements.get("dilithium"))

#Carbon is in the dictionary, so True is printed. D
#ilithium isn’t in our dictionary so None is returned by get and then printed. 
#If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program.

#identity operators.
#is	evaluates if both sides have the same identity.
#is not	evaluates if both sides have different identities.

#Example

n = elements.get("dilithium")
print(n is None)
print(n is not None)

#What happens if we look up a value that isn't in the dictionary? 
#Create a test dictionary and use the square brackets to look up a value that you haven't defined. What happens? A key erros occurs.
#Checking for equality == vs identity is.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
 
#a and b are identical and equal but a and c are equal  ut not identical.  output True, true,true and false.

#Quick question
# invalid dictionary - this should break
#room_numbers = {
    #['Freddie', 'Jen']: 403,
    #['Ned', 'Keith']: 391,
    #['Kristin', 'Jazzmyne']: 411,
    #['Eugene', 'Zach']: 395
#}
#The question above generates a hashcode error.
#TypeError: unhashable type: 'list'. In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable,
# meaning its value does not change during its lifetime. 
# This allows Python to create a unique hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values. 
# This is why Python requires us to use immutable datatypes for the keys in a dictionary.
#The lists used in the code above are NOT immutable, and thus cannot be hashed and used as dictionary keys.

#Compound Data Structures.
#We can include containers in other containers to create compound data structures.
#An example.

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)

#Collections
#When we have a group of data we can think about it as a collection (of data elements). 
#In this lesson, we have seen many different data structures that Python provides for storing, accessing and manipulating collections of data. 
#In particular, we have seen lists, sets, and dictionaries.
#list are sortable, you can add an item to a list with .append and list items are always indexed with numbers starting at 0.

#how to add is_noble_gas into the question to make is_noble_gas to helium be true while in hydrogen be false.
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

#Random Questions
#Find the number of unique words in the text.
#1.Split verse into a list of words. Hint: You can use a string method.
#2.Convert the list into a data structure that would keep only the unique elements from the list.
#3.Print the length of the container.

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
print(verse, '\n')
verse_list = verse.split() #solution to split the verse. You use the split method. 
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set =set(verse_list) # solution to get unique elements.A set stores unique items. 
print(verse_set, '\n')

#print the number of unique words
num_unique = len(verse_set) #The number in our case will be regarded as length
print(num_unique, '\n')

#How many unique words are in verse_dict?
#Is the key "breathe" in verse_dict?
#What is the first element in the list created when verse_dict is sorted by keys?
#Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. Use this list of keys to answer the next two questions as well.
#Which key (word) has the highest value in verse_dict?
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')
#find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[1]) 

#Control Flow
#If statements
#These are statements that runs or skips code based on whether a condition is true or false.
#An if statement is always followed by a condition then a colon, the next statement starts after indentation. 
# A good example is if phone_balance < 5: #This is the condition that is set
    #phone_balance += 10 #if its true(condition) this executes. If the condition is false the block is skipped
    #bank_balance -= 10 # as well as this.

#conditional statements use comparison operators such as == or =!
#if, elif, and else statements.
# in our case we had to allow the user to input the season so that the if statements may execute.

season = input("What season are we in ?")
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

#Example 

number = 186
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Example 
age = 43

# Here are the age limits for bus fares
free_up_to_age = 5
child_up_to_age = 16
senior_from_age = 60

# These lines determine the bus fare prices
concession_ticket = 2.65
adult_ticket = 3.45

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

#An if statement that lets the gamer know what they have won.
# The prizes and range are 
#Points	and Prize
#1 - 50	wooden rabbit
#51 - 150	no prize
#151 - 180	wafer-thin mint
#181 - 200	penguin

points = 165

# write your if statement here

if points <= 50:
    result = "Congratulations! You just won a wooden rabbit."
elif points <= 150:
    result = "Oh dear, no prize at this time." 
elif points <= 180:
    result = "Congratulations! you just won a wafer-thin mint."
else:
    result = "congratulations! you just won a penguin."
    
print(result)

# An exercise on guessing the number.
 #You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.
# their guess compares to the answer.
# '''
answer = 500 #provide answer
guess = 250#provide guess

if guess < answer: #provide conditional
    result = "Oops!  Your guess was too low."
elif guess > answer: #provide conditional
    result = "Oops!  Your guess was too high."
elif guess == answer: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)

#Question on tax purchase
#Depending on where an individual is from we need to tax them appropriately. 
#The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. 
#Use this information to take the amount of a purchase and the corresponding state to assure that they are taxed by the right amount.
state = "NY" #Either CA, MN, or NY
purchase_amount = 500#amount of purchase

if state == "CA":#provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif  state == "MN": #provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY": #provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

#Complex Boolean expressions.
#For example
weight = 55
height = 164
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

##if is_raining and is_sunny:
    #print("Is there a rainbow?")

##if (not unsubscribed) and (location == "USA" or location == "CAN"):
    #print("send email")
#An example of giving prizes using points and rewards
points = 174  # this input is constant

# the default prize value is None
prize = None

# use points and prize indication
if points <= 50:
    prize = "a wooden rabbit!"
elif 151<= points <=180:
    prize= "a wafer-thin mint"
elif points >= 181:
    prize= "a penguin"
     

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
    
else:
    result= "Oh dear no prize this time."

print(result)
 #Python uses two loops for loop and while loop.
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities: # city is the iteration variable, and cities is the iterable being looped over.
    print(city)
print("Done!")   
#Using the range() Function with for Loops
#range() is a built-in function used to create an iterable sequence of numbers. 
#You will frequently use range() with a for loop to repeat an action a certain number of times.
#Any variable can be used to iterate through the numbers, 
# but Python programmers conventionally use i
#range(start=0, stop, step=1)
#The range() function takes three integer arguments, the first and third of which are optional:
#The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0.
#The 'stop' argument is 1 more than the last number of the sequence. This argument must be specified.
#The 'step' argument is the difference between each number in the sequence. If unspecified, 'step' defaults to 1.

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)
#to find multiples of 5
for i in range(5, 35, 5):
    print(i)

#how to replace names to lower case and use underscores instead of spaces between names.
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)
#writing names using range
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")
print(usernames)

   
  


