class PositionalBinaryTree:
  """Linked representation of a Positional Binary Tree using a node-based structure.
     Key Features:
        Encapsulation: Uses a Position class to abstract access.
        Validation: Ensures safety of operations using _validate.
        Modular Design: Attach, delete, and replace respect binary tree invariants.
        Linked Structure: Each node keeps references to parent, left, and right children.
  """

  class _Node:
      """Lightweight, nonpublic class for storing a node (See note below)."""
      __slots__ = '_element', '_parent', '_left', '_right'

      def __init__(self, element, parent=None, left=None, right=None):
          self._element = element
          self._parent = parent
          self._left = left
          self._right = right

  class Position:
      """An abstraction representing the location of a single node."""
      def __init__(self, container, node):
          self._container = container
          self._node = node

      def element(self):
          return self._node._element

      def __eq__(self, other):
          return type(other) is type(self) and other._node is self._node

  def _validate(self, p):
      """Return associated node, or raise error if invalid."""
      if not isinstance(p, self.Position):
          raise TypeError("p must be a valid Position type.")
      if p._container is not self:
          raise ValueError("p does not belong to this container.")
      if p._node._parent is p._node:  # convention for deprecated node
          raise ValueError("p is no longer valid.")
      return p._node

  def _make_position(self, node):
      """Return Position instance for given node (or None if no node)."""
      return self.Position(self, node) if node is not None else None

  def __init__(self):
      """Create an initially empty binary tree."""
      self._root = None
      self._size = 0

  def __len__(self):
      return self._size

  def is_empty(self):
      return self._size == 0

  def root(self):
      return self._make_position(self._root)

  def parent(self, p):
      node = self._validate(p)
      return self._make_position(node._parent)

  def left(self, p):
      node = self._validate(p)
      return self._make_position(node._left)

  def right(self, p):
      node = self._validate(p)
      return self._make_position(node._right)

  def num_children(self, p):
      node = self._validate(p)
      count = 0
      if node._left is not None:
          count += 1
      if node._right is not None:
          count += 1
      return count

  def is_root(self, p):
      return self.root() == p

  def is_leaf(self, p):
      return self.num_children(p) == 0

  def add_root(self, e):
      if self._root is not None:
          raise ValueError("Root exists")
      self._size = 1
      self._root = self._Node(e)
      return self._make_position(self._root)

  def add_left(self, p, e):
      node = self._validate(p)
      if node._left is not None:
          raise ValueError("Left child exists")
      self._size += 1
      node._left = self._Node(e, parent=node)
      return self._make_position(node._left)

  def add_right(self, p, e):
      node = self._validate(p)
      if node._right is not None:
          raise ValueError("Right child exists")
      self._size += 1
      node._right = self._Node(e, parent=node)
      return self._make_position(node._right)

  def replace(self, p, e):
      node = self._validate(p)
      old = node._element
      node._element = e
      return old

  def delete(self, p):
      node = self._validate(p)
      if self.num_children(p) == 2:
          raise ValueError("Node has two children")
      child = node._left if node._left else node._right
      if child is not None:
          child._parent = node._parent
      if node is self._root:
          self._root = child
      else:
          parent = node._parent
          if node is parent._left:
              parent._left = child
          else:
              parent._right = child
      self._size -= 1
      node._parent = node  # convention for deprecated node
      return node._element

  def attach(self, p, t1, t2):
      node = self._validate(p)
      if not self.is_leaf(p):
          raise ValueError("Position must be a leaf")
      if not isinstance(t1, type(self)) or not isinstance(t2, type(self)):
          raise TypeError("Tree types must match")
      self._size += len(t1) + len(t2)
      if not t1.is_empty():
          t1._root._parent = node
          node._left = t1._root
          t1._root = None
          t1._size = 0
      if not t2.is_empty():
          t2._root._parent = node
          node._right = t2._root
          t2._root = None
          t2._size = 0
        
  def preorder(self):
        """Generate a preorder iteration of elements in the tree."""
        if not self.is_empty():
            yield from self._subtree_preorder(self.root())
  
  def _subtree_preorder(self, p):
            """Generate a preorder iteration of subtree rooted at p."""
            # "Visit" node
            yield p.element()
            # Process left subtree
            if self.left(p) is not None:
                yield from self._subtree_preorder(self.left(p))
            # Process right subtree
            if self.right(p) is not None:
                yield from self._subtree_preorder(self.right(p))
        

  def inorder(self):
        """Generate an inorder iteration of elements in the tree."""
        if not self.is_empty():
            yield from self._subtree_inorder(self.root())

  def _subtree_inorder(self, p):
            """Generate an inorder iteration of subtree rooted at p."""
            # Process left subtree
            if self.left(p) is not None:
                yield from self._subtree_inorder(self.left(p))
            # "Visit" node
            yield p.element()
            # Process right subtree
            if self.right(p) is not None:
                yield from self._subtree_inorder(self.right(p))
                

if __name__ == "__main__":
    """ 
        Test for pre-order and inorder traversals. 
    """
    tree = PositionalBinaryTree()
    root = tree.add_root("A")
    left = tree.add_left(root, "B")
    right = tree.add_right(root, "C")
    tree.add_left(left, "D")
    tree.add_right(left, "E")
    tree.add_left(right, "F")
    tree.add_right(right, "G")
    
    print("Preorder traversal:")
    print(" -> ".join(tree.preorder()))  # A -> B -> D -> E -> C -> F -> G
    
    print("Inorder traversal:")
    print(" -> ".join(tree.inorder()))   # D -> B -> E -> A -> F -> C -> G  

"""
__slots__ = '_element', '_parent', '_left', '_right'
    The __slots__ statement serves several important purposes:
    1.	Memory optimization: It restricts the instance attributes to only those listed (_element, _parent, _left, _right), preventing Python from creating a __dict__ for each instance. This significantly reduces memory usage per node.
    2.	Performance improvement: Attribute access becomes faster since Python doesn't need to look up attributes in a dictionary.
    3.	Attribute restriction: It prevents accidental creation of new attributes on _Node instances, which helps catch typos and ensures the class interface remains clean.
    4.	Space efficiency for tree structures: Since binary trees can have many nodes, the memory savings from __slots__ can be substantial when working with large trees.
    This is particularly beneficial in the _Node class because it's described as a "lightweight, nonpublic class" - the __slots__ declaration ensures it truly remains lightweight by minimizing the memory footprint of each node in the binary tree.

"""       
        