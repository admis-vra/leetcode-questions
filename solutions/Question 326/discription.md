# 326. Power of Three

**Difficulty:** `Easy`  
**Topics:** Math, Recursion  
**LeetCode Link:** [Power of Three](https://leetcode.com/problems/power-of-three/)

---

### Problem Description

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

 

**Example 1:**

```
**Input:** n = 27
**Output:** true
**Explanation:** 27 = 33
```

**Example 2:**

```
**Input:** n = 0
**Output:** false
**Explanation:** There is no x where 3x = 0.
```

**Example 3:**

```
**Input:** n = -1
**Output:** false
**Explanation:** There is no x where 3x = (-1).
```

 

**Constraints:**

	
- `-231 31 - 1`

 
**Follow up:** Could you solve it without loops/recursion?

---

### Solutions

- **[Solution1.py](./Solution1.py)** (`python3`, Runtime: 25 ms, Memory: 17.7 MB)
