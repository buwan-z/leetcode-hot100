from collections import defaultdict

class Solution:
    def partition_lable(self,s:str)->list[int]:
        fresh_n=defaultdict(int)
        for idx,ch in enumerate(s):
            fresh_n[ch]=idx

        ans=[]
        max_step=fresh_n[s[0]]
        left=0
        for right,ch in enumerate(s):
            max_step=max(max_step,fresh_n[s[right]])
            if right==max_step:
                ans.append(right-left+1)
                left=right+1

        return ans

def main():
    s=input().strip()
    ans=Solution().partition_lable(s)
    print(*ans)

if __name__ =="__main__":
    main()