class Solution:
    def rain_water(selt,heights:list[int])->int:
        # pre_max[i] heights[i] 左边的最大值
        # suf_max[i] heights[i] 右边的最大值
        total_water=0
        heights=[0]+heights+[0]
        n=len(heights)
        pre_max=[0]*n
        suf_max=[0]*n
        for i in range(1,n-1):
            pre_max[i]=max(pre_max[i-1],heights[i-1])
        for i in range(n-2,0,-1):
            suf_max[i]=max(suf_max[i+1],heights[i+1])

        for i in range(1,n-1):
            total_water+=max(min(pre_max[i],suf_max[i])-heights[i],0)

        return total_water

        



def main():
    n=int(input().strip())
    heights=list(map(int,input().split()))[:n]
    ans=Solution().rain_water(heights)
    print(ans)


if __name__ == "__main__":
    main()