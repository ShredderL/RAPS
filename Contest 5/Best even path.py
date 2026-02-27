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
    # return max sum of a path starting at root that only continues through even-valued nodes
    #
    # Hint for structure (not the full solution):
    # - make a helper dfs(node)
    # - dfs returns "best even-path sum starting from this node"
    # - stopping cases: node is None OR node.data is odd
    # - otherwise: node.data + max(dfs(left), dfs(right))
    pass


#input
tree_count = int(input("Enter number of nodes in the tree: ").strip())

tree = None
print("Enter the node values (one per line):")
for _ in range(tree_count):
    tree_item = int(input().strip())
    tree = insert_node_into_binary_search_tree(tree, tree_item)

max_sum = MaxEvenNodeSum(tree)
print("Max even path sum:", max_sum)