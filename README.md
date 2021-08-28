# Python ORM sqlalchemy 사용방법 및 설명
참고자료
ORM 관련 정리 문서 : https://velog.io/@yejin20/DjangoORM%EC%9D%98-%EC%9E%A5%EB%8B%A8%EC%A0%90

악분 일상 유튜브 : https://www.youtube.com/watch?v=kS1J_QwnIgs

sqlalchmey overview 문서 : https://docs.sqlalchemy.org/en/14/core/engines.html



# ORM(Object Realational Mapping)
#### 객체형태로와 관계형데이터베이스를 매핑시켜주고 CRUD가 가능하게 해준다.


## 장점

객체지향적인 코드라 직관적으로 이해하기 쉽다.
=> SQL문을 직접 사용하는 것이 아니라 클래스의 메서드로 데이터베이스를 조작할 수 있어. 개발자는 모델 개발에 집중할 수 있다.
이렇게 되면 코드의 가독성 또한 증가하게 된다.


## 단점
ORM이 모든 것을 해결해줄 수 없다고 한다.
프로젝트의 복잡성이 커지고 난이도가 올라가 설계를 잘못 했을 경우 속도 저하 및 일관성을 무너뜨릴 수 있다고 한다. 그래서 필요에 따라선 SQL을 사용해야한다.

