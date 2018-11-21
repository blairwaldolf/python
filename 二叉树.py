'''
1. 二叉树
1.1 二叉树的定义
  二叉树是一种特殊的树，它具有以下特点：
  （1）树中每个节点最多只能有两棵树，即每个节点的度最多为2。
  （2）二叉树的子树有左右之分，即左子树与右子树，次序不能颠倒。
  （3）二叉树即使只有一个子树时，也要区分是左子树还是右子树。
1.2 满二叉树
  满二叉树作为一种特殊的二叉树，它是指：所有的分支节点都存在左子树与右子树，并且所有的叶子节点都在同一层上。其特点有：
  （1）叶子节点只能出现在最下面一层
  （2）非叶子节点度一定是2
  （3）在同样深度的二叉树中，满二叉树的节点个数最多，节点个数为： 2h−1 ，其中 h 为树的深度。
1.3 完全二叉树
  若设二叉树的深度为 h ，除第 h 层外，其它各层 (1～h−1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。其具有以下特点：
  （1）叶子节点可以出现在最后一层或倒数第二层。
  （2）最后一层的叶子节点一定集中在左部连续位置。
  （3）完全二叉树严格按层序编号。（可利用数组或列表进行实现，满二叉树同）
  （4）若一个节点为叶子节点，那么编号比其大的节点均为叶子节点。
2. 二叉树的相关性质
2.1 二叉树性质
  （1）在非空二叉树的 i 层上，至多有 2i−1 个节点 (i≥1) 。
  （2）在深度为 h 的二叉树上最多有 2h−1 个节点 （k≥1) 。
  （3）对于任何一棵非空的二叉树,如果叶节点个数为 n0 ，度数为 2 的节点个数为 n2 ，则有: n0=n2+1 。
2.1 完全二叉树性质
  （1）具有 n 个的结点的完全二叉树的深度为 log2n+1 。.
  （2）如果有一颗有 n 个节点的完全二叉树的节点按层次序编号，对任一层的节点 i，（1≥i≥n） 有：
    （2.1）如果 i=1 ，则节点是二叉树的根，无双亲，如果 i>1 ，则其双亲节点为 ⌊i/2⌋ 。
    （2.2）如果 2i>n 那么节点i没有左孩子，否则其左孩子为 2i 。
    （2.3）如果 2i+1>n 那么节点没有右孩子，否则右孩子为 2i+1 。
    
'''
#前序遍历，先序遍历左子树，先序遍历右子树。根-左-右
def PreOrder(self, root):
        '''打印二叉树(先序)'''
        if root == None:
            return 
        print(root.val, end=' ')
        self.PreOrder(root.left)
        self.PreOrder(root.right)
#中序遍历：先中序访问左子树，然后访问根，最后中序访问右子树。总的来说是左—根—右
    def InOrder(self, root):
        '''中序打印'''
        if root == None:
            return
        self.InOrder(root.left)
        print(root.val, end=' ')
        self.InOrder(root.right)
#后序遍历：后序访问左子树，右子树，根。左-右-根
    def BacOrder(self, root):
        '''后序打印'''
        if root == None:
            return
        self.BacOrder(root.left)
        self.BacOrder(root.right)
        print(root.val, end=' ')
#对比另三个代码的区别
def preTraverse(root):  
    '''
    前序遍历
    '''
    if root==None:  
        return  
    print(root.value)  
    preTraverse(root.left)  
    preTraverse(root.right)  

def midTraverse(root): 
    '''
    中序遍历
    '''
    if root==None:  
        return  
    midTraverse(root.left)  
    print(root.value)  
    midTraverse(root.right)  
  
def afterTraverse(root):  
    '''
    后序遍历
    '''
    if root==None:  
        return  
    afterTraverse(root.left)  
    afterTraverse(root.right)  
    print(root.value)
   
#层次队列。利用队列，依次将根，左子树，右子树存入队列，按照队列的先进先出规则来实现层次遍历。
    def BFS(self, root):
        '''广度优先'''
        if root == None:
            return
        # queue队列，保存节点
        queue = []
        # res保存节点值，作为结果
        #vals = []
        queue.append(root)

        while queue:
            # 拿出队首节点
            currentNode = queue.pop(0)
            #vals.append(currentNode.val)
            print(currentNode.val, end=' ')
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        #return vals
 
#深度优先遍历。利用栈，先将根入栈，再将根出栈，并将根的右子树，左子树存入栈，按照栈的先进后出规则来实现深度优先遍历。
    def DFS(self, root):
        '''深度优先'''
        if root == None:
            return
        # 栈用来保存未访问节点
        stack = []
        # vals保存节点值，作为结果
        #vals = []
        stack.append(root)

        while stack:
            # 拿出栈顶节点
            currentNode = stack.pop()
            #vals.append(currentNode.val)
            print(currentNode.val, end=' ')
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)          
        #return vals
