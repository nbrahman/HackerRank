import sys


class Solution(object):
    def __init__(self):
        self.st = []
        self.qu = []

    def pushCharacter(self, ch):
        self.st.append(ch)

    def popCharacter(self):
        ch = self.st[len(self.st)-1]
        del self.st[len(self.st)-1]
        return ch

    def enqueueCharacter(self, ch):
        self.qu.append(ch)

    def dequeueCharacter(self):
        ch = self.qu[0]
        del self.qu[0]
        return ch


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")