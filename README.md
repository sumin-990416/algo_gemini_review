아! Git 저장소의 README.md 파일을 업데이트하고 싶으신 거군요. 하지만 현재 제공된 도구로는 직접 Git 파일을 수정할 수 없습니다.
대신 프로젝트 루트 디렉토리의 README.md 파일 내용을 제공해드릴게요. 이 내용을 복사해서 직접 파일에 붙여넣으시면 됩니다:
markdown# 🎯 Algorithm Solution Archive

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-Practice-brightgreen?style=for-the-badge)
![Baekjoon](https://img.shields.io/badge/Baekjoon-Online%20Judge-0078D4?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Powered-orange?style=for-the-badge)

**백준 알고리즘 문제 풀이 및 AI 분석 자동화 프로젝트**

[문제 보기](https://www.acmicpc.net)

</div>

---

## 📌 프로젝트 소개

알고리즘 문제를 풀면서 **"어떤 접근 방식을 사용했는지"**, **"핵심 아이디어는 무엇인지"**를 나중에 쉽게 복습하고 싶다는 필요에서 시작된 프로젝트입니다.

### 🎯 주요 특징

- **🤖 AI 기반 코드 분석**: Gemini API를 활용한 자동 코드 분석
- **📊 체계적인 분류**: 알고리즘 유형별 폴더 구조
- **📝 상세한 README**: 각 문제별 핵심 아이디어, 알고리즘, 시간 복잡도 자동 생성
- **🚀 자동화된 워크플로우**: Git 커밋/푸시까지 원클릭 처리

---

## 🏗️ 프로젝트 구조
```
algo_sol/
├── BFS/                          # 너비 우선 탐색
│   ├── 16940-BFS_스페셜_저지/
│   ├── 2178-미로_탐색/
│   ├── 2606-바이러스/
│   └── 7569-토마토/
├── 백트래킹/                      # 백트래킹
│   ├── 10974-모든_순열/
│   ├── 1182-부분_수열/
│   ├── 15649-N과_M_(1)/
│   └── 15650-N과_M_(2)/
├── 브루트포스 알고리즘/           # 완전 탐색
│   ├── 1969-DNA/
│   ├── 2309-일곱_난쟁이/
│   └── 9663-N-queen/
├── 최단 경로/                     # 다익스트라, 벨만-포드 등
│   ├── 1261-알고스팟/
│   └── 4485-녹색_옷_입은_애가_젤다지/
├── 최소 스패닝 트리/               # MST (크루스칼, 프림)
│   ├── 1197-최소_스패닝_트리/
│   └── 4386-별자리_만들기/
├── 우선순위 큐/                   # 힙
│   ├── 11279-최대_힙/
│   ├── 1715-카드_정렬하기/
│   └── 1927-최소_힙/
├── manager.py                    # 🔧 메인 자동화 스크립트
├── test_api.py                   # API 연결 테스트
└── .env                          # 환경 변수 (API 키)
```

---

## 🚀 시작하기

### 1️⃣ 필수 요구사항

- Python 3.8 이상
- Gemini API 키 ([발급받기](https://makersuite.google.com/app/apikey))

### 2️⃣ 설치
```bash
# 저장소 클론
git clone https://github.com/yourusername/algo_sol.git
cd algo_sol

# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 패키지 설치
pip install google-generativeai python-dotenv
```

### 3️⃣ 환경 설정

`.env` 파일을 생성하고 API 키를 추가합니다:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ API 연결 테스트
```bash
python test_api.py
```

---

## 💻 사용 방법

### 기본 워크플로우

1. **문제 풀이**: 백준에서 문제를 풀고 소스 코드를 저장 (예: `1234.py`)

2. **자동화 스크립트 실행**:
```bash
python manager.py
```

3. **정보 입력**:
```
▎문제 번호를 입력하세요: 1234
▎문제 제목을 입력하세요: 예제 문제
▎문제 난이도를 입력하세요: 실버 3
▎알고리즘 분류를 입력하세요: BFS
```

4. **자동 처리 과정**:
   - ✅ AI가 코드를 분석하여 핵심 아이디어 추출
   - ✅ 알고리즘 설명 및 시간 복잡도 계산
   - ✅ README.md 파일 자동 생성
   - ✅ 폴더 구조 정리
   - ✅ Git 커밋 & 푸시

### 📋 생성되는 README 예시

각 문제 폴더에는 다음과 같은 형식의 README가 자동 생성됩니다:
```markdown
# 📝 Baekjoon 2178: 미로 탐색

| **Solved Date** | **Difficulty** | **Algorithm** | **Link** |
|:---:|:---:|:---:|:---:|
| 2025-09-15 | ![실버 1](https://img.shields.io/badge/Silver-1-949393) | `BFS` | [2178번 문제](https://www.acmicpc.net/problem/2178) |

## ✨ AI Code Analysis

### 🧠 핵심 아이디어
BFS를 이용하여 미로의 시작점에서 끝점까지의 최단 경로를 찾습니다...

### 📝 알고리즘
1. 입력 처리
2. BFS 큐 초기화
3. 방문 처리 및 탐색
...

### 🧐 시간 복잡도
O(N*M) - N은 행의 수, M은 열의 수
```

---

## 🤖 AI 분석 시스템

### Gemini API 활용
```python
def analyze_code_with_gemini(code_content: str, language: str) -> str:
    """
    코드를 분석하여 다음 정보를 추출합니다:
    - 핵심 아이디어
    - 알고리즘 설명
    - 시간 복잡도 분석
    """
```

### 지원 언어
- ✅ Python (.py)
- ✅ Java (.java)
- ✅ C++ (.cpp)
- ✅ JavaScript (.js)
- ✅ Kotlin (.kt)

---

## 📊 알고리즘 분류 체계(업로드 기준 예시)

| 분류 | 문제 수 | 난이도 범위 |
|------|---------|------------|
| BFS | 4개 | 실버 1 ~ 골드 3 |
| 백트래킹 | 5개 | 실버 2 ~ 실버 3 |
| 브루트포스 알고리즘 | 4개 | 브론즈 1 ~ 골드 4 |
| 최단 경로 | 3개 | 골드 4 |
| 최소 스패닝 트리 | 2개 | 골드 3 ~ 골드 4 |
| 그리디 | 1개 | 실버 2 |
| 우선순위 큐 | 3개 | 실버 2 ~ 골드 4 |
| 덱 | 2개 | 실버 4 |
| 트리 | 1개 | 실버 1 |
| 정수론 | 2개 | 실버 1 ~ 골드 4 |
| 조합론 | 1개 | 실버 2 |

**총 문제 수: 28개**

---

## 🛠️ 주요 기능

### 1. 자동 폴더 생성
```python
target_dir = os.path.join(algo_type, f"{number}-{title}")
os.makedirs(target_dir, exist_ok=True)
```

### 2. 난이도별 뱃지 생성
```python
tier, level = info['level'].split()
color_map = {
    "Bronze": "B56A3C",
    "Silver": "949393",
    "Gold": "E5A323",
    "Platinum": "52E2A8"
}
badge = f"![{level}](https://img.shields.io/badge/{tier}-{level}-{color})"
```

### 3. Git 자동화
```bash
git add .
git commit -m "feat: Solve BOJ 1234 (예제 문제)"
git push
```

---

## 🎨 커스터마이징

### 1. AI 모델 변경

`manager.py`의 모델명을 변경하여 다른 Gemini 모델을 사용할 수 있습니다:
```python
model = genai.GenerativeModel('gemini-flash-lite-latest')  # 또는 다른 모델
```

### 2. README 템플릿 수정

`create_readme()` 함수를 수정하여 원하는 형식으로 변경 가능합니다:
```python
def create_readme(info: dict, summary: str, code: str) -> str:
    """README.md 파일의 전체 내용을 생성합니다."""
    # 원하는 형식으로 수정
```

### 3. 프롬프트 커스터마이징

AI 분석 결과를 조정하려면 `analyze_code_with_gemini()` 함수의 프롬프트를 수정하세요:
```python
prompt = f"""
당신은 백준 알고리즘 풀이 분석 전문가입니다.
아래 {language} 코드는 백준 온라인 저지 문제의 정답 코드입니다.
코드를 분석해서 다음 항목에 대해 한국어 마크다운 형식으로 설명해주세요.
...
"""
```

---

## 🤝 기여하기

프로젝트 개선을 위한 기여를 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 라이선스

이 프로젝트는 개인 학습 목적으로 제작되었습니다.

---

## 🙏 감사의 말

- [Baekjoon Online Judge](https://www.acmicpc.net) - 문제 제공
- [Google Gemini API](https://ai.google.dev) - AI 분석 기능
- [Shields.io](https://shields.io) - 뱃지 생성

---

## 📧 연락처

프로젝트에 대한 질문이나 제안이 있으시면 이슈를 등록해주세요!

---

<div align="center">

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!**

Made with ❤️ and 🤖

</div>