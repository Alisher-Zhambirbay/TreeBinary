class Node:
    def __init__(self, key): self.value, self.left, self.right = key, None, None

class BinaryTree:
    def __init__(self): self.root = None
    def insert(self, key):
        if not self.root: self.root = Node(key)
        else: self._insert_recursive(self.root, key)
    def _insert_recursive(self, node, key):
        if key < node.value: 
            if node.left: self._insert_recursive(node.left, key)
            else: node.left = Node(key)
        else: 
            if node.right: self._insert_recursive(node.right, key)
            else: node.right = Node(key)

    def show(self): self._show_recursive(self.root)
    def _show_recursive(self, node):
        if node: 
            self._show_recursive(node.left)
            print(node.value, end=" ")
            self._show_recursive(node.right)

    def delete(self, key): self.root = self._delete_recursive(self.root, key)
    def _delete_recursive(self, node, key):
        if not node: return node
        if key < node.value: node.left = self._delete_recursive(node.left, key)
        elif key > node.value: node.right = self._delete_recursive(node.right, key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            min_node = self._min_value_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        return node

    def _min_value_node(self, node):
        while node.left: node = node.left
        return node
#end
# not the main code
tree = BinaryTree()

for key in [20, 8, 22, 4, 12, 10, 14, 100, 90, 100.5]:
    tree.insert(key)

print("Tree before deletion:")
tree.show()
print("\nDeleting 8...")
tree.delete(8)
print("Tree after")
tree.show()
