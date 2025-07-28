from positional_binary_tree import PositionalBinaryTree

def showTree(tree):
    print("Preorder traversal:")
    print(" -> ".join(tree.preorder()))
    print("Inorder traversal:")
    print(" -> ".join(tree.inorder())) 
    print()
    
def test_binary_tree():
    print("Initializing tree...")
    tree = PositionalBinaryTree()

    print("Adding root node - A")
    root = tree.add_root("A")
    showTree(tree)

    print("Adding left and right children to root - B, C to A")
    left = tree.add_left(root, "B")
    right = tree.add_right(root, "C")
    showTree(tree)

    print("Adding grandchildren - D, E to A and F, G to C")
    left_left = tree.add_left(left, "D")
    tree.add_right(left, "E")
    tree.add_left(right, "F")
    right_right = tree.add_right(right, "G")
    showTree(tree)

    print("Replacing a node’s value - C with Z")
    tree.replace(right, "Z")
    showTree(tree)

    print("Deleting a leaf node - D")
    tree.delete(left_left)
    showTree(tree)

    print("Attaching two subtrees - X, Y to G")
    t1 = PositionalBinaryTree()
    t2 = PositionalBinaryTree()
    r1 = t1.add_root("X")
    r2 = t2.add_root("Y")
    tree.attach(right_right, t1, t2)
    print("Tree size:", len(tree))
    showTree(tree)

if __name__ == "__main__":
    test_binary_tree()