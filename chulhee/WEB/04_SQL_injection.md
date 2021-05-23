

# SQL Injection

SQL injection 이란, 보안상의 취약점을 이용하여
임의의 SQL 문을 주입하여 DB 의 비정상적 동작을 하도록 조작하는 행위를 말합니다.



### 공격 방식

- Error based SQL Injection
- Blind SQL Injcetion
- Union SQL Injection



#### Error based SQL Injection

말 그대로, 에러를 이용한 공격 기법으로 고의로 SQL 문에 에러를 발생시킵니다.

에러 메세지를 통해 쿼리문의 구성을 추측하고, DB의 구조 파악까지 가능합니다.

**따라서, 에러가 발생하더라도 front에 에러 메세지를 띄우지 않는 것을 추천합니다.**



#### Blind SQL Injection

위에서 언급한, 에러 메세지가 보이지 않는 경우 사용하는 기법입니다.

이는 특정 쿼리문으로 인한 결과가 참/거짓인 것 만 알 수 있을 때 사용합니다.



#### Union SQL Injection

Union 쿼리를 사용하는 기법입니다.

공격에 쓰이는 union 연산을 위해 두 테이블의 컬럼 수와 데이터 형이 같아야하는 조건이 있지만, 이를 만족하면 다른 정보들도 함께 조회할 수 있습니다.



### 방어

공격 방법에 대한 기법과 키워드는 굉장히 많습니다. 다만, 이는 사용자 입력값을 그대로 믿고 사용하기 때문에 발생합니다.

**따라서, 사용자의 입력값을 반드시 검증한 뒤 사용해야 합니다.**

```ruby
# Ruby on Rails SQL Injection
# 나쁜 예 - 어떠한 매개변수든지 들어갈 수 있음
Client.where("orders_count = #{params[:orders]}")

# 좋은 예 - 적절한 매개변수만 들어갈 수 있음
Client.where('orders_count = ?', params[:orders])
```

위와 같이 사용자의 입력을 그대로 사용하지 않고, 단순한 문자열로 인식할 수 있어야 합니다.

또한, 에러 메세지를 노출하지 않아야 합니다.



#### Prepared Statement 구문사용

사용자의 입력 값이 쿼리문의 파라미터로 들어가기 전에 DBMS가 미리 컴파일하여 실행하지 않고 대기합니다.

그 후 사용자의 입력 값이 들어와도 단순히 문자열로 인식하기 때문에 공격을 방어할 수 있습니다.

### 

## 레퍼런스

- https://kk-7790.tistory.com/74