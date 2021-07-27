    def levelOrder(self,root):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    from collections import deque
    def levelOrder(self,root):      

        queue = self.deque([root]) if root else self.deque()

        while queue:
            node = queue.popleft()
            print(node.data, end=' ')

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)


