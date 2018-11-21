    def PreOrder(self, root):
        '''打印二叉树(先序)'''
        if root == None:
            return 
        print(root.val, end=' ')
        self.PreOrder(root.left)
        self.PreOrder(root.right)
