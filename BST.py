# Written by Farhad Asadi

class BST:
    """ Binary Serach Tree"""
    class Node:
        """ Node Class"""
        def __init__(self):
            """ Constructor for Node """
            self.left = None
            self.right = None
            self.data = None

    def __init__(self):
        """ Constructor for Binary Search Tree"""
        self._root = None
        self.node_id = 0 # ONLY USED WITHIN to_graphviz()!

    def insert(self, element):
        """ This function inserts new node to into the tree """
        new_node = self.Node()
        new_node.data = element
        if self._root is None:
            self._root = new_node
            return
        current = self._root
        while current is not None:
            parent = current
            if element < current.data:
                current = current.left
            else:
                current = current.right
        if self.find(element) is False:
            if element < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def find(self, element):
        """ This function finds a node in the tree, If the node exists it returns True,
        otherwise it returns False"""
        current = self._root
        while current is not None:  # While current node is the Root
            parent = current    # The current node becomes a parent node
            if element == current.data:
                return True
            if element < current.data:
                current = current.left
            else:
                current = current.right
        if element == parent.data:
            return True
        else:
            return False

    def remove(self, element):
        self._root = self._remove(self._root, element)

    def _remove(self, root , key):
        # Find the node to be deleted and remove it
        #print(root.data)
        if self.find(key) is True:
            if not root:
                return root
            elif key < root.data:
                root.left = self._remove(root.left, key)
            elif key > root.data:
                root.right = self._remove(root.right, key)
            else:
                if root.left is None and root.right is None:
                    #print("No children")
                    root = None
                    return root
                elif root.left is not None:
                    current_temp = root.left
                    parent_temp = root
                    if current_temp.right is None:
                        parent_temp.data = current_temp.data
                        parent_temp.left = current_temp.left
                    else:
                        current_temp = self._get_max(root.left)
                        root.data = current_temp.data
                        root.left = self._remove(root.left, current_temp.data)
                else:
                    current_temp = root.right
                    root = None
                    return current_temp
            return root
        else:
            #print("Did not find the element")
            return root

    def _get_max(self, root):
        if root is None or root.right is None:
            return root
        return self._get_max(root.right)

    # Preorder traversering
    def pre_order_walk(self):
        """ Preorder walk, The function returns a list"""
        current = self._root
        lst1 = self._preorder(current)
        return lst1

    def _preorder(self, root):
        lst1 = []
        if root is not None:
            lst1.append(root.data)
            lst1 = lst1 + self._preorder(root.left)
            lst1 = lst1 + self._preorder(root.right)
        return lst1

    #Inorder traversering
    def in_order_walk(self):
        """ Inorder traversering, The function returns a list"""
        current = self._root
        lst1 = self._inorder(current)
        return lst1

    def _inorder(self, root):
        lst1 = []
        if root is not None:
            lst1 = self._inorder(root.left)
            lst1.append(root.data)
            lst1 = lst1 + self._inorder(root.right)
        return lst1

    # Postorder traversering
    def post_order_walk(self):
        """ Postorder walk. The function returns a list"""
        current = self._root
        lst1 = self._postorder(current)
        return lst1

    def _postorder(self, root):
        lst1 = []
        if root is not None:
            lst1 = self._postorder(root.left)
            lst1 = lst1 + self._postorder(root.right)
            lst1.append(root.data)
        return lst1

    # Get the tree height
    def get_tree_height(self):
        """ This function returns the height of the tree """
        return self._height(self._root)

    def _height(self, current_node):
        if current_node is None:
            return -1
        left_height = self._height(current_node.left)
        right_height = self._height(current_node.right)
        return 1 + max(left_height, right_height)

    def get_min(self):
        """ This function returns the smallest value in the tree """
        current = self._root
        while current is not None:
            if current.left is None:
                return current.data
            else:
                current = current.left

    def get_max(self):
        """ This function return the largest value in the tree"""
        current = self._root
        while current is not None:
            if current.right is None:
                return current.data
            else:
                current = current.right


    def to_graphviz_rec(self, data, current):
        my_node_id = self.node_id
        data += "\t" + str(my_node_id) + " [label=\"" + str(current.data) + "\"];\n"
        self.node_id += 1
        if current.left is not None:
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [color=blue];\n"
            data = self.to_graphviz_rec(data, current.left)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n"

        self.node_id += 1
        if current.right is not None:
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [color=red];\n"
            data = self.to_graphviz_rec(data, current.right)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n"
        return data

    def to_graphviz(self):
        data = ""
        if self._root is not None:
            self.node_id = 0
            data += "digraph {\n"
            data += "\tRoot [shape=plaintext];\n"
            data += "\t\"Root\" -> 0 [color=black];\n"
            data = self.to_graphviz_rec(data, self._root)
            data += "}\n"
        return data


def main():
    bst = BST()
    lst1 = [10, 80, 50, 100, 60]
    for i in lst1:
        bst.insert(i)

    print(bst.to_graphviz())

if __name__ == '__main__':
    main()
