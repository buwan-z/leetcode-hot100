from collections import Counter
class Solution:
    def findAnagrams(self,s:str,p:str):
        ans=[]
        cnt_s=Counter()
        cnt_p=Counter(p)
        left=0
        n=len(p)
        for right,x in enumerate(s):
            cnt_s[x]+=1
            if right>=n:
                cnt_s[s[left]]-=1
                left+=1
            if right>=n-1 and cnt_s==cnt_p:
                ans.append(left)


        return ans



def main():
    s=input()
    p=input()
    ans=Solution().findString(s,p)
    print(len(ans))
    print(*ans)

if __name__== "__main__":
    main()