from positional_binary_tree import PositionalBinaryTree

def showTree(tree):
    print("Final Tree:")
    print("Preorder traversal:")
    print(" -> ".join(tree.preorder()))
    print("Inorder traversal:")
    print(" -> ".join(tree.inorder()))   
    
def test_binary_tree():
    print("Initializing tree...")
    tree = PositionalBinaryTree()
    assert tree.is_empty()
    assert len(tree) == 0

    print("Adding root node...")
    root = tree.add_root("A")
    assert root.element() == "A"
    assert tree.root() == root
    assert tree.is_root(root)
    assert tree.num_children(root) == 0

    print("Adding left and right children to root...")
    left = tree.add_left(root, "B")
    right = tree.add_right(root, "C")
    assert tree.num_children(root) == 2
    assert tree.left(root) == left
    assert tree.right(root) == right
    assert tree.parent(left) == root
    assert tree.parent(right) == root

    print("Adding grandchildren...")
    left_left = tree.add_left(left, "D")
    tree.add_right(left, "F")
    right_right = tree.add_right(right, "E")
    tree.add_left(right, "G")
    assert tree.num_children(left) == 2
    assert tree.num_children(right) == 2
    assert tree.is_leaf(left_left)
    assert tree.is_leaf(right_right)

    showTree(tree)

    print("Replacing a node’s value...")
    old_val = tree.replace(right, "Z")
    assert old_val == "C"
    assert right.element() == "Z"

    showTree(tree)

    print("Deleting a leaf node...")
    deleted_val = tree.delete(left_left)
    assert deleted_val == "D"
    assert tree.left(left) is None

    showTree(tree)

    print("Attaching two subtrees...")
    t1 = PositionalBinaryTree()
    t2 = PositionalBinaryTree()
    r1 = t1.add_root("X")
    r2 = t2.add_root("Y")
    tree.attach(right_right, t1, t2)
    assert tree.left(right_right).element() == "X"
    assert tree.right(right_right).element() == "Y"

    print("Tree size:", len(tree))
    showTree(tree)

    

    print("Test suite completed successfully.")

if __name__ == "__main__":
    test_binary_tree()