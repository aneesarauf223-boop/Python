#create a tuple withh differnt data types
tuplex = ("tuple", False, 3.2,1)
print(tuplex)
#sreate a tuple 
tuplex = (4,6,2,8,3,1)
print(tuplex)
#tuples are imutable so you cannot add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#counts the number of occurrences of item 50 from a tuple
tuple1 = (50,10,60,70,50)
print(tuple1.count(50))
#create a tuple 
tuplex = (2,4,3,5,4,6,7,8,6,1)
#used tuple [start:stop] the start index is inclusive and the stop index_slice = tuplex[3:5]
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defind; is taken from the beg inning of the tuple _slice = tuplex[:6]
print(slice)