#A dictionary is created using curvy brackets
adict = {}

#You can add values when you create a dictionary
bdict = {"one": "red", "two": "blue", "three": "yellow"}

#If you print a dictionary, you will see its key:value pairs
print(bdict)

#You can call a value by it's key
print(bdict["one"])
print(bdict["three"])

#You can create a dictionary using a loop or other data process
cdict = {}

for x in range(10):

    cdict[x] = x * 10

print(cdict)

#You can split a dictionary into lists of keys and values

bk = bdict.keys()
bv = bdict.values()

print(bk)

print(bv)

###  my dictionary loop and five elements
#Creating an empty Dictionary
Dict ={}
print("Empty Dicitonary:")


# Adding elements one at a time
print(Dict)
Dict[0] ='Geeks'
Dict[1] = 'For '
Dict[3] ='1'
print("\nDictionary after adding 3 elements:")
print(Dict)

#Adding set of values
#to single Key
Dict['Value_set'] = 2, 3, 4
print(Dict)


#Updating existing Key's value
Dict[2] = 'Welcome'
print("\nUpdated key value:")
print(Dict)

#Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: " )
print(Dict)
# class objects

class whiteroom():
    """ Pick a door: red, blue, green, or black. """

    do = raw_input("> ")

    if "red" in do:
        print "You entered the red room."

    elif "blue" in do:
        print "You entered the blue room."

    elif "green" in do:
        print "You entered the green room."

    elif "black" in do:
        print "You entered the black room."

    else:
        print "You sit patiently but slowly begin to stave.  You're running out of time."
        return whiteroom()

game = whiteroom()
game
#Code challenge code two lists  columns lists and value relationship and print dicitonary

keys_list = ["pH", "Cr6".  "Cr4", "mv", "water"]
value_list = [1, 2, 3, 4, 5]
dictionary = dict(zip(keys, values))
print(dictionary)
