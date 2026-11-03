# Triplets with Smaller Sum

**Difficulty:** Medium  
**Accuracy:** 40.33%  
**Points:** 4

---

## Problem Statement

Given an array `arr[]` of **distinct** integers and an integer `sum`, count the number of **unique triplets** whose total sum is **strictly less than** the given `sum`.

A triplet is identified only by the three elements it contains. Different permutations of the same three elements are counted as **one** triplet.

---

## Examples

### Example 1

```python
Input:
sum = 2
arr = [-2, 0, 1, 3]

Output:
2
```

**Explanation:**

The triplets whose sum is less than 2 are:

- `(-2, 0, 1)` → -1
- `(-2, 0, 3)` → 1

### Example 2

```python
Input:
sum = 12
arr = [5, 1, 3, 4, 7]

Output:
4
```

**Explanation:**

The valid triplets are:

- `(1, 3, 4)` → 8
- `(5, 1, 3)` → 9
- `(1, 3, 7)` → 11
- `(5, 1, 4)` → 10

---

## Constraints

- `1 ≤ sum ≤ 10⁵`
- `3 ≤ arr.size() ≤ 10³`
- `-10³ ≤ arr[i] ≤ 10³`