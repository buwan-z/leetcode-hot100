class Solution:
    def median_of_sorted_array(self,nums1:list[int],nums2:list[int])->float:
        ans=0
        


        return ans





def main():
    data=list(map(int,input().split()))
    m,n=data[0],data[1]
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    ans=Solution().median_of_sorted_array(nums1,nums2)
    print(ans)

if __name__=="__main__":
    main()