number = 1 + 2 * 3 / 4.0
print(number)

number = 1 + 2 * 3 / 4.0
print(number)

squared = 8 ** 2
cubed = 8 ** 3
print(squared)
print(cubed)

# now we will use operators with strings
helloworld = "hello" + " " + "world"
print(helloworld)
# now we will multiple multiple strings
lotsofhellos = "hello" * 69
print(lotsofhellos)
#now we will use operations with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)
print([1,2,3] * 3)
print([1,2,3] * 3)
# basic string operations
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
astring = "Hello world!"
print(astring.index("o"))
astring = "Hello world!"
print(astring.count("l"))
astring = "Hello world!"
print(astring[3:7:2])
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
