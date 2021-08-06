# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0]
# ]
# dirs = [
#     lambda x, y: (x + 1, y),  # 下
#     lambda x, y: (x - 1, y),  # 上
#     lambda x, y: (x, y - 1),  # 左
#     lambda x, y: (x, y + 1),  # 右
# ]
#
#
# def maze_path(x1, y1, x2, y2):
#     stack = []
#     stack.append((x1, y1))
#     maze[x1][y1] = 2
#     while (len(stack) > 0):
#         biz = 0
#         curNode = stack[-1]  # 当前的节点
#         # print('curNode =', curNode)
#         if curNode[0] == x2 and curNode[1] == y2:
#             # 走到终点了
#             for p in stack:
#                 print(p)
#             return True
#         # x,y 四个方向：上 x-1,y, 右 x,y+1, 下 x+1,y, 左 x,y-1
#         for dir in dirs:
#             nextNode = dir(curNode[0], curNode[1])
#             if nextNode[0] > 4 or nextNode[0] < 0 or nextNode[1] < 0 or nextNode[1] > 4:
#                 continue
#             if maze[nextNode[0]][nextNode[1]] == 0:
#                 stack.append(nextNode)
#                 # print('nextNode =', nextNode)
#                 maze[nextNode[0]][nextNode[1]] = 2  # 避免走回头路
#                 # print(maze)
#                 biz = 1
#                 break
#         if biz == 0:
#             # print('pop =', stack[-1])
#             stack.pop()
#     print('没有路')
#     return False
#
#
# maze_path(0, 0, 4, 4)

def middle2behind(expression):
    result = []  # 结果列表
    stack = []  # 栈
    for item in expression:
        if item.isnumeric():  # 如果当前字符为数字那么直接放入结果列表
            result.append(item)
        else:  # 如果当前字符为一切其他操作符
            if len(stack) == 0:  # 如果栈空，直接入栈
                stack.append(item)
            elif item in '*/(' :  # 如果当前字符为*/（，直接入栈
                stack.append(item)
            elif item == ')' :  # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[len(stack)-1] in '*/':
                if stack.count('(') == 0:   # 如果没有左括号，弹出所有
                    while stack:
                        result.append(stack.pop())
                else:  # 如果有左括号，弹到左括号为止
                    t = stack.pop()
                    while t != '(' :
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)
            else:
                stack.append(item)    # 其余情况直接入栈（如当前字符为+，栈顶为+-）
    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回字符串
    return "".join(result)


expression = "3+(6*7-2)+2*3"
print(middle2behind(expression))

