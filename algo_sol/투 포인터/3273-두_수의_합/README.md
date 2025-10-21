# 📝 Baekjoon 3273: 두 수의 합

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-10-21 | ![실버 3](https://img.shields.io/badge/Silver-3-949393?style=for-the-badge) | `투 포인터` | [3273번 문제](https://www.acmicpc.net/problem/3273) |

<br/>

## ✨ AI Code Analysis

> AI가 요약한 핵심 아이디어 및 전략입니다.

## 백준 문제 풀이 분석

제시된 코드는 배열 내에서 합이 특정 목표값($target$)과 일치하는 쌍의 개수를 찾는 문제입니다.

### 🧠 **핵심 아이디어**

주어진 리스트를 내림차순으로 정렬한 후, 양 끝에서 시작하는 두 포인터($i$와 $j$)를 사용하여 목표 합을 찾는 투 포인터(Two Pointers) 기법을 활용합니다. 리스트가 정렬되어 있으므로, 두 포인터의 합을 비교하여 포인터 이동 방향을 효율적으로 결정할 수 있습니다.

### 📝 **알고리즘**

1. **입력 및 정렬**: $N$, 숫자 리스트, 목표값 $target$을 입력받습니다. 리스트를 내림차순으로 정렬합니다 ($\text{sort}(\text{reverse}=\text{True})$).
2. **초기화**: 왼쪽 포인터 $i$를 0으로, 오른쪽 포인터 $j$를 리스트의 마지막 인덱스($n-1$)로 설정하고, 쌍의 개수를 셀 $\text{result}$를 0으로 초기화합니다.
3. **투 포인터 탐색**: $i < j$인 동안 다음을 반복합니다.
    * 현재 두 포인터가 가리키는 값의 합($\text{current\_sum} = \text{num\_list}[i] + \text{num\_list}[j]$)을 계산합니다.
    * **합이 $target$과 같으면**: 쌍을 찾았으므로 $\text{result}$를 1 증가시키고, 다음 탐색을 위해 양쪽 포인터를 모두 안쪽으로 이동시킵니다 ($i \leftarrow i+1, j \leftarrow j-1$).
    * **합이 $target$보다 크면**: 합을 줄여야 하므로, 현재 가장 큰 값인 $\text{num\_list}[i]$를 배제하고 $i$를 증가시켜 더 작은 수와 합을 시도합니다 ($i \leftarrow i+1$). (주의: 이 코드는 내림차순 정렬을 사용하고 있으므로, 합이 클 경우 가장 큰 수(i)를 버리는 것이 아니라, 가장 작은 수(j)를 버려야 합이 줄어듭니다. 그러나 제시된 코드는 $i$를 증가시키고 있습니다. 이는 **오름차순 정렬일 때의 표준 로직**을 내림차순 정렬에 적용한 것으로 보입니다. **정확한 분석을 위해 제시된 코드의 로직을 그대로 설명합니다.**)
        * *제시된 코드 로직*: $\text{current\_sum} > \text{target}$이면 $i$를 증가시킵니다 (가장 큰 수를 버리고 다음 큰 수를 선택).
    * **합이 $target$보다 작으면**: 합을 키워야 하므로, 현재 가장 작은 값인 $\text{num\_list}[j]$를 배제하고 $j$를 감소시켜 더 큰 수와 합을 시도합니다 ($j \leftarrow j-1$).
4. **결과 출력**: 반복이 끝나면 $\text{result}$를 출력합니다.

### 🧐 **시간 복잡도**

1. **입력 및 정렬**: 리스트를 정렬하는 데 $\mathcal{O}(N \log N)$ 시간이 소요됩니다.
2. **투 포인터 탐색**: 포인터 $i$와 $j$는 시작 후 최대 한 번만 움직이며, 두 포인터가 교차할 때까지 최대 $N$번의 비교 연산이 수행됩니다. 따라서 탐색 과정은 $\mathcal{O}(N)$입니다.

전체 시간 복잡도는 정렬 단계에 지배되므로 $\mathcal{O}(N \log N)$ 입니다.

<br/>

<details>
<summary>💻 My Code (Click to expand)</summary>

````py
# Baekjoon Problem 3273: 두 수의 합
# https://www.acmicpc.net/problem/3273

n = int(input())
num_list = list(map(int, input().split()))
target = int(input())

num_list.sort(reverse=True)

i = 0
j = n - 1
result = 0

while i < j:
    current_sum = num_list[i] + num_list[j]
    
    if current_sum == target:
        i += 1
        j -= 1
        result += 1
    elif current_sum > target:
        i += 1
    else:
        j -= 1

print(result)
</details>