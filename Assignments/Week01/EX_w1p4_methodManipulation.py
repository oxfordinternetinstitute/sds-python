"""
Example 4: Method Manipulation

# Week 1: Example Code 4: Methods

Python is an "object-oriented" language. 
This means that we work with objects, with their own properties and methods.

A method is a systematic technique for acting upon an object. 
Methods can exist by themselves or inside of a "class".
We will discuss classes and objects in a later tutorial.  
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

LB = "\n-----------------------"

# print "Remember that strings are actually lists? This makes them objects!"
# print "To find out the methods we can use on a string type dir(stringvar)" 
# newstr = "Another string" 
# print dir(newstr)
# 
# print "Now we can see there are a lot of methods, such as isspace."
# print "But if we want to create our own method, we can do that too"
# print "by saying\ndef <name> (inputs):\nfollowed by the method\n"
# print "We give output using the 'return' statement."
# 
# print LB

print "Here's the output from a basic method:"

#### METHOD 1 ####
 		
x = None 

def concatWithCheeze(str1,str2):
	return str1 + " cheeze " + str2

print concatWithCheeze("Kahuna burgers with ", " and Friends")

print LB
print "But this method is not robust, as it could take other values."
print "This one has 'exception catching'"

#### METHOD 2: With Exception ####
def concatWithCheeze(str1,str2):
	# if not type(str1) == str or not type(str2) == str:
	# 	print "NOT A STRING!"
	# 	return

	# return str1 + "cheese" + str2

	try: 
		return str1 + "cheese" + str2
	except TypeError:
		return "Incorrect type - both args should be strings"
	
print concatWithCheeze("123", "4000")# "and Friends")

print LB
print "To note: You have to define a method before implementing it."
print "Also, methods can have defaults."
print "Instead of (strvar), we would type (strvar \"yes\")"

#### METHOD 3: Wtih Exception and Defaults ####
def concatWithCheeze(str1="Chilli", str2="doodles"):
	x = ""
	try: 
		x = str1 + " cheeze " + str2
	except:
		x = "Could not concatenate"

	return x

output = concatWithCheeze()
print output

output = concatWithCheeze(str2="chips")
print output
