class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
        def __str__(self):
            # we will return a string
            return self.word+'('+self.meaning+')'
flash =[]
print("welcome to flashcard application")
#the following loop will be reapeted until
#user stops to add flashcards
while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word")
    flash.appeand(flashcard(word,meaning))
    option = int(input("enter 0 , if you wan to add another flashcard otherwise enter 1 : "))
    if(option):
        break
    #printing all the flash cards
    print("\nyour flashcards")
    for i in flash:
        print(">", i)