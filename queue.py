a = [1,4,5,6,7]
a = a.insert(2,8)
print(a)

def queue_time(customers,n):
    list_temp = [0]*n
    for item in customers:
        list_temp[list_temp.index(min(list_temp))] += item  #找到当前所有购物台中总用时最少的，让队列头加入该购物台
    return max(list_temp)

def hotPotato(namelist, num):
	simqueue = Queue()
	for item in namelist:
		simqueue.enqueue(item)
	while(simqueue.size()>1):
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
		simqueue.dequeue()
	return simqueue.dequeue()
