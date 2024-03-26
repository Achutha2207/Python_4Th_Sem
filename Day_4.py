#demonstrating The Use Of BackSlash operator {As A Continue Moving Forward operator}
print('My name Is Courage'\
'And I hate to lose')
a='abc'\
'bedfe'
print(a)

# Demonstrating The Use Of end='' attribute inside the print function
# This virtue signals the compiler To print space Instead Of A New Line Character

print("This Is 1st Line", end=' ')
print("This Is 2nd Line", end=' ')
print("This Is 3rd line", end=' ')
print("\n")

#If I want to specify to the compiler that the end of the line should not 
#even contain a space then I can mention it as end=''

print('this is line1',end='')
print('this is line2',end='')
print('this is line2Z',end='')
print('\n')

#usage of sep inside print function

#this prints A B C
print('A','B','C')

#this prints ABC
print('A','B','C',sep='')

#I can use any characters inside the sep
#to tell the compiler that my elements in the print
#fuction are "SEPERATED" by a specific value
#The printed items will be seperated by sep='these characters'

print('a','b','c',sep='Loves')

#Escape characters
# \n ->New Line
# \t ->Horizontal 8 spaces shift
# \' ->Single Quote
# \" ->Double quote
# \\ ->\BackSlash

print("a\n")
print("a\tb\t")
print('a       b        ')
print(' I\'m ')
print("\"I\'m Dumb\"")
print('path :c\\a\\b\\c')

#demonstrating floating numbers
a=45.0
b=a/7
print(b)
#this prints 15 significant floating numbers

# How to regulate the unwanted floating numbers (

#by using a buikt in format function
a_=323323.1212213431
print(format(a_,'.2f'))#prints 323323.12

#here 1st argument in the format fuction is the floating number
#and 2nd argument is a String specifying .{how many digits to format}
#eg format(1.2344,'.2f') formats to 1.23 anf f represents that number is a float

#The Actual value still remains the same but
#we get the formatted output

print(a_) #prints 323323.1212213431

#Formatting in scientific notation

print(format(123.1343324,'e'))

#e->Exponent
#e+02 - > 10^2

#here e/E can be used

print(format(32.12312312,'.2e'))

#We can also add commas

print(format(2112312.123123,',.2f'))
#International Number System Is Used Of course cause Its widely popular
#the million and billions system
#Indian System - lakhs , crores
#International System - k,mil,bil
