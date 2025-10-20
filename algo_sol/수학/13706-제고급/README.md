# 📝 Baekjoon 13706: 제고급

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-10-20 | ![실버 4](https://img.shields.io/badge/Silver-4-949393?style=for-the-badge) | `수학` | [13706번 문제](https://www.acmicpc.net/problem/13706) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

## 백준 알고리즘 풀이 분석

제시된 코드는 주어진 정수 $N$의 제곱근을 정수 부분만 구하는 문제입니다.

### 🧠 **핵심 아이디어**

주어진 양의 정수 $N$에 대해, $\lfloor \sqrt{N} \rfloor$를 계산하는 것이 핵심입니다. Python의 `math` 모듈에서 제공하는 `math.isqrt(n)` 함수는 이 정수 제곱근 계산을 효율적으로 수행합니다.

### 📝 **알고리즘**

1. **입력 받기:** 표준 입력으로부터 정수 $N$을 입력받습니다.
2. **정수 제곱근 계산:** `math.isqrt(n)` 함수를 사용하여 $N$의 정수 제곱근을 계산합니다. 이 함수는 $x^2 \le N$을 만족하는 가장 큰 정수 $x$를 반환합니다.
3. **결과 출력:** 계산된 정수 제곱근을 표준 출력합니다.

### 🧐 **시간 복잡도**

`math.isqrt(n)` 함수의 시간 복잡도는 $O(\log N)$ 또는 $O(\text{log}^2 N)$으로 알려져 있으며, 이는 입력 값 $N$의 비트 수에 따라 결정되는 매우 빠른 연산입니다. 따라서 전체 알고리즘의 시간 복잡도는 **$O(\log N)$** 입니다. (입력/출력 시간 제외)

<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 13706: 제고급
# https://www.acmicpc.net/problem/13706

import math
n = int(input())
print(math.isqrt(n))
</details>