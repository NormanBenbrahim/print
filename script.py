# the most basic way to print a message
message = "four or five"
print(message)

# print based on the result of another operation
print("Five plus four is {}".format(5+4))

# print only if a condition is met
if 5+1 > 10:
    print("duhhh")

# print after adding strings together
message2 = " or also twenty"
print(message + message2)

# advanced printing using fstrings
msg1 = "the man in the store"
space = " " 
msg2 = "is looking at oranges"
msg3 = "and he thinks they're too orange"

print(f"{msg1}{space}{msg2}{space}{msg3}")

# fstrings are evaluated at runtime, so you can do things like this
print(f"{msg1.replace('the', 'AHHH')}")