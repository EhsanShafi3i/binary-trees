# BINARY TREES

#### You can use this app to display Binary Tree.
#### convert an tree array to doubly linkedlist 
#### display an array to binary tree



## Usage
First run the Menu.py file to start.
```bash
!!!HELLO TO BINARY TREE!!!

CHOOSE AN OPTION

1-BINARY SEARCH TREE (BST)
2-MIN HEAP
3-MAX HEAP

4-EXIT


-->

```
choose an option:\
### 1-BST:
```bash
INSERT A BST

ENTER THE NUM OF NODES

-->

```
then enter numbers of node\
then enter each node:
```bash
ENTER NUM
-->
```
like this:
```bash
 ___64_
/      \
4     454
 \
 7_
   \
  24

```
### 2-MIN HEAP
```bash
INSERT A MIN HEAP

ENTER NUM OF ELEMENTS
-->
```
```bash
ENTER NUM
-->
```
```bash
     __2_
    /    \
  _54_  78
 /    \
464  64

```
### 3-MAX HEAP
```bash
INSERT A MAX HEAP

ENTER NUM OF ELEMENTS
-->
```
```bash
ENTER NUM
-->
```
```bash
         ___2222__
        /         \
    ___886_      778_
   /       \    /    \
  255_    64    8   456
 /    \
15   55
```
other usage of this code you can convert an array of binary tree into a doubly linkedlist \
by `MKnode.py`  .
```python
array = [1, 2, 3, 4, 5, 6, 7]
#set the first index as root
doubly_linked_list = Node(array[0])
doubly_linked_list.convert_array_to_doubly_linked_list(array)
#also can display this array by
doubly_linked_list.display()
```
