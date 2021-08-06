# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Node():
	def __init__(self,data,next=None):
		self.__data=data
		self.__next=next
	def getData(self):
		return self.__data
	def getNext(self):
		return self.__next
	def setData(self,newdata):
		self.__data=newdata
	def setNext(self,newnext):
		self.__next=newnext

class SingleLinkedList(Node):

	def __init__(self):
		self.__head=None
		self.__size=0
	def isEmpty(self):
		return self.__head==None
	def count(self):
		current=self.__head
		count=0
		while current!=None:
			count+=1
			current=current.getNext()
		return count
	def travel(self):
		current=self.__head
		while current!=None:
			print(current.getData(),end=' ')
			current=current.getNext()
		print()
	def add(self,data):  #在链表前端添加元素
		temp=Node(data)
		temp.setNext(self.__head)
		self.__head=temp
	def append(self,data):   #在链表尾部添加元素
		temp=Node(data)
		if self.isEmpty():
			self.__head=temp
		else:
			current=self.__head
			while current.getNext()!=None:
				current=current.getNext()
			current.setNext(temp)
	def search(self,data):  #检索元素是否在链表中
		current=self.__head
		while current!=None:
			if current.getData()!=data:
				current=current.getNext()
			else:
				return True
		return False
	def index(self,data):  #索引元素在链表中的位置
		current=self.__head
		count=0
		while current!=None:
			count+=1
			if current.getData()!=data:
				current = current.getNext()
			else:
				return count
		return False
	def remove(self,data):  #删除链表中的某项元素
		current=self.__head
		pre=None
		while current!=None:
			if current.getData()!=data:
				pre=current
				current=current.getNext()
			else:
				if not pre:
					self.__head=current.getNext()
				else:
					pre.setNext(current.getNext())
				break
	def insert(self,index,data):  #链表中插入元素
		if index<=1:
			self.add(data)
		elif index>self.count():
			self.append(data)
		else:
			temp=Node(data)
			current=self.__head
			count=1
			while count<index:
				count+=1
				pre=current
				current=current.getNext()
			pre.setNext(temp)
			temp.setNext(current)


if __name__=='__main__':
	a=SingleLinkedList()
	for i in range(1,10):
		a.append(i)
	a.travel()
	print(a.count())
	print(a.search(9))
	a.remove(1)
	a.travel()
	print(a.index(6))
	a.insert(5,100)
	a.travel()
	a.add(10)
	a.remove(9)
	a.travel()




