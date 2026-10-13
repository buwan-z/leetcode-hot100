class ListNode:
    def __init__(self,val=0,node=None):
        self.val=val
        self.next=node
class Solution:
    def add_two_nums(self,l1:ListNode,l2:ListNode)->ListNode:
        # 保存进位
        carry=0
        dummy=tail=ListNode()
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            tail.next=ListNode(carry%10)
            tail=tail.next
            carry=carry//10

        return dummy.next

def main():
    m,n=map(int,input().split())
    values1 = list(map(int,input().split()))
    values2= list(map(int,input().split()))
    dummy1=tail1=ListNode()
    for value in values1:
        tail1.next=ListNode(value)
        tail1=tail1.next
    dummy2=tail2=ListNode()
    for value in values2:
        tail2.next=ListNode(value)
        tail2=tail2.next

    head=Solution().add_two_nums(dummy1.next,dummy2.next)
    ans=[]
    while head:
        ans.append(head.val)
        head=head.next
    print(len(ans))
    print(*ans)

    
        
if __name__ == "__main__":
    main()