class Solution:
    def partition(self,s:int)->list[list[int]]:
        def is_ok(left:int,right:int)->bool:
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        # 从start下标进行切分 之前切分的每一段都是回文子串

        path=[]
        ans=[]
        n=len(s)
        def dfs(start:int):
            # 递归出口
            if start==n:
                ans.append(path[:])
                return 

            for end in range(start,n):
                if is_ok(start,end):
                    path.append(s[start:end+1])    
                    dfs(end+1)
                    path.pop()
        dfs(0)
        return ans




def main():
    s=input()
    ans=Solution().partition(s)
    for a in ans:
        print(len(a),*a)


if __name__ == "__main__":
    main()