class Solution:
    def searchBST(self, root, val: int) :
        if root.val==None:
            return None
        if root.val==val:
            return root
        if root.val>val:
            if root.left==None:
                return None
            return self.searchBST(root.left, val)
        else:
            if root.right==None:
                return None
            return self.searchBST(root.right, val)
            