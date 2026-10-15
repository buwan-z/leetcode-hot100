class Solution:
    def max_water(self,heights:list[int])->int:
        max_water=0
        n=len(heights)
        left,right=0,n-1
        while left<right:
            max_water=max(max_water,(right-left)*min(heights[right],heights[left]))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water



def main():
    n=int(input().strip())
    heights=list(map(int,input().split()))
    ans = Solution().max_water(heights)
    print(ans)

if __name__ == "__main__":
    main()