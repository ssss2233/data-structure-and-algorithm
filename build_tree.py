from collections import *
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def level_order(root):
    # 初始化队列，加入根节点
    queue = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res

class BuildTree():
    def dfs(self,preorder,inorder_map,i,l,r):
        if l > r:
            return None
        root = TreeNode(preorder[i])      # 初始化根节点
        m = inorder_map[preorder[i]]      # 中序遍历中根节点索引

        root.left = self.dfs(preorder,inorder_map,i+1,l,m-1)
        root.right = self.dfs(preorder,inorder_map,i+1+m-l,m+1,r)

        return root
    def build_tree(self,preorder,inorder):
        inorder_map = {val:i for i,val in enumerate(inorder)}
        root = self.dfs(preorder,inorder_map,0,0,len(inorder)-1)
        return root 

def main():
    preorder = [3, 9, 5, 6, 2, 1, 7]
    inorder = [5, 9, 6, 3, 1, 2, 7]
    buildtree_obj = BuildTree()
    root = buildtree_obj.build_tree(preorder,inorder)
    res = level_order(root)
    print(res)
main()



