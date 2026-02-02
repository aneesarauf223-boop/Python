#create class
class IOString():
    #constructer to set default value
    def __init__(self):
        self.str1 = ""
        #function to get input from user
    def get_String(self):
        self.str1 = input("enter string : ")
        #function to print the string in upper case
    def print_String(self):
        print("result is :", self.str1.upper())
# object creation
str1 = IOString()
# call function
str1.get_String()
str1.print_String()