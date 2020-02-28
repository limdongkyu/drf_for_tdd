[![CircleCI](https://circleci.com/gh/limdongkyu/drf_for_tdd.svg?style=svg)](https://circleci.com/gh/limdongkyu/drf_for_tdd)
[![codecov](https://codecov.io/gh/limdongkyu/drf_for_tdd/branch/master/graph/badge.svg)](https://codecov.io/gh/limdongkyu/drf_for_tdd)

## for 글로컬 주니어 개발자들

DRF 기본 사용 방법 및 TDD 사용 방법 및 이해

## 사전 지식 + 자세
* 당연히 파이썬 사용 경험 다들 있죠?
* 장고로 프로젝트 몇번은 경험 했죠?
* 예전 TDD 교육과 함께 python unittest 와 pytest 교육을 받았죠?
* 이젠 TDD 필요함 + 소중함을 절실하게 느껴겠죠?

## 본론
* 간단한 TODO 리스트를 DRF를 이용해 만들어 보아요.
* 테스트 케이스를 만들어 보아요.
* 우리가 만든 테스트 케이스들이 커버리지가 얼마나 되는지 궁금하지 않나요? 한번 알아보아요.
* DRF 를 만들었다면 당연히 사용자에게 문서를 만들어줘야 겠죠?
* Circle CI 를 붙여서 빌드와 테스트를 자동으로 해보아요

### 중요 
* 프론트엔드는 없어요. 나중에 누가 만들어 PR을 날려주면 너무나 즐거울 것 같아요. 커피한잔 ^^
* 예전 Selenium + IDE + GRID 교육으로 UI 테스트를 해봤었죠? 그것도 PR을 날려주면... 합이 커피두잔 ^^

### 테스트 케이스
* 회원가입
* 로그인
* 로그아웃
* todo api - CRUD

### API URL

#### 사용자

* **/api/users/** (회원가입)
* **/api/users/login/** (로그인)
* **/api/users/logout/** (로그아웃)


#### TODO

* **/api/todos/** (Todo 생성 및 리스트)
* **/api/todos/{todo-id}/** (Todo - RUD)


### API DOCS URL

* **/swagger/** (회원가입)

### virtual 
    자알 알아서~

### Install

    pip install -r requirements.txt

### Usage

    python manage.py test

### 마치고

테스트 코드 작성의 정답은 없습니다. 
하지만 개발을 하면 할수록 모두가 필요성을 느끼죠?
테스트 코드는 스킬이 아닙니다. 단지 개발자의 성의라고 생각됩니다.
글로컬 주니어 개발자분들은 앞으로 성의 있는 개발자가 되길 바랍니다.
