class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
	def addNeighbor(self,nbr,weight = 0):
		self.connectedTo[nbr] = weight
	def getConnections(self):
		return self.connectedTo.keys() #keys()将字典中的键以列表的形式返回
	def getId(self):
		return self.id
	def getWeight(self,nbr):
		return self.connectedTo[nbr]
	def __str__(self):  # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
	def addVertex(self,key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
	def __contains__(self,n):
		return n in self.vertList
	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv=self.addVertex(f)
		if t not in self.vertList:
			nv=self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t],cost)
	def getVertices(self):
		return self.vertList.keys()
	def __iter__(self): #如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
		return iter(self.vertList.values()) #values()方法以列表的形式返回字典中的值

g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
print(g.vertList)
for v in g:  #调用__iter__()方法
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

# prim算法
def prim(graph,n):
    '''
    prim算法求最小生成树
    :param graph: 图
    :return: 最小的权值
    :n:点的个数
    '''
    lowcost = [] #记录当前已访问顶点集合到剩下的点的最低权值，“-1”表示已访问过的点，无需访问
    mst = [] #记录当前被更新的最低权值来自于哪个点，相当于记录是边的起始点，lowcost的下标表示的是最低权值的终止点
    cost = 0 #记录整个最小生成树的权值
    for i in range(n): #初始化lowcost与mst，默认先选择第0个点，把第0个点到其余所有点的权值赋给lowcost，mst内全部赋值为0（也就是第0个点为起始）
        lowcost.append(graph[0][i])
        mst.append(0)
    v = 0 #记录当前被选择的点
    lowcost[0] = -1 #用“-1"来标记已经被访问过的点
    for i in range(n-1):  #还需把其余n - 1个点访问到
        min = float("inf") #初始化为最大值，作用是记录当前最低权值
        for j in range(n):
            if (min > lowcost[j] and lowcost[j] != -1):
                min = lowcost[j]
                v = j
        cost += min
        print(mst[v],"->",v,": ",min)
        lowcost[v] = -1  #点v已经访问
        for k in range(n): #更新lowcost，只需更新从v出发到未访问过的点的权值，已访问过的点lowcost取值为-1不会改变
            if (lowcost[k] > graph[v][k]):
                lowcost[k] = graph[v][k]
                mst[k] = v #如果有被更新的权值，就把当前点v作为被更新权值的那条边的起始点
    return cost
MAX = float("inf")
graph = [[MAX,6,1,5,MAX,MAX],
		 [6,MAX,5,MAX,3,MAX],
		 [1,5,MAX,5,6,4],
		 [5,MAX,5,MAX,MAX,2],
		 [MAX,3,6,MAX,MAX,6],
		 [MAX,MAX,4,2,6,MAX]]
print(prim(graph,len(graph)))



'''
实现最小生成树之Kruscal算法
'''
def adjacency_matrix_to_edge_set(Graph,n):
    '''
    邻接矩阵->边集数组
    :param Graph: 邻接矩阵
    :param n: 图顶点个数
    :return: 边集数组
    '''
    edge_set = []
    '''因为邻接矩阵存储时，有数据冗余，仅使用上三角部分就可得到所有边的信息'''
    for i in range(n):
        for j in range(i,n):
            edge_set.append([i,j,Graph[i][j]])
    return edge_set

def find(parent,v1):
    '''
    查找顶点V1的根
    :param parent:并查集森林
    :param v1:顶点
    :return:v1的根节点
    '''
    if(parent[v1] == v1):
        return v1
    return find(parent,parent[v1]) #递归查找，因为这是棵树

def union(parent,rank,x,y):
    '''
    将两棵树合并在一起，通过将一棵树的根连接到另一棵树的根
    :param parent: 并查集森林
    :param rank: 秩
    :param x: 顶点x
    :param y: 顶点y
    :return: None
    '''
    xroot = find(parent,x) #查找x的根
    yroot = find(parent,y) #查找y的根
    '''
    按秩合并，总是将更小的树连接到更大的树上
    单元素的秩定义为0
    当两颗秩相同的树联合时，他们的秩+1
    '''
    if(rank[xroot] > rank[yroot]):
        parent[yroot] = xroot
    elif(rank[yroot] > rank[xroot]):
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruscal(Graph):
    '''
    克鲁斯卡尔算法，输出最小生成树的路径及最小权值
    :param Graph: 邻接矩阵
    :return: 最小权值
    '''
    price = 0  #记录权值
    MST = []  #记录路径
    n = len(Graph)-1 #MST边的个数
    '''把邻接矩阵转化为边集数组'''
    edge_set = adjacency_matrix_to_edge_set(Graph,len(Graph))
    edge_set.sort(key = lambda edge: edge[2])
    print(edge_set)
    parent = [x for x in range(n+1)]  #并查集森林初始化，点数是MST边的个数+1
    rank = [0] * (n+1) #秩初始化
    e = 0  #当前可取的最小权值边的索引
    cal = 0  #判断是否已经有n条边
    while (cal < n):
        v1,v2,w = edge_set[e]
        e += 1
        x = find(parent,v1)
        y = find(parent,v2)
        if (x == y): #如果加进来的边形成了环则丢弃这条边
            continue
        union(parent,rank,x,y)
        MST.append([v1,v2,w])
        cal += 1
        price += w

    for v1,v2,w in MST:
        print("%s -> %s == %s" %(v1,v2,w))

    return price


if __name__ == '__main__':
    MAX = float("inf")
    graph = [[MAX,6,1,5,MAX,MAX],
             [6,MAX,5,MAX,3,MAX],
             [1,5,MAX,5,6,4],
             [5,MAX,5,MAX,MAX,2],
             [MAX,3,6,MAX,MAX,6],
             [MAX,MAX,4,2,6,MAX]]
    print(kruscal(graph))

'''dijkstra算法'''

def find_parent(parent, v):

    if (parent[v] != v):
        print(find_parent(parent, parent[v]),"-> ",end="")  #从当前点不断倒推整条路径直到源点
    return v  #print完v点的parent之后还是要再return v让上一层来print v的，这样print顺序才是从源点依次print出整条路径


def dijkstra(graph,vertex):

    n = len(graph)  #顶点个数
    dict = []  #记录从源点出发到达该点的最短路径
    parent = []  #记录到达当前点的最短路径中最后一条边的起始点
    sign = [] #标记结点是否被访问

    #初始化
    for i in range(n):
        dict.append(graph[vertex][i])
        parent.append(vertex)
        sign.append(1) #1表示未访问，0表示已访问
    sign[vertex] = 0
    dict[vertex] = 0
    cal = 1  #记录已访问点的个数
    v = vertex #记录当前被选择的节点
    while (cal < n):
        cal += 1
        min = MAX
        for j in range(n):
            if (sign[j] and dict[j] < min):  #在未访问点中找到从源点出发到达该点的路径最短所对应的点
                min = dict[j]
                v = j
        sign[v] = 0
        for k in range(n):
            if (graph[v][k] < MAX and sign[k] and graph[v][k] + dict[v] < dict[k]):  #更新从源点出发经由v到达点k的最短路径
                dict[k] = graph[v][k] + dict[v]
                parent[k] = v
    for i in range(n):
        print("w:",dict[i],"path：",end="")
        find_parent(parent,i)
        print(i)

if __name__ == "__main__":
    MAX = float("inf")
    graph = [[MAX,3,MAX,7,MAX],
             [3,MAX,4,2,MAX],
             [MAX,4,MAX,5,6],
             [7,2,5,MAX,4],
             [MAX,MAX,6,4,MAX]]
    dijkstra(graph,0)
