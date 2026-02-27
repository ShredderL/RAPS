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


def MaxEvenNodeSum(tree):

    def dfs(node):
        if node is None:
            return 0
        if node.data % 2 != 0:
            return 0
        
        leftSum = dfs(node.left)
        rightSum = dfs(node.right)

        return node.data + max(leftSum,rightSum)
    
    return dfs(tree)


#input
tree_count = int(input("Enter number of nodes in the tree: ").strip())

tree = None
print("Enter the node values (one per line):")
for _ in range(tree_count):
    tree_item = int(input().strip())
    tree = insert_node_into_binary_search_tree(tree, tree_item)

max_sum = MaxEvenNodeSum(tree)
print("Max even path sum:", max_sum)