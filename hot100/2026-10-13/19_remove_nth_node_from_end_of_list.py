class ListNode:
    def __init__(self,val=0,node=None):
        self.val=val
        self.next=node

class Solution:
    def removeNthNode(self,head:ListNode,k:int)->ListNode:
        # 传入链表的头结点
        # dummy 1 2 3 4 5
        # 存在slow 指针 和fast 指针
        # fast 指针先移动n 步 slow 指向dummy
        # fast slow 同时移动 当fast 指向最后一个节点5时  slow 指针就是删除节点4 的前面的一个节点 直接slow->next=slow.next.next 即可
        dummy=ListNode(0,head)
        slow=fast=dummy

        for _ in range(k):
            fast=fast.next

        while fast.next!=None:
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next
        return dummy.next


def main():
    length,k=map(int,input().split())
    values=list(map(int,input().split()))
    dummy=tail=ListNode()
    for value in values:
        tail.next=ListNode(value)
        tail=tail.next


    head=Solution().removeNthNode(dummy.next,k)

    ans = []
    while head:
        ans.append(head.val)
        head=head.next

    print(length-1)
    print(*ans)



if __name__ == "__main__":
    main()