## for 글로컬 주니어 개발자들

DRF 기본 사용 방법 및 TDD 사용 방법 및 이해

## 사전 지식
* 당연히 파이썬 사용 경험 다들 있죠?
* 장고로 프로젝트 몇번은 경험 했죠?
* 예전 TDD 교육과 함께 unittest 와 pytest 교육을 받았죠?
* 이젠 TDD 필요함 + 소중함을 절실하게 느껴겠죠?

## 본론
* 간단한 TODO 리스트를 DRF를 이용해 만들어 보아요.
* 간단한 테스트 케이스를 만들어 보아요.
* 우리가 만든 테스트 케이스들이커버리지가 얼마나 되는지 궁금하지 않나요? 한번 알아보아요.
* DRF 를 만들었다면 당연히 사용자에게 문서를 만들어줘야 겠죠?
* Circle CI 를 붙여서 빌드와 테스트를 자동으로 해보아요

### 중요 
* 프론트엔드는 없어요. 나중에 누가 만들어 PR을 날려주면 너무나 즐거울 것 같아요. 커피한잔 ^^
    * 예전 Selenium + IDE + GRID 교육으로 UI 테스트를 해봤었죠? 그것도 PR을 날려주면... 커피두잔 ^^

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

실제 프로젝트에 커버리지 100% 코드가 있을까? 

todo - Circle CI 로 자신의 서버에 배포해 보아요

Name                                          Stmts   Miss  Cover
-----------------------------------------------------------------
todos/__init__.py                                 0      0   100%
todos/admin.py                                    6      0   100%
todos/migrations/0001_initial.py                  7      0   100%
todos/migrations/0002_auto_20200226_2021.py       6      0   100%
todos/migrations/__init__.py                      0      0   100%
todos/models.py                                  12      0   100%
todos/permissions.py                              4      0   100%
todos/serializers.py                             12      0   100%
todos/urls.py                                     4      0   100%
todos/views.py                                   15      0   100%
users/__init__.py                                 0      0   100%
users/admin.py                                    0      0   100%
users/models.py                                   0      0   100%
users/serializers.py                             47      1    98%
users/urls.py                                     4      0   100%
users/views.py                                   42      0   100%
-----------------------------------------------------------------
TOTAL                                           159      1    99%
----------------------------------------------------------------------
Ran 24 tests in 2.796s

OK


