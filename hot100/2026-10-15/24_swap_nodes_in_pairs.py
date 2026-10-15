class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
class Solution:
    def build_list(self,values:list[int])->ListNode|None:
        if not values:
            return None
        dummy=tail=ListNode()
        for val in values:
            tail.next=ListNode(val)
            tail=tail.next
        return dummy.next

    def sawp_nodes(self,head:ListNode|None)->ListNode|None:
        dummy=ListNode(0,head)
        n0=dummy
        while n0.next and n0.next:
            n1=n0.next
            n2=n0.next.next

            n3=n2.next

            n0.next=n2
            n2.next=n1
            n1.next=n3

            n0=n1
        return dummy.next


def main():
    n=int(input().strip())
    values=list(map(int,input().split()))
    head=Solution().build_list(values)
    new_head=Solution().sawp_nodes(head)
    ans=[]
    while new_head:
        ans.append(new_head.val)
        new_head=new_head.next
    print(*ans)

if __name__ =="__main__":
    main()