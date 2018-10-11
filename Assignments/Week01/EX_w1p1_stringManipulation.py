"""
Week 1: Example 1: String Manipulation

Strings are ordered collections of characters. 

By default, they only include ascii characters 
(the basic set of English letters, punctuation, numbers and whitespace) 
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

import string

# Example string manipulation 

# Printing a string: 
print "Hello \"Terra\"!!!"

# Special whitespace characters
print "When you type \\t in code it turns into a tab character:"
print "\t<- right here!"

print "When you type \\n in code it turns into a new line:"
print "\n^ up here!"

# Print a string inside a variable
strvar = "planetfe;hoiagrho'iaegrlhiaegr"

print "\nHello %s !!!" % strvar

LB = "\n-----------------------"
print LB
# Pringing two strings at the same time
print "Multiple strings can be printed at once."
strvar1 = "Cheezburger"
strvar2 = "Fries"

print "\nIn sequence:"
print strvar1,strvar2

print "\nConcatenated:"
print strvar1 + strvar2

print "\nInside a third string:"
print "I can has %(b)s and %(b)s?" % {'a':strvar1, 'b':strvar2}

print LB

# String manipulation
print "Replacing values: (Cheez is now Ham)"
strvar3 = strvar1.replace("Cheez","Ham")
print strvar3

print LB
print "Altering text: To upper and lower case"
print strvar3

strvar4 = "OH MY GAWD; ermahgerd verbles"
print strvar4
print strvar4.lower()
print strvar4

# print strvar1.lower().replace("cheez","ickel")

# print strvar3.upper()
# print strvar3.lower()
# print strvar3.lower().replace("cheez","Ham")

print LB
# Strings can be split up. 
# In fact, they are actually a list of characters
print "This string %s is actually a list. Below I print it as a list:" % strvar1
print list(strvar1)

print LB
print "Lists are sequences, and accessible by index." 
print "I can access the characters by number, starting with 0."

index = 0
print strvar1[index]
print strvar1[0]

print "The %(a)s character in %(b)s is the fifth letter, but at index %(c)d" % {'a':strvar1[index], 'b':strvar1, 'c':index}

print LB
# We can move the other way, too: from lists to strings. 
wordlist = ["I", "can", "haz", "wot?"]
print "Here is the list:"
print wordlist

print "Here it is joined (which adds in spaces by default):"
print string.join(wordlist)

print "Here I've joined it with tabs"
tabstring = string.join(wordlist,"\t")
print tabstring

print LB

message = "What can be joined, can be split."
print message
splituplist = message.split(" ")
print splituplist

