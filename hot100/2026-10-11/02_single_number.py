class Solution:
    def single_num(self,nums:list[int])->int:
        ans=0
        for num in nums:
            ans^=num
        return ans


def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().single_num(nums)
    print(ans)


if __name__ == "__main__":
    main()