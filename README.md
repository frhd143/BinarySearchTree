# Binary Search Tree (BST) Implementation in Python
This repository contains an implementation of Binary Search Tree (BST) data structure in Python.


## Overview
A Binary Search Tree is a binary tree in which each node has at most two children, and for each node, all the values in the left subtree are less than the node's value, and all the values in the right subtree are greater than the node's value.

The following operations can be performed on a BST:

- `insert(element)`: inserts a new node into the tree
- `remove(element)`: removes a node from the tree
- `find(element)`: finds an element in the tree
- `pre_order_walk()`: returns a list of the nodes traversed in pre-order
- `in_order_walk()`: returns a list of the nodes traversed in in-order
- `post_order_walk()`: returns a list of the nodes traversed in post-order
- `get_tree_height()`: returns the height of the tree
- `get_min()`: returns the smallest node in the tree
- `get_max()` returns the largest node in the tree
- `to_graphviz()`: returns a code the can be used to visualize the tree

## Usage
To use the BST tree, simply import the `BST` class from the module and create an instance of it:
```python
from BST import BST

tree = BST()
```

You can then use the methods listed above to insert, remove, and find elements in the tree.

```python
tree.insert(5)
tree.insert(3)
tree.insert(8)

print(tree.find(3)) # True
print(tree.find(10)) # False

print(tree.pre_order_walk()) 
print(tree.in_order_walk()) 
```

You can also use https://dreampuf.github.io/GraphvizOnline/ to visulize the tree.
To this you need to call the `to_graphviz()` function:
```python
print(tree.to_graphviz())
```
The function prints the code you need to copy and paste in the website above.

## Contributing
Contributions to this project are welcome. If you find a bug or want to suggest an improvement, please open an issue or submit a pull request.
Or email me here: f.asadi2002@gmail.com

## License
This code is released under the MIT License.
