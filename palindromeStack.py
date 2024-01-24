
#checks if a word is the same if you reverse the order using a stack
checkWord = "racecar".upper()
def StringToList(str):
    list=[]
    list[:0]=str
    return list
class Stack():
    def __init__(self):
        self.stack = []

    def push(self,list):
        for i in list:
            self.stack.append(i)

        return self.stack
    def pop(self, list):
        deleteFromList = []
        for i in list:
            deleteFromList.append(i)
        for i in deleteFromList:
            list.remove(i)
def reverseList(list):
    newList =[]
    s = Stack()
    for i in list:
        newList.insert(0, i)
    s.push(newList)
    s.pop(list)
    return newList

checkPalindrome = reverseList(StringToList(checkWord))
if checkPalindrome == StringToList(checkWord):
    print("Palindrome")
else: print("Not Palindrome")
