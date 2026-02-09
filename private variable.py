class myclass:
    #private variable
    __privatevar = 27;
#private method
    def __privmeth(self):
        print("i'm inside myclass")
    # function to print value of private variable
    def hello(self):
        print("private variable value :",myclass.__privatevar)
        # object creation and method call 
        foo = myclass()
        foo.hello()
        foo.__privmeth