from collections import deque
class Solution:
    def sliding_win_max(self,nums:list[int],k:int)->list[int]:
        q=deque()
        ans=[]
        # 使用单调不增栈 3 -1 -3
        for right in range(len(nums)):
            while len(q)>0 and nums[right]>q[-1]:
                q.pop()
            q.append(nums[right])



            if right>=k:
                left=right-k
                if q[0]==nums[left]:
                    q.popleft()

            if right>=k-1:
                ans.append(q[0])
        return ans



def main():
    m,k=map(int,input().split())
    nums=list(map(int,input().split()))[:m]
    ans=Solution().sliding_win_max(nums,k)
    print(*ans)

if __name__ == "__main__":
    main()
    