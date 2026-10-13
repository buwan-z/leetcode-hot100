# LeetCode 153. 寻找旋转排序数组中的最小值

原题：[Find Minimum in Rotated Sorted Array](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)

以下为单组测试数据的 ACM 输入输出改编。

## 中文题意

给定一个由严格递增数组循环旋转得到的整数数组，求其中的最小元素。一次旋转把末尾元素移到开头；旋转若干次后也可能恢复原数组。要求时间复杂度为 O(log n)。

## ACM 输入格式

第一行一个整数 n。第二行 n 个整数，表示数组 nums。

## 输出格式

输出一个整数，表示数组的最小值。

## 样例

输入：

```text
5
3 4 5 1 2
```

输出：

```text
1
```

说明：最小元素为 1。

## 主要数据范围

1 ≤ n ≤ 5000；-5000 ≤ nums[i] ≤ 5000。所有元素互不相同，数组由严格递增数组旋转 1 至 n 次得到。
