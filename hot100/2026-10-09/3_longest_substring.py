import sys
from collections import defaultdict

class Solution:
    def longestsubstring(self,s:str)->int:
        cnt=defaultdict(int)
        left=0
        ans=0
        for right,char in enumerate(s):
            cnt[char]+=1
            while cnt[char]>1:
                cnt[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans

def main():
    s=input()
    ans=Solution().longestsubstring(s)
    print(ans)

if __name__=="__main__":
    main()

