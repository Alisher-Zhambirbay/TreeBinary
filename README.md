# Binary Tree

## Description

This is a simple implementation of a Binary Search Tree (BST) in Python. It includes basic operations:

- Insertion of elements
- Deletion of elements
- Display elements in ascending order (in-order traversal)

## Structure

### `Node` Class

Represents a node in the tree with three main attributes:

- `value` — the value of the node.
- `left` — reference to the left subtree.
- `right` — reference to the right subtree.

### `BinaryTree` Class

Implements the Binary Search Tree with the following methods:

- `insert(key)` — inserts a key into the tree.
- `_insert_recursive(node, key)` — recursive helper method for insertion.
- `show()` — displays elements of the tree in ascending order.
- `_show_recursive(node)` — recursive method for tree traversal.
- `delete(key)` — deletes an element from the tree.
- `_delete_recursive(node, key)` — recursive method for deletion.
- `_min_value_node(node)` — finds the node with the minimum value in the subtree.

## Example Usage

```python
tree = BinaryTree()

for key in [20, 8, 22, 4, 12, 10, 14, 100, 90, 100.5]:
    tree.insert(key)

print("Tree before deletion:")
tree.show()

print("\nDeleting 8...")
tree.delete(8)

print("Tree after deletion:")
tree.show()
