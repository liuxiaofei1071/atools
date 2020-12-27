# _*_ coding:utf-8 _*_
# @Time:2020/11/2 12:50
# @Author:Cadman
# @File __init__.py.py

'''
#封装节点数据结构
class Node():
    def __init__(self,item):
        self.item = item
        self.next = None
    def __str__(self):
        return self.item

class Link():
    """
    封装链表数据结构
    """
    #初始化一个空链表
    def __init__(self):
        #该属性永远指向第一个节点
        self._head = None

    def isEmpty(self):
        return self._head == None

    def add(self,item):
        """
        创建一个新的节点对象
        将节点插入到链表的头部
        """
        node = Node(item)
        node.next = self._head
        self._head = node


    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def length(self):
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.next
        return count

    def append(self,item):
        cur = self._head   #第一个节点的地址
        pre = None #cur前面节点的地址

        node = Node(item)
        #如果链表为空则新节点作为链表中的第一个节点
        if self._head is None:
            self._head = node
            return
        #链表非空对应的插入情况
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def insert(self,pos,item):
        cur = self._head
        pre = None
        node = Node(item)
        length = self.length()

        #对特殊情况的处理
        if pos > length:
            self.append(item)
            return
        if pos <= 0:
            self.add(item)
            return

        #正常处理
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur

    def remove(self,item):
        cur = self._head
        pre = None

        #如果删除的是第一个节点
        if item == cur.item:
            self._head = cur.next
            return
        while cur:
            if cur.item == item:
                pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next


    def search(self,item):
        find = False
        cur = self._head
        while cur:
            if cur.item == item:
                find = True
                break
            cur = cur.next
        return find
'''


'''
class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class Tree:
    """
    二叉树
    """

    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        
        if self.root is None:
            self.root = node
            return       
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                return
            else:
                queue.append(cur.left)
            if cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    def travel(self):
        if self.root is None:
            return
        queue = [self.root]
        
        while queue:
            cur = queue.pop(0)
            print(cur.item)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
'''