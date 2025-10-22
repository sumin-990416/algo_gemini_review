# 📝 Baekjoon 1644: 소수의 연속합

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-10-22 | ![골드 3](https://img.shields.io/badge/Gold-3-E5A323?style=for-the-badge) | `투 포인터` | [1644번 문제](https://www.acmicpc.net/problem/1644) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

제시된 코드는 특정 자연수 $N$이 소수들의 연속된 부분합으로 표현될 수 있는 경우의 수를 찾는 문제입니다. (백준 문제 번호 16563번 또는 유사 문제로 추정됩니다.)

### 🧠 **핵심 아이디어**

1. **소수 목록 생성:** 먼저, 주어진 숫자 $N$보다 작거나 같은 모든 소수를 에라토스테네스의 체를 이용하여 효율적으로 생성합니다.
2. **투 포인터 (Two Pointers) 활용:** 생성된 소수 목록(`sum_list`)을 이용하여 연속된 부분합이 $N$과 일치하는 경우의 수를 투 포인터 기법으로 탐색합니다.
3. **초기화 특수 처리:** 만약 $N$ 자체가 소수인 경우, 문제의 조건에 따라 $N$을 제외한 나머지 소수들로만 합을 구해야 하므로 초기 포인터 설정과 결과값을 조정합니다.

### 📝 **알고리즘**

1. **소수 생성 (에라토스테네스의 체):**
    * `Prime_num_list(n)` 함수는 크기가 $N+1$인 불리언 배열 `is_prime`을 생성하고, 2부터 $\sqrt{N}$까지 반복하며 배수들을 소수가 아닌 것으로 표시합니다.
    * 최종적으로 2부터 $N$까지 중 `True`로 남아있는 숫자들만 모아 소수 목록 `sum_list`를 만듭니다.

2. **투 포인터 설정:**
    * **$N$이 소수인 경우:** `result`를 1로 초기화하고, $N$을 `sum_list`에서 제거합니다. 포인터 $i$와 $j$는 남은 목록의 마지막 인덱스로 설정됩니다.
    * **$N$이 소수가 아닌 경우:** `result`를 0으로 초기화하고, 포인터 $i$와 $j$는 전체 소수 목록의 마지막 인덱스로 설정됩니다. (이때 $i$와 $j$는 부분합을 구성하는 구간의 시작과 끝을 나타내며, 초기에는 같은 값을 가집니다. 루프 진입 시 $i$가 끝이 됩니다.)

3. **연속 부분합 계산 및 포인터 이동:**
    * `while i >= 0` 동안 다음을 반복합니다:
        * 현재 부분합 $\text{sum}(\text{sum\_list}[i:j+1])$을 계산합니다.
        * **합 < $N$:** 시작점 $i$를 왼쪽(작은 소수 쪽)으로 한 칸 이동하여 합을 늘리려 시도합니다 ($i \leftarrow i-1$).
        * **합 > $N$:** 끝점 $j$를 왼쪽으로 한 칸 이동하고, $i$를 새로운 $j$로 재설정합니다. 이는 현재 구간이 너무 크므로 구간을 좁히기 위해 시작점과 끝점을 동시에 왼쪽으로 이동하는 효과를 줍니다.
        * **합 == $N$:** 경우의 수 `result`를 1 증가시키고, $j$를 왼쪽으로 이동한 후, $i$를 새로운 $j$로 재설정하여 다음 탐색을 준비합니다.

### 🧐 **시간 복잡도**

1. **소수 생성 (에라토스테네스의 체):** $O(N \log \log N)$
2. **투 포인터 탐색:** 소수 목록의 길이를 $P$라고 할 때, 투 포인터 $i$와 $j$는 전체 탐색 과정에서 최대 $P$번 이동합니다. 하지만 `sum()` 함수를 내부에서 호출하여 현재 부분합을 계산합니다.
    * **개선된 투 포인터 구조가 아닌 경우:** 만약 $\text{sum}(\text{sum\_list}[i:j+1])$ 계산 시 매번 전체 구간을 더한다면 최악의 경우 $O(P^2)$가 될 수 있습니다.
    * **제시된 코드 분석:** 제시된 코드는 $\text{sum}(\text{sum\_list}[i:j+1])$을 매번 호출합니다. $i$와 $j$가 포인터처럼 작동하지만, 합을 갱신하는 대신 매번 재계산하므로, 최악의 경우 (예: $N$이 매우 클 때 $N$이 소수가 아니고 모든 소수가 1씩 차이 날 때) 합 계산에 $O(P)$ 시간이 소요되며, 전체적으로 $O(P^2)$에 근접할 수 있습니다.
    * **실제 $P$ 값:** $P \approx N / \ln N$ 입니다. 따라서 전체 복잡도는 $O(N \log \log N + P^2)$가 됩니다. 효율적인 누적합 기반 투 포인터($O(P)$)를 사용하지 않았기 때문에, 소수 개수에 대해 이차적인 복잡도를 가집니다. (다만, 문제의 제약 조건이 $N$이 작다면 허용될 수 있습니다.)

**결론:** 소수 생성은 $O(N \log \log N)$이지만, 연속 부분합 계산이 `sum()`을 이용해 매번 재계산되므로 투 포인터 구간이 최대로 길어질 경우 **$O(P^2)$** 에 가까운 성능을 보입니다. ($P$는 $N$ 이하의 소수의 개수)

<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 1644: 소수의 연속합
# https://www.acmicpc.net/problem/1644

def Prime_num_list(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    i = 2
    while i * i <= n:  
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
    
    return [i for i in range(2, n + 1) if is_prime[i]]

n = int(input())
sum_list = Prime_num_list(n)


if n in sum_list:
    result = 1
    sum_list.pop()
    i = len(sum_list)-1
    j = i
    sum_num = 0
else:
    result = 0
    i = len(sum_list)
    j = i
    sum_num = 0

while i >= 0:
    if sum(sum_list[i:j+1]) < n:
        i -= 1
    elif sum(sum_list[i:j+1]) > n:
        j -= 1
        i = j
    elif sum(sum_list[i:j+1]) == n:
        j -= 1
        i = j
        result += 1

print(result)
</details>