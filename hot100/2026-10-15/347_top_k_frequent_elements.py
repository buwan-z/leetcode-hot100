import heapq
from collections import Counter

class Solution:
    def top_k_elem(self,nums:list[int],k:int)->list[int]:
        cnt_num=Counter(nums)
        min_heap=[]
        for key,freq in cnt_num.items():
            heapq.heappush(min_heap,(freq,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return [val for freq,val in min_heap]


def main():
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    ans=Solution().top_k_elem(nums,k)
    print(*ans[::-1])

if __name__ == "__main__":
    main()