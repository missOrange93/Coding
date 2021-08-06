class Node():
    def __init__(self,item):
        self.__item=item
        self.__next=None
        self.__previous=None
    def getItem(self):
        return self.__item
    def getNext(self):
        return self.__next
    def getPrevious(self):
        return self.__previous
    def setItem(self,newitem):
        self.__item=newitem
    def setNext(self, newnext):
        self.__next = newnext
    def setPrevious(self, newprevious):
        self.__previous = newprevious

class DoubleLinkedList(Node):
    def __init__(self):
        self.__head=None
    def isEmpty(self):  # 检测链表是否为空
        return self.__head == None
    def count(self):
        current=self.__head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def travel(self):
        current = self.__head
        while current!=None:
            print(current.getItem(),end=" ")
            current=current.getNext()
        print()
    def add(self,item): #在链表前端添加元素
        temp=Node(item)
        if self.isEmpty():
            self.__head=temp
        else:
            temp.setNext(self.__head)
            self.__head.setPrevious(temp)
            self.__head=temp
    def append(self,item):  # 在链表尾部添加元素
        temp=Node(item)
        if self.isEmpty():
            self.__head=temp
        else:
            current=self.__head
            while current.getNext()!=None:
                current=current.getNext()   #遍历链表
            current.setNext(temp)
            temp.setPrevious(current)
    def search(self,item):  #检索元素是否在链表中
        current=self.__head
        while current!=None:
            if current.getItem()!=item:
                current = current.getNext()
            else:
                return True
        return False
    def index(self,item): #索引元素在链表中的位置
        current=self.__head
        count=0
        while current!=None:
            count += 1
            if current.getItem()!=item:
                current = current.getNext()
            else:
                return count
        return False
    def remove(self,item):  #删除链表中的某项元素
        current = self.__head
        while current != None:
            if current.getItem()!=item:
                current = current.getNext()
            else:
                if not current.getPrevious():
                    self.__head=current.getNext()
                    current.getNext().setPrevious(None)
                elif not current.getNext():
                    current.getPrevious().setNext(None)
                else:
                    current.getNext().setPrevious(current.getPrevious())
                    current.getPrevious().setNext(current.getNext())
                break
    def insert(self,index,item):
        if index<=1:
            self.add(item)
        elif index>self.count():
            self.append(item)
        else:
            temp=Node(item)
            current=self.__head
            count=1
            while count<index:
                current=current.getNext()
                count+=1
            current.getPrevious().setNext(temp)
            temp.setPrevious(current.getPrevious())
            temp.setNext(current)
            current.setPrevious(temp)

if __name__=='__main__':
    a=DoubleLinkedList()
    for i in range(1,10):
        a.append(i)
    a.travel()
    print(a.count())
    print(a.search(9))
    a.remove(1)
    a.travel()
    a.insert(8,100)
    a.add(10)
    a.travel()
    print(a.index(10))
    a.remove(9)
    a.travel()