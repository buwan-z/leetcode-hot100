import sys

class Solution:
    def twoSum(self,nums: list[int], target: int) -> list[int]:
        dic={}
        for idx,num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],idx]
            dic[num]=idx


def main():
    n=int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)   

if __name__ == "__main__":
    main()