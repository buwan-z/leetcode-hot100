# LeetCode 141. 环形链表

原题：[Linked List Cycle](https://leetcode.cn/problems/linked-list-cycle/)

以下为单组测试数据的 ACM 输入输出改编。

## 中文题意

给定单链表头节点，判断沿 next 指针不断前进时是否会再次到达已经访问过的节点。若会，则链表有环。节点值相同不代表节点相同。可进一步尝试 O(1) 额外空间。

## ACM 输入格式

第一行两个整数 n 和 head。随后 n 行描述编号 0 至 n-1 的节点，每行两个整数 value 和 next_index。next_index=-1 表示空指针，否则表示后继节点编号。n=0 时 head=-1 且没有节点行；n>0 时 head 为合法编号。保证所有节点都能从 head 沿 next 到达。

## 输出格式

有环输出小写 true，无环输出小写 false。

## 样例

输入：

```text
4 0
3 1
2 2
0 3
-4 1
```

输出：

```text
true
```

说明：从头节点依次访问编号 0、1、2、3、1，编号 1 再次出现，所以有环。

## 主要数据范围

0 ≤ n ≤ 10000；-100000 ≤ value ≤ 100000；next_index 为 -1 或 [0, n-1] 内的整数。
