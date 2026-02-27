import math
import os
import random
import re
import sys

class BinarySearchTreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.left = None
        self.right = None


def insert_node_into_binary_search_tree(node, node_data):
    if node is None:
        return BinarySearchTreeNode(node_data)

    if node_data <= node.data:
        node.left = insert_node_into_binary_search_tree(node.left, node_data)
    else:
        node.right = insert_node_into_binary_search_tree(node.right, node_data)

    return node


def GetParent(tree, k):
    parent = None
    current = tree

    while current is not None:
        if k == current.data:
            if parent is not None:
                return parent.data
            else: 
                return -1
            
        if k < current.data:
            parent = current
            current = current.left
        else:
            parent = current
            current = current.right

    return -1



#input

k = int(input("Enter value k to search for parent: "))

tree_count = int(input("Enter number of nodes in the tree: "))

tree = None
print("Enter the node values (one per line):")

for _ in range(tree_count):
    tree_item = int(input("Node value: "))
    tree = insert_node_into_binary_search_tree(tree, tree_item)

parent = GetParent(tree, k)

print("Parent:", parent)