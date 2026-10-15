class Solution:
    def search_matrix(self,matrix:list[list[int]],target:int)->bool:
        m,n=len(matrix),len(matrix[0])
        i,j=0,n-1
        while i<=m-1 and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False


def main():
    m,n,target=map(int,input().split())
    matrix=[list(map(int,input().split()))[:n] for _ in range(m)]
    ans=Solution().search_matrix(matrix,target)
    print(str(ans).lower())

if __name__ == "__main__":
    main()