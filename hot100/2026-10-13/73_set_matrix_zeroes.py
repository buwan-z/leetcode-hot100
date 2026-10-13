class Solution:
    def setMatrixZero(self,matrix:list[list[int]])->list[list[int]]:
        first_col_zero=False
        first_row_zero=False

        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0]==0:
                first_col_zero=True
        for j in range(n):
            if matrix[0][j]==0:
                first_row_zero=True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        if first_row_zero:
            matrix[0]=0
        if first_col_zero:
            for i in range(m):
                matrix[i][0]=0

             



        return matrix


def main():
    m,n=map(int,input().split())
    matrix=[list(map(int,input().split())) for _ in range(m)]
    new_matrix=Solution().setMatrixZero(matrix)
    for line in new_matrix:
        print(*line)


if __name__ == "__main__":
    main()