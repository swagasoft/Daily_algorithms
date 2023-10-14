def inorder(root):
    # fill in
    # if root is not None: # O(n) time, O(n) space
    #     result.extend(inorder(root.left))
    #     result.append(root.val)
    #     result.extend(inorder(root.right))
        
    result = []
    stack = []
    current =  root
    
    while current is not None or stack:# O(n) time, O(n) time
        while current is not None:
            stack.append(current)
            current  =  current.left
            
        current =  stack.pop()
        result.append(current.val)
        current = current.right
    
    return result


# Node definition
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Regular binary trees
tree1 = Node(4)
tree1.left = Node(1)
tree1.right = Node(3)

tree2 = Node(5)
tree2.left = Node(10)
tree2.left.left = Node(17)
tree2.left.right = Node(3)
tree2.right = Node(8)

# Binary search trees
tree3 = Node(6)
tree3.left = Node(3)

tree4 = Node(5)
tree4.left = Node(3)
tree4.left.left = Node(2)
tree4.left.left.left = Node(1)

tree5 = Node(8)
tree5.left = Node(6)
tree5.right = Node(9)
tree5.left.left = Node(5)
tree5.left.right = Node(7)
tree5.right.right = Node(10)


def tree_to_arr(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node.val)
        if cur_node.left:
            stack.append(cur_node.left)
        if cur_node.right:
            stack.append(cur_node.right)
    return nodes









import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert callable(inorder) == True
        print("PASSED: `inorderTraversal` should be a function")

    def test_2(self):
        assert inorder(tree2) == [17, 10, 3, 5, 8]
        print("PASSED: `tree2` should return `[17, 10, 3, 5, 8]`")

    def test_3(self):
        assert inorder(tree3) == [3, 6]
        print("PASSED: `tree3` should return `[3, 6]`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")