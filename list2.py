l = [4,5,1,2,9,7,10,8]
print("original list:", l)
# variable to store the sum of
# the list
count = 0
# finding the sum
for i in l:
    count += i
    # divide the total elements by
    #number of elements
    avg = count/len(l)
    print("sum = ", count)
    print("average = ", avg)
    #sorting the elemants of the list
    l.sort()
    # printing the first element
    print("smallest element is:", l[-1])
    # printing the last elemant
    print("largest element is:", l[-1])