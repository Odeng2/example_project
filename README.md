# example_project  
FastAPI 기반 백엔드 예제 프로젝트

## 🧩 프로젝트 개요  
이 저장소는 **FastAPI 기반 백엔드 구조를 학습하기 위한 예제 프로젝트**입니다.  
API 설계, 데이터베이스 연동, 서비스 계층 분리 등 실제 서비스 개발 환경과 유사한 구조로 구성되어 있습니다.  
초보 개발자가 프로젝트 아키텍처와 계층형 구조를 이해하고 실습할 수 있도록 제작되었습니다.

## 🚀 주요 기능  
- FastAPI 기반 RESTful API 구현  
- config, router, model, service, repository 계층 분리  
- 의존성 주입(Dependency Injection) 구조 예제  
- 환경 변수 설정(`.env`) 기반 구성  
- 데이터베이스 모델 및 CRUD 예시 코드 포함  

## 🛠 기술 스택  
| 구분 | 기술 |
|------|------|
| 백엔드 프레임워크 | FastAPI |
| 언어 | Python 3.x |
| 데이터베이스 | SQLite / PostgreSQL (환경에 따라 선택 가능) |
| 의존성 관리 | requirements.txt |
| 실행 도구 | Uvicorn |
| 버전 관리 | Git, GitHub |

> **참고:** 실제 사용된 라이브러리 버전은 `requirements.txt` 파일을 참고하세요.

## 📁 디렉토리 구조  
```
/example_project
├─ main.py # FastAPI 실행 진입점
├─ config.py # 환경 변수 및 설정 관리
├─ dependencies.py # 공통 의존성 주입
├─ models.py # 데이터베이스 모델 정의
├─ repositories.py # 데이터 CRUD 로직
├─ routers.py # API 라우터 관리
├─ services.py # 비즈니스 로직 계층
├─ init.py
├─ .env # 환경 변수 파일
└─ README.md
```
