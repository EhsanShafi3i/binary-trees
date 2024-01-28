from MKnode import *
from main import *
import time
import os
while True:
    os.system("cls")
    # os.system("clear")
    print("!!!HELLO TO BINARY TREE!!!\n")
    print("CHOOSE AN OPTION"+"\n")
    print("1-BINARY SEARCH TREE (BST)")
    print("2-MIN HEAP")
    print("3-MAX HEAP\n")
    print("4-EXIT")
    choice = input("\n\n--> ")
    if choice == "1":
        os.system("cls")
        # os.system("clear")
        bst = BST_Node(None)
        print("INSERT A BST\n")
        nodes = int(input("ENTER THE NUM OF NODES\n\n-->"))
        for i in range(nodes):
            node = int(input("ENTER NUM\n-->"))
            bst.insert(node)
        os.system("cls")
        # os.system("clear")
        bst.display()
        input()
    elif choice == "2":
        
        os.system("cls")
        print("INSERT A MIN HEAP\n")
        # os.system("clear")
        elements = int(input("ENTER NUM OF ELEMENTS\n-->"))
        minh = Min_Heap(elements)
        for ii in range(elements):
            node = int(input("ENTER NUM\n-->"))
            minh.insert(node)
        minhlist = minh.prints()
        dll = Node(minhlist[0])
        dll.convert_array_to_doubly_linked_list(minhlist)
        os.system("cls")
        # os.system("clear")
        dll.display()
        input()
    elif choice == "3":
        os.system("cls")
        print("INSERT A MAX HEAP\n")
        # os.system("clear")
        elements = int(input("ENTER NUM OF ELEMENTS\n-->"))
        maxh = Max_heap(elements)
        for ii in range(elements):
            node = int(input("ENTER NUM\n-->"))
            maxh.insert(node)
        maxhlist = maxh.prints()
        dll = Node(maxhlist[0])
        dll.convert_array_to_doubly_linked_list(maxhlist)
        os.system("cls")
        # os.system("clear")
        dll.display()
        input()
    elif choice == "4":
        break
    else:
        print("YOU ENTER WRONG NUM")
        time.sleep(0.5)
