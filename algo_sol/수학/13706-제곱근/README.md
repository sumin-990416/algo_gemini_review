# 📝 Baekjoon 13706: 제곱근

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-10-20 | ![실버 4](https://img.shields.io/badge/Silver-4-949393?style=for-the-badge) | `수학` | [13706번 문제](https://www.acmicpc.net/problem/13706) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

### ❌ AI 분석 실패
- 오류: 400 API key not valid. Please pass a valid API key. [reason: "API_KEY_INVALID"
domain: "googleapis.com"
metadata {
  key: "service"
  value: "generativelanguage.googleapis.com"
}
, locale: "en-US"
message: "API key not valid. Please pass a valid API key."
]
- API 키가 정확한지, 환경 변수 설정이 올바르게 되었는지 확인해주세요.

<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 13706: 제곱근
# https://www.acmicpc.net/problem/13706

import math
n = int(input())
print(math.isqrt(n))
</details>