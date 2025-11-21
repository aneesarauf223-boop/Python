#take input of a word
string = input("please enter your own own word : ")
#take input of a character
char = input("please enter your own character : ")
i = 0
count = 0 
#loop will to find the accurance of character
while(i < len(string)): #string  oparation
    if(string[i] == char): #condection 1
        count = count + 1
    i = i + 1
    #display the result
print("the total number of times ", char,"has accurred =" , count )