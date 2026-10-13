class Solution:
    def partition(self,s:str)->list[list[str]]:
        ans=[]
        path=[]
        n=len(s)

        def is_ok(left,right)->bool:
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1

            return True

        # 从start下标开始切 前面每一段都是回文子串
        def dfs(start:int):
            if start==n:
                ans.append(path[:])
                return
            for i in range(start,n):
                if is_ok(start,i):
                    path.append(s[start:i+1])
                    dfs(i+1)
                    path.pop()
                
        dfs(0)
        return ans
        


def main():
    s=input()
    ans_list=Solution().partition(s)
    print(len(ans_list))
    for idx,ans in enumerate(ans_list):
        print(len(ans),*ans)
     
if __name__ == "__main__":
    main()
