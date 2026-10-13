# LeetCode 215. 数组中的第K个最大元素

原题：[Kth Largest Element in an Array](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

以下为单组测试数据的 ACM 输入输出改编。

## 中文题意

给定整数数组 nums 和整数 k，求数组按从大到小排列时第 k 个元素。相同数值按出现次数分别计入排名。可进一步尝试不对整个数组排序。

## ACM 输入格式

第一行两个整数 n 和 k。第二行 n 个整数 nums[i]。

## 输出格式

输出一个整数，表示第 k 大的元素。

## 样例

输入：

```text
9 4
3 2 3 1 2 4 5 5 6
```

输出：

```text
4
```

说明：降序排列为 [6, 5, 5, 4, 3, 3, 2, 2, 1]，第 4 个为 4。

## 主要数据范围

1 ≤ k ≤ n ≤ 100000；-10000 ≤ nums[i] ≤ 10000。
