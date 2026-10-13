# LeetCode 240. 搜索二维矩阵 II

原题：[Search a 2D Matrix II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)

以下为单组测试数据的 ACM 输入输出改编。

## 中文题意

给定一个 m 行 n 列整数矩阵和目标值 target。矩阵每行从左到右、每列从上到下均按非递减顺序排列，判断 target 是否出现在矩阵中。请设计高效的查找算法。

## ACM 输入格式

第一行三个整数 m、n 和 target。随后 m 行，每行 n 个整数，表示矩阵的一行。

## 输出格式

如果矩阵中存在 target，输出小写 true；否则输出小写 false。

## 样例

输入：

```text
3 4 6
1 4 7 11
2 5 8 12
3 6 9 16
```

输出：

```text
true
```

说明：目标值 6 出现在第 3 行第 2 列。

## 主要数据范围

1 ≤ m,n ≤ 300；-1000000000 ≤ 矩阵元素、target ≤ 1000000000。每行及每列均非递减。
