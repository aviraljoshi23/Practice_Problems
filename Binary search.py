# Python3 program to implement
# optimized delete in BST.
 
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to do
# inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
 
# A utility function to insert a
# new node with given key in BST
def insert(node, key):
 
    # If the tree is empty,
    # return a new node
    if node is None:
        return Node(key)
 
    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node
 
 
# Given a binary search tree
# delete the key and returns the new root
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # Recursive calls for ancestors nodes of
    # node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
 
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root
 
    # We reach here when root is the node
    # to be deleted.
     
    # If root node is a leaf node
     
    if root.left is None and root.right is None:
          return None
 
    # If one of the children is empty
 
    if root.left is None:
        temp = root.right
        root = None
        return temp
 
    elif root.right is None:
        temp = root.left
        root = None
        return temp
 
    # If both children exist
 
    succParent = root
 
    # Find Successor
 
    succ = root.right
 
    while succ.left != None:
        succParent = succ
        succ = succ.left
 
    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
 
    root.key = succ.key
 
    return root
 

root = None
root = insert(root, 36)
root = insert(root, 54)
root = insert(root, 10)
root = insert(root, 29)
root = insert(root, 43)
root = insert(root, 66)
root = insert(root, 22)
root = insert(root, 27)
root = insert(root, 19)
root = insert(root, 77)
root = insert(root, 33)
root = insert(root, 12)
root = insert(root, 20)
print("Tree")
inorder(root)

#Deletion of nodes manually 
print("\nDelete 12")
root = deleteNode(root,12)
print("Modified tree")
inorder(root)
 
print("\nDelete 36")
root = deleteNode(root,36)
print("Modified tree")
inorder(root)
 
print("\nDelete 10")
root = deleteNode(root,10)
print("Modified tree")
inorder(root)

print("\nDelete 66")
root = deleteNode(root,66)
print("Modified tree")
inorder(root)

