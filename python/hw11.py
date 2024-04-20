#opens the text file and default assigns the object as read only
file = open("python\\hw11text.txt")
#reads lines from file and splits them into a list
words = file.readline().split(' ')
#conversion in a set which removes duplicates and leaves unique words
uniwords = set(words)
#length of the words list for range function
length = len(words)
print("These all are the words within the text")
#range print function to remove brackets and quotations
for x in range(0,length):
    print(words[x],end=' ')
print("\nThis is all the unique words")
#print function to remove brackets and quotations
for items in uniwords:
    print(items,end=" ")
 
