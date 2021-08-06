class CStack(object):

    def __init__(self):
        self.Queue1 = []
        self.Queue2 = []


    def appendTail(self, value):
        if len(self.Queue1):
            self.Queue1.append(value)
        else:
            self.Queue2.append(value)
        """
        :type value: int
        :rtype: None
        """


    def deleteTail(self):
        if (not len(self.Queue1)) and (not len(self.Queue2)):
            return -1
        elif not len(self.Queue1):
            for i in range(0,len(self.Queue2)-1):
                temp = self.Queue2.pop(0)
                self.Queue1.append(temp)
            return self.Queue2.pop(0)
        elif not len(self.Queue2):
            for i in range(0,len(self.Queue1)-1):
                temp = self.Queue1.pop(0)
                self.Queue2.append(temp)
            return self.Queue1.pop(0)

        """
        :rtype: int
        """
    def showStack(self):
        if self.Queue1:
            print(self.Queue1)
        elif self.Queue2:
            print(self.Queue2)
        else:
            print('[]')

stack = CStack()
stack.appendTail(1)
stack.appendTail(9)
stack.appendTail(5)
stack.showStack()
print(stack.deleteTail())
print(stack.deleteTail())
print(stack.deleteTail())
print(stack.deleteTail())
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()