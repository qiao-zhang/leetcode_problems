# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        def dfsIteratively():
            cur, R, stack, l = root, [], [], 0
            while True:
                while cur:
                    stack.append((cur, l))
                    if l < len(R):
                        cur.next, R[l] = R[l], cur
                    elif l == len(R):
                        R.append(cur)
                    cur, l = cur.right, l+1
                if not stack: break
                node, level = stack.pop()
                cur, l = node.left, level+1
        
        def bfs():
            if not root: return
            level = [root]
            while level:
                for i in range(len(level)-1):
                    level[i].next = level[i+1]
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return bfs()
