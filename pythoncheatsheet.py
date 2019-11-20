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



