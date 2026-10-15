# 11. 盛最多水的容器

来源：[LeetCode 11](https://leetcode.cn/problems/container-with-most-water/)。本题改编为 ACM 标准输入输出格式，每次运行处理一组数据。

## 题意

给定 n 个非负整数 height。对于每个下标 i，在横坐标 i 处有一条高度为 height[i] 的竖线。选择两条竖线与横轴组成容器，求能够容纳的最大水量。容器不能倾斜；选择下标 i < j 时，容量为 (j - i) × min(height[i], height[j])。

## 输入格式

第一行输入整数 n。第二行输入 n 个整数，表示 height。

## 输出格式

输出一个整数，表示最大容量。

## 样例 1

输入：

```text
9
1 8 6 2 5 4 8 3 7
```

输出：

```text
49
```

## 样例 2

输入：

```text
2
1 1
```

输出：

```text
1
```

## 数据范围

- 2 ≤ n ≤ 10^5。
- 0 ≤ height[i] ≤ 10^4。
