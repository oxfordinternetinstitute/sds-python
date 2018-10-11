# """
# Week 1: Example 2: List Manipulation
# 
# Lists are sequential collections of objects. 
# 
# Python allows you to collect any object in a list, and then iterate over that list.
# """
# 
# __author__ =  'Bernie Hogan'
# __version__=  '1.0'
# 
LB = "\n-----------------------"
# 
# example list manipulation
list1 = ["hello", "fellow", "scripters"]

# first, the for loop:
# print the for loop means we do something to each element.	
for anyNameWillDo in list1:
	print anyNameWillDo

print LB
print "The iterator (traditionally 'i'), refers to each element in the list"

for i in list1: 
	print i.upper()

print LB
print "If we want to save this new upper case list, we wrap the loop in a list."
print "This is called a list comprehension."

# list2 = [i*2 for i in list1]
# print list2
list2 = [i.upper() for i in list1]
print list2

print LB
print "List comps can also employ if statement after the 'for' part."
numList1 = [1,1,2,3,5,8,12,21]
print numList1
numListFiltered = [i for i in numList1 if i < 10]
print numListFiltered

print LB

numList1 = ["alpha","beta","gamma","delta","epsilon"]

print "To find out how many elements are in a list: len()"
print "numList1 has %d elements" % len(numList1)

print LB
print "To iterate through a list by number, we can ask for a range from 0 to the len()"

listlength = len(numList1) 
print listlength

for i in numList1:
	print i

print LB
for i in [0,1,2,3,4]:
	print numList1[i]

print LB
print "This demonstration is a bit more fancy"

numList1 = [1,1,2,3,5,8,12,21]

# for i in range(len(numList1)):
for i in numList1:
	if i < (len(numList1) - 2):
		print "not calculating: %(a)d + %(b)d = %(c)d still in a string" % {'a':i, 'b':i+1, 'c':i+2}
		# print "%(a)d + %(b)d = %(c)d" % {'a':numList1[i], 'b':numList1[i+1], 'c':numList1[i+2]}
		
		
print "\n"
print "How do we know the above used list values rather than calculations?"

numList1 = [1,1,2,3,5,8,12,21]

print LB
print "How about this time?"
for i in range(len(numList1)):
	if i < (len(numList1) - 1):
		var1 = numList1[i]
		var2 = numList1[i+1]
		var3 = var1 + var2
		print "%(a)d + %(b)d = %(c)d" % {'a':var1, 'b':var2, 'c':var3}

print LB
print "Okay, here's a real fibonacci sequence:"

var1 = 1
var2 = 1
var3 = 2

for i in range(7):
	var1 = var2
	var2 = var3
	var3 = var1 + var2

	print "%(a)d + %(b)d = %(c)d" % {'a':var1, 'b':var2, 'c':var3}

print LB
print "Any object can be an element in a list, including another list!"
objectList1 = [numList1,"34",34,"Thirty-four!"]
print objectList1

for i in objectList1:
	print i

print LB
print "To add something to a list, we can use the + symbol"

objectList2 = objectList1 + ["42 is better than 34"]
objectList2.append(objectList2)


print objectList2[5]
# 
print LB
print "When you 'print' an object, you're turning it into a string."
print "We can do this manually using str() method."
objectStr = str(objectList2)
# 
# print objectStr
# print objectStr[3:]
# 
# print "Once you sort a list, that is the new order."
# numList1 = [3,5,4,2,6]
# print numList1
