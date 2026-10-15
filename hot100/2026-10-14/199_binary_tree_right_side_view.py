from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

        
class Solution:
    def buildTree(self,values:list[str])->TreeNode | None:
        if not values or values[0]=="null":
            return None
        root = TreeNode(int(values[0]))
        q=deque([root])
        n=len(values)
        i=1
        while q:
            node=q.popleft()
            if i<n and values[i]!="null":
                node.left=TreeNode(int(values[i]))
                q.append(node.left)
            i+=1
            if i<n and values[i]!="null":
                node.right=TreeNode(int(values[i]))
                q.append(node.right)
            i+=1
        return root

    def treeSideView(self,root:TreeNode | None)->list[int]:
        q=deque([root])
        ans=[]
        while q:
            n=len(q)
            levelVal=[]
            for _ in range(n):
                node=q.popleft()
                levelVal.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(levelVal[-1])

        return ans





def main():
    n=int(input())
    values = input().split()[:n]
    root=Solution().buildTree(values)
    ans = Solution().treeSideView(root)
    print(len(ans))
    print(*ans)

if __name__ =="__main__":
    main()