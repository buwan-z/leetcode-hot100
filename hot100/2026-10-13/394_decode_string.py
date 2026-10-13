class Solution:
    def decodeString(self,s:str)->str:
        # 使用栈来进行描述
        # 遇到[ 将外面的数字和字符串入栈，并初始化内部
        # 遇到 数字或者字符串 进行拼接
        # 遇到] 弹出栈 进行拼接

        stack=[]
        k=0
        cur_string=""
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                stack.append((cur_string,k))
                cur_string=""
                k=0
            elif c=="]":
                last_string,repeat_times=stack.pop()
                cur_string=last_string+cur_string*repeat_times
            else:
                cur_string+=c
        return cur_string


def main():
    s=input()
    ans=Solution().decodeString(s)
    print(ans)

if __name__ == "__main__":
    main()