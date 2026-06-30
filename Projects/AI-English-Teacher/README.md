# AI English Teacher

OpenAI GPT를 활용한 CLI 기반 영어 학습 프로그램입니다.

사용자가 영어 문장을 입력하면 문법과 표현을 교정하고, 이전 대화를 기억하여 간단한 영어 튜터처럼 동작합니다.

---

## 주요 기능

### 영어 문장 교정

사용자의 영어 문장을 분석하여 다음 정보를 제공합니다.

* 수정된 문장
* 수정 이유
* 한국어 번역
* 더 자연스러운 표현

예시

```
입력
i am go

출력

[수정된 문장]
I am going.

[수정 이유]
"go"는 현재진행형으로 사용할 수 없으므로 "going"으로 수정합니다.

[한국어 번역]
나는 가고 있다.

[더 자연스러운 표현]
I'm on my way.
```

---

### 대화 기록 저장

모든 대화는 `conversation_log.json`에 저장됩니다.

저장되는 정보

* 질문
* GPT 전체 답변
* 수정된 문장(GPT Memory용)
* 시간

예시

```json
{
    "question": "i am go",
    "answer": "...",
    "corrected_sentence": "I am going.",
    "time": "2026-07-01 16:30:00"
}
```

---

### 최근 대화 기억

프로그램은 최근 대화를 GPT에게 함께 전달하여 이전 내용을 기억합니다.

예시

```
My favorite color is blue.

...

What is my favorite color?
```

최근 대화 안에 정보가 있다면 GPT가 답변합니다.

---

### Prompt Routing

입력 유형에 따라 서로 다른 System Prompt를 사용합니다.

#### 교정 모드

영어 문장을 입력하면

* 영어 교정
* 수정 이유
* 번역
* 자연스러운 표현

을 제공합니다.

#### 대화 모드

질문을 입력하면

* 이전 대화를 참고하여 답변
* 이전 대화에 없는 정보는 추측하지 않음

---

## 프로젝트 구조

```
AI-English-Teacher
│
├── main.py
│   ├── 사용자 입력
│   ├── 입력 유형 분류
│   └── 프로그램 흐름 제어
│
├── gpt_service.py
│   ├── GPT 호출
│   └── GPT 응답 처리
│
├── conversation.py
│   ├── 대화 저장
│   ├── 대화 불러오기
│   └── History 생성
│
├── prompt.py
│   ├── CORRECTION_PROMPT
│   └── CHAT_PROMPT
│
├── conversation_log.json
│
└── .env
```

---

## 사용 기술

* Python
* OpenAI Responses API
* python-dotenv
* JSON

---

## 실행 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env`

```
OPENAI_API_KEY=YOUR_API_KEY
```

### 4. 실행

```bash
python main.py
```

---

## 현재 구현 완료

* OpenAI Responses API 연동
* 영어 문장 교정
* Prompt 분리
* Conversation History 저장
* 최근 대화 기억
* CLI 인터페이스
* JSON 기반 대화 저장

---

## 향후 계획

* 발음 평가 기능
* 음성(STT) 입력
* 음성(TTS) 출력
* 단어 학습 모드
* 문법 퀴즈
* 학습 통계
* SQLite 데이터베이스 적용
* GUI(Web 또는 Desktop) 개발

---

## 프로젝트 목적

이 프로젝트는 OpenAI API를 활용하여 LLM 기반 애플리케이션을 직접 구현하고,

* Prompt Engineering
* Conversation Memory
* OpenAI Responses API
* Python 프로젝트 구조 설계

를 학습하는 것을 목표로 합니다.
