class Solution:
    def insert_position(self,nums:list[int],target:int)->int:
        # 第一个大于等于target 的位置
        left,right=0,len(nums)
        while left<right:
            mid= left+(right-left)//2
            if nums[mid]>=target:
                right=mid
            else:
                left=mid+1
        return left


def main():
    n,target=map(int,input().split())
    nums=list(map(int,input().split()))[:n]
    ans =Solution().insert_position(nums,target)
    print(ans)

if __name__ == "__main__":
    main()