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


def GetDepth(tree, k):
    current = tree
    depth = 0
    while current is not None:
        if k == current.data:
            return depth
        if k < current.data:
            current = current.left
            depth +=1
        else:
            current = current.right
            depth +=1
    return -1


#input

k = int(input("Enter value k to search for depth: "))

tree_count = int(input("Enter number of nodes in the tree: "))

tree = None
print("Enter the node values (one per line):")

for _ in range(tree_count):
    tree_item = int(input("Node value: "))
    tree = insert_node_into_binary_search_tree(tree, tree_item)

depth = GetDepth(tree, k)

print("Depth result:", depth)