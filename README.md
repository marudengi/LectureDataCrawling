# LectureDataCrawling

## 개발 환경

VSCode, Git

packages : selenium, webdriver_manager

## 크롤링 대상 사이트

유튜브 → 인프런

인프런 안될줄 알았는데 너무 잘되서 바꿈

## 셀레니움

### windows에서 pip upgrade 액세스 거부 이슈

→ vscode 관리자 권한 실행

### 너무 빠른 입력 대응책

pyautogui → ‘ctrl’ + ‘v’ 기능 수행

pyperclip → 클립보드에 저장

### 클래스

selenium_crawling.py

- webdriver의 초기화 및 작업 수행

parser.py

- get(), set() 메서드를 통해 webdriver 작업 수행
- get() 메서드로 받아온 데이터 파싱
