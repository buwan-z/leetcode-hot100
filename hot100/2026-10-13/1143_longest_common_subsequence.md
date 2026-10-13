# LeetCode 1143 · 最长公共子序列

题目来源：[LeetCode 1143](https://leetcode.cn/problems/longest-common-subsequence/) · [Hot 100](https://leetcode.cn/studyplan/top-100-liked/)。本练习将函数接口改编为标准输入输出。

## 中文题意
给定两个字符串，求它们最长公共子序列的长度。子序列可以通过删除零个或多个字符得到，保留字符的相对顺序不变，字符不必连续。若没有共同字符，输出 0。
## ACM 输入格式
第一行字符串 text1。
第二行字符串 text2。
字符串均不含空格或引号；输入仅包含一组数据。
## 输出格式
输出一行一个整数，表示最长公共子序列的长度。
## 样例
输入：
```text
abcde
ace
```
输出：
```text
3
```
解释：ace 是两者的公共子序列。
## 主要数据范围
- 1 ≤ text1 的长度, text2 的长度 ≤ 1000。
- 两个字符串仅包含小写英文字母。
