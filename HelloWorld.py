#print
print "Hello, Python"

#Continuation Character
item1 = "Bread"
item2 = "milk"
item3 = "eggs"

total = item1 + \
        item2 + \
        item3

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday"]

#String literals
word = 'word'
sentence = """This is a sentence made up \
           of multiple lines and sentences"""

#Waiting for user input
#raw_input("\n\nPress the key to exit\n")

#variables
#Standard data types: Number, String, List, Tuple, Dictionary
counter = 100
miles = 1000.50
firstName = "Aoife"
surname = 'Sayers'

#raw input
print "Hello my name is " + firstName + " " + surname
print "\nI drove " + str(miles) + " miles today"
#can't combine float and strings
age = raw_input("\nWhat is your age?\n")
print "You said you were " + str(age) + " years old!"

#list
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

#tuple
print "Printing Tuples"
tuple = ("abcd", 793, 23.3, "John", 30.3)
tinyTuple = (123, "john")
print tuple #complete list
print tuple[0] #prints 1st index
print tuple[1:3]      # Prints elements starting from 2nd till 3rd
print tuple[2:]       # Prints elements starting from 3rd element
print tinyTuple * 2   # Prints list two times
print tuple + tinyTuple # Prints concatenated lists

#dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

#Arithmetic operators
a = 10
b = 20
c = 2

print str(a) + " + " + str(b) + " = " + str((a+b))
print str(a) + " - " + str(b) + " = " + str((a-b))
print str(a) + " * " + str(b) + " = " + str((a*b))
print str(b) + " / " + str(a) + " = " + str((b/a))
print str(c) + " to the power of " + str(a) + " = " + str((2**10))
