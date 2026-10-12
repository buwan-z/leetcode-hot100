# LeetCode 118. 杨辉三角

原题：[Pascal's Triangle](https://leetcode.cn/problems/pascals-triangle/)

以下为单组测试数据的 ACM 输入输出改编。

## 中文题意

给定正整数 numRows，输出杨辉三角的前 numRows 行。第 1 行只有一个 1，每行首尾均为 1，其余位置的数等于上一行左上方和右上方两个数之和。

## ACM 输入格式

一行一个整数 numRows。

## 输出格式

输出 numRows 行，第 i 行包含杨辉三角第 i 行的 i 个整数，以空格分隔，i 从 1 开始。

## 样例

输入：

```text
5
```

输出：

```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

说明：样例输出杨辉三角的前 5 行。

## 主要数据范围

1 ≤ numRows ≤ 30。
