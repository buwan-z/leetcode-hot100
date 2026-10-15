from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:
    def buildTree(self,values:list[str])->TreeNode | None:
        if not values or values[0]=="null":
            return None

        root=TreeNode(int(values[0]))
        i=1
        q=deque([root])
        while q:
            node=q.popleft()
            if i<len(values) and values[i]!="null":
                node.left=TreeNode(int(values[i]))
                q.append(node.left)
            i+=1
            if i<len(values) and values[i]!="null":
                node.right=TreeNode(int(values[i]))
                q.append(node.right)
            i+=1

        return root
        



    def maxPathSum(self, root: TreeNode | None) -> int:
        # ans 保存全局最大路径和；路径可能全是负数，所以不能初始化为 0。
        ans = float("-inf")

        def dfs(node: TreeNode | None) -> int:
            nonlocal ans
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # ans 可以取到当前节点的负数值
            ans = max(ans, left_sum + right_sum + node.val)
            # 返回的贡献值大于等于0
            return max(max(left_sum,right_sum)+node.val,0)

        dfs(root)
        return ans


def main():
    length = int(input().strip())
    values = input().split()[:length]

    root = Solution().buildTree(values)
    print(Solution().maxPathSum(root))


if __name__ == "__main__":
    main()
