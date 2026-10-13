import sys

class Solution:
    def maxWater(self,height:list[int])->int:
        max_water=0
        n=len(height)
        left,right=0,n-1
        while left<right:
            max_water=max(max_water,
                          min(height[left],height[right])*
                          (right-left))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_water

def main():
    n=int(input())
    height=list(map(int,input().split()))
    max_water=Solution().maxWater(height)
    print(max_water)

if __name__ == "__main__":
    main()