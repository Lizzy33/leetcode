from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    @staticmethod
    def createTree():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        # root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        #层序遍历 返回没有None的列表
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            item = queue.pop(0)
            res.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        print(res)
        return res
        """

        """
        # 层序遍历 返回有None的列表
        if not root: return []
        stack, queue, res, nCount = [root], [], [[root.val]], 1
        resss = []
        while stack:
            temp = stack.pop(0)
            if not temp:
                resss.append(None)
                continue
            else:
                resss.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            else:
                stack.append(None)
            if temp.right:
                stack.append(temp.right)
        print(resss)
        return resss
        """

        if not root:
            return []
        queue = [root]
        res = []
        pres = []
        ncount = 1
        while queue:
            item = queue.pop(0)
            pres.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
            ncount -= 1
            if ncount == 0:
                res.append(pres)
                pres = []
                ncount = len(queue)

        print(res)
        return res


l = MyTree.createTree()
sol = Solution()
sol.levelOrder(l)