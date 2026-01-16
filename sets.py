# DIFFERNT TYPES OF SETS IN PYTHON
# set of integers
my_set = {1,2,3}
#set of mixed datatypes
my_set = {1.0, "hello", ( 1,2,3)}
print(my_set)
# ste cannot have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)
#we can make set from a list
my_set = set([1,2,3,2])
print(my_set, "\n")
#remove a number from a list
num_set = set([0,1,3,4,5])
print("original set:")
print(num_set)
num_set.pop()
print("after removeing the first element from the said set")
print(my_set, "\n")


