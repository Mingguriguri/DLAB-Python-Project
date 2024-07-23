# DLAB-Python-Project
>DLAB 코딩학원 정자 캠퍼스에서 아이들을 가르치고 있습니다.
> 
> DLAB에서 매년 11월에 열리는 GGF(Great Geeks Festival)에 대비하여, 파이썬 심화 수업을 듣고있는 학생들에게 지금까지 배운 내용을 활용하여 GGF에 출전할 아이디어를 얻을 수 있도록 고안하다가 해당 레포지토리를 만들게 되었습니다.

### 환경설정
> Mac 

자신의 Python 환경에 맞춰 설정
```shell
brew install python-tk@3.12
```

## 1. Tkinter를 이용한 간단한 그림판 어플리케이션
- 난이도: 상
- 핵심 개념: Tkinter, 이벤트 처리, 함수

<img width="718" alt="스크린샷 2024-07-23 오후 5 18 48" src="https://github.com/user-attachments/assets/75140761-d1ca-4019-9c28-4a9296382f4c">


### 기능
> 마우스 드래그로 그림 그리기, 색상 선택 기능, 지우개 기능, 캔버스 초기화 기능, 브러시 크기 조절 기능
1. **그림 그리기**
- 마우스 드래그로 그림 그리기: 마우스를 눌러 드래그하면 그림이 그려집니다. 마우스가 움직이는 동안 paint 함수가 호출되어 타원형으로 그림을 그립니다.
- 브러시 크기 조절: 브러시 크기를 조절할 수 있는 슬라이더를 이용해 브러시의 크기를 변경할 수 있습니다. 슬라이더 값에 따라 브러시 크기가 조절됩니다.
2. **색상 선택**
- 색상 선택 버튼: 색상 선택 버튼을 눌러 색상 선택 창을 열 수 있습니다. 색상을 선택하면 선택된 색상으로 브러시 색상이 변경됩니다.
3. **지우개 기능**
- 지우개 버튼: 지우개 버튼을 눌러 브러시 색상을 흰색으로 변경하여 그림을 지울 수 있습니다. 흰색으로 덧그리면서 기존의 그림을 지우는 효과를 줍니다.
4. **캔버스 초기화**
- 캔버스 초기화 버튼: 초기화 버튼을 눌러 캔버스를 깨끗하게 지울 수 있습니다. 캔버스에 그려진 모든 그림이 삭제됩니다.

5. **UI 구성**
- 캔버스: 그림을 그릴 수 있는 흰색 배경의 캔버스가 중앙에 배치됩니다.
- 버튼 및 슬라이더: 색상 선택 버튼, 지우개 버튼, 캔버스 초기화 버튼, 브러시 크기 조절 슬라이더가 화면 아래에 배치됩니다.

### 실행방법 
```shell
python PaintBoard.py
```

## 2. Tkinter를 이용한 간단한 타이핑 게임
- 난이도: 중상
- 핵심 개념: Tkinter, 문자열 처리, 이벤트 처리, 랜덤 모듈
  
<img width="404" alt="스크린샷 2024-07-23 오후 5 27 14" src="https://github.com/user-attachments/assets/b4ff7c69-aa6c-4e28-9e52-929da5ea5035">

https://github.com/user-attachments/assets/d227ad86-af4f-42af-b5c4-aa29ce0bd2bc



### 기능
1. **게임 시작**
- 게임 시작 버튼: 사용자가 버튼을 눌러 게임을 시작할 수 있습니다. 게임 시작 시 점수와 틀린 수, 남은 시간이 초기화됩니다.

2. **제한 시간**
- 타이머: 게임에 60초의 제한 시간이 주어집니다. 타이머는 1초마다 감소하며, 남은 시간이 0이 되면 게임이 종료됩니다.
- 타이머 표시: 남은 시간이 화면에 표시됩니다.

3. **단어 입력**
- 단어 제시: 화면에 무작위로 선택된 단어가 표시됩니다.
- 단어 입력란: 사용자는 입력란에 단어를 입력하고 Enter 키를 눌러 단어를 제출합니다.

4. **점수 및 틀린 수**
- 점수 계산: 사용자가 올바른 단어를 입력하면 점수가 1점 증가합니다.
- 틀린 수 계산: 사용자가 틀린 단어를 입력하면 틀린 수가 1점 증가합니다.
- 점수 및 틀린 수 표시: 현재 점수와 틀린 수가 화면에 표시됩니다.

5. **단어 목록**
- 단어 목록: 게임에 사용되는 단어들은 사전에 정의된 목록에서 무작위로 선택됩니다. 단어 목록에는 다양한 난이도의 단어들이 포함될 수 있습니다.

6. **게임 종료**
- 게임 종료 메시지: 시간이 다 되면 "게임 종료!" 메시지가 화면에 표시되며, 입력란이 비활성화됩니다.

### 실행방법
```shell
python TypingGame.py
```

## 3. Tkinter를 이용한 간단한 계산기 어플리케이션
- 난이도: 중
- 핵심 개념: Tkinter, 함수, 조건문

<img width="476" alt="스크린샷 2024-07-23 오후 5 40 22" src="https://github.com/user-attachments/assets/24cac5de-1bc4-49df-8dc8-46dc09bcae4d">


### 기능
1. **기본적인 계산 기능**
- 덧셈, 뺄셈, 곱셈, 나눗셈: 기본적인 산술 연산을 수행할 수 있습니다.
- 소수점: 소수점 입력을 지원합니다.

2. **결과 출력**
- 결과 표시: `=` 버튼을 눌러 수식을 평가하고 결과를 화면에 표시합니다.
- 오류 처리: 수식 평가 중 오류가 발생하면 "오류" 메시지를 표시합니다.
3. **입력 관리**
- 입력 초기화: `C` 버튼을 눌러 현재 입력된 수식을 초기화할 수 있습니다.
-  백스페이스: `←` 버튼을 눌러 마지막으로 입력한 문자를 삭제할 수 있습니다.
4. **중복 소수점 방지**
- 소수점 중복 방지: 하나의 숫자에 두 번 이상 소수점이 입력되지 않도록 방지합니다.
5. **UI 구성**
- 레이블: 입력된 수식과 결과를 표시하는 레이블이 상단에 위치합니다.
- 버튼: 숫자 버튼(0-9), 소수점 버튼(`.`), 연산자 버튼(+, -, *, /), 결과 버튼(`=`), 초기화 버튼(`C`), 백스페이스 버튼(`←`)으로 구성된 버튼들이 있습니다.

### 실행방법
```shell
python Calculator.py
```

## Tkinter를 이용한 간단한 일정 관리 어플리케이션
- 난이도: 상
- 핵심 개념: Tkinter, 리스트, 딕셔너리, 함수, 파일 입출력

<img width="516" alt="스크린샷 2024-07-23 오후 5 51 55" src="https://github.com/user-attachments/assets/0f3d4fdc-73a8-47bb-94e5-e3235f5150ad">


### 기능
1. **일정 관리 기능**
- 일정 추가: 사용자가 입력한 날짜와 일정을 추가할 수 있습니다. 날짜와 일정이 모두 입력되지 않은 경우 경고 메시지를 표시합니다.
- 일정 편집: 선택한 일정을 수정할 수 있습니다. '일정 편집' 버튼을 눌러 새로운 일정을 입력하면 기존 일정이 수정됩니다.
- 일정 삭제: 선택한 일정을 삭제할 수 있습니다. 삭제할 일정을 선택하지 않은 경우 경고 메시지를 표시합니다.
- 일정 표시: 선택한 날짜의 모든 일정을 목록으로 표시합니다.
2. **데이터 관리 기능**
- 데이터 저장: 일정 데이터를 JSON 파일에 저장합니다. 일정이 추가되거나 삭제될 때마다 데이터를 저장합니다.
- 데이터 로드: 어플리케이션 시작 시 JSON 파일에서 일정 데이터를 불러옵니다. 파일이 존재하지 않는 경우 새로운 파일을 생성합니다.
3. **입력 검증 기능**
- 날짜 형식 검증: 사용자가 입력한 날짜가 "YYYY-MM-DD" 형식인지 확인합니다. 잘못된 형식이 입력되면 경고 메시지를 표시합니다.
4. **사용자 인터페이스**
- 입력란: 사용자가 날짜와 일정을 입력할 수 있는 입력란을 제공합니다.
- 일정 목록: 날짜별로 일정을 표시하는 리스트 박스를 제공합니다.
- 버튼: 일정 추가, 일정 편집, 일정 삭제 기능을 수행하는 버튼을 제공합니다.
- 경고 메시지: 입력값이 누락되거나 잘못된 경우 경고 메시지를 표시합니다.

### 실행방법
```shell
python Calender.py
```
