# 79. 单词搜索（Word Search）

来源：[LeetCode 79](https://leetcode.cn/problems/word-search/)，属于 LeetCode Hot 100。本题将原题改编为 ACM 标准输入输出格式；每次运行只处理一组数据。

## 中文题意

给定 m 行 n 列的字符网格 board 和单词 word，判断能否沿网格中的一条路径拼出 word。相邻字符必须位于上下左右相邻的格子，不能斜向移动，同一个格子在这条路径中至多使用一次。字母区分大小写。

## ACM 输入格式

第一行两个整数 m、n。
接下来 m 行，每行一个长度为 n 的字符串，表示一行网格，字符间没有空格。
最后一行一个字符串 word。

## 输出格式

若存在符合要求的路径，输出小写 true；否则输出小写 false。

## 样例

输入：

```text
3 4
ABCE
SFCS
ADEE
ABCCED
```

输出：

```text
true
```

说明：可以依次经过 A、B、C、C、E、D 六个不同格子。

## 主要数据范围

1 ≤ m, n ≤ 6；1 ≤ word 的长度 ≤ 15；网格与 word 仅包含大小写英文字母。
