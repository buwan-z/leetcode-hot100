from collections import Counter

class Solution:
    def find_anagrams(self,s:str,p:str)->list[int]:
        cnt_s=Counter()
        cnt_p=Counter(p)
        n=len(p)
        ans=[]
        for idx,ch in enumerate(s):
            if ch in cnt_p:
                cnt_s[ch]+=1
            if idx>=n:
                if s[idx-n] in cnt_p:
                    cnt_s[s[idx-n]]-=1

            if cnt_s==cnt_p:
                ans.append(idx-n+1)

        return ans

def main():
    s=input().strip()
    # s="abcdeabc"
    p=input().strip()
    # p="abc"
    ans=Solution().find_anagrams(s,p)
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()