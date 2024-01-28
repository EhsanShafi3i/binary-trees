import random
import math
from MKnode import Node


class BST_Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BST_Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BST_Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # Print the Tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Min_Heap:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index-1) // 2

    def getLeftchildIndex(self, index):
        return (2*index)+1

    def getRightchildIndex(self, index):
        return (2*index) + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftchild(self, index):
        return self.getLeftchildIndex(index) < self.size

    def hasRightchild(self, index):
        return self.getRightchildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftchildIndex(index)]

    def RightChild(self, index):
        return self.storage[self.getRightchildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        if (self.isFull()):
            raise ("HEAP IS FULL")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def removeMin(self):
        if (self.size == 0):
            raise ("EMPTY HEAP")
        data = self.storage[0]
        self.storage[0]=self.storage[self.size-1]
        self.storage.pop(self.size-1)
        self.size -= 1
        self.heapifyDown()
        return data

    def heapifyDown(self):
        index = 0
        while (self.hasLeftchild(index)):
            smallerChildIndex = self.getLeftchildIndex(index)
            if (self.hasRightchild(index) and self.RightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightchildIndex(index)
            if (self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    def prints(self):
        return self.storage


# array = [5548, 87, 7, 787, 1, 465, 97, 787, 454, 15, 445, 487, 64, 4, 11, 2, 3]
# minh = Min_Heap(len(array))
# for i in array:
#     minh.insert(i)
# minheaplist = minh.prints()
# doubly_linked_list = Node(minheaplist[0])
# doubly_linked_list.convert_array_to_doubly_linked_list(minheaplist)
# doubly_linked_list.display()
# minh.removeMin()
# minheaplist = minh.prints()
# doubly_linked_list = Node(minheaplist[0])
# doubly_linked_list.convert_array_to_doubly_linked_list(minheaplist)
# doubly_linked_list.display()
class Max_heap:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index-1) // 2

    def getLeftchildIndex(self, index):
        return (2*index)+1

    def getRightchildIndex(self, index):
        return (2*index) + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftchild(self, index):
        return self.getLeftchildIndex(index) < self.size

    def hasRightchild(self, index):
        return self.getRightchildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftchildIndex(index)]

    def RightChild(self, index):
        return self.storage[self.getRightchildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        if (self.isFull()):
            raise ("HEAP IS FULL")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()
    
    def heapifyUp(self):
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) < self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
    def removeMax(self):
        if (self.size == 0):
            raise ("EMPTY HEAP")
        data = self.storage[0]
        self.storage[0]= self.storage[self.size-1]
        self.storage.pop()
        self.size -= 1
        self.heapifyDown()
        return data

    def heapifyDown(self):
        index = 0
        while (self.hasLeftchild(index)):
            smallerChildIndex = self.getLeftchildIndex(index)
            if (self.hasRightchild(index) and self.RightChild(index) > self.leftChild(index)):
                smallerChildIndex = self.getRightchildIndex(index)
            if (self.storage[index] > self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
    
    def prints(self):
        return self.storage
    

# maxh = Max_heap(5)
# # for i in range(50):
# #     d = random.randint(0,100)
# #     maxh.insert(d)
# maxh.insert(1)
# maxh.insert(5)
# maxh.insert(6)
# maxh.insert(54)
# maxh.insert(33)
# maxh.removeMax()
# x = maxh.prints();y = Node(x[0])
# y.convert_array_to_doubly_linked_list(x)
# y.display()
