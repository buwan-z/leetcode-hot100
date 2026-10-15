# 763. 划分字母区间

来源：[LeetCode 763](https://leetcode.cn/problems/partition-labels/)。本题改编为 ACM 标准输入输出格式，每次运行处理一组数据。

## 题意

给定仅包含小写英文字母的字符串 s，将它划分成尽可能多的非空连续片段，使同一个字母最多只出现在一个片段中。所有片段按原顺序拼接必须恰好得到 s。输出每个片段的长度。

## 输入格式

输入一行字符串 s，不包含空格或引号。

## 输出格式

第一行输出片段数量 p。第二行按片段在原字符串中的顺序输出 p 个长度，以空格分隔。

## 样例 1

输入：

```text
ababcbacadefegdehijhklij
```

输出：

```text
3
9 7 8
```

## 样例 2

输入：

```text
eccbbbbdec
```

输出：

```text
1
10
```

### 样例说明

样例 1 的三个片段依次为 ababcbaca、defegde、hijhklij。

## 数据范围

- 1 ≤ |s| ≤ 500。
- s 仅包含 a 到 z 的小写英文字母。
