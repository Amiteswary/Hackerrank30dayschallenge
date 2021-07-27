    def getHeight(self,root):
        if root != None:
            l_height = 0
            r_height = 0
            l_height = self.getHeight(root.left) + 1
            r_height = self.getHeight(root.right) + 1
            return max(l_height, r_height)
        else:
            return -1
