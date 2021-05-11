# 03. SQL INJECTION

## SQL INJECTION의 종류

`SQL INJECTION` 이란 임의의 SQL 문을 주입하여 데이터베이스가 비정상적으로 동작하도록 하는 공격방법입니다.

`SQL INJECTION` 도 공격하는 방식에 따라 여러 가지 방법이 존재합니다.



### Error based SQL injection

논리적 에러를 이용한 공격방법입니다.

아래와 같이 유저 인증 쿼리가 있습니다.

```sql
select *
from User
where id='{id}'
and password='{password}'
```



만약 id 값으로 아래와 같이 입력한다면 어떻게 될까요

```
' or 1=1 --
```



쿼리는 다음과 같이 바뀌고 테이블에 있는 모든 정보를 조회하여 로그인에 성공하게 됩니다.

``` sql
select *
from User
where id='' or 1=1 --'and password='{password}'
```



### Union based SQL injection

Union 연산을 이용하여 DB의 다른 데이터를 조회해보는 공격방법입니다.

```sql
select *
from Post
where title like '%{title}%'
or content like '%{content}%'
```



만약 title 값으로 아래와 같이 입력한다면 어떻게 될까요

``` 
' union select id, password from User --
```



쿼리는 다음과 같이 바뀌고 유저들의 id와 password가 함께 조회됩니다.

``` sql
select *
from Post
where title like '%' union select id, password from User -- %' or content like '%{content}%'
```



물론 union 연산을 사용하기 위해서는 두 테이블의 칼럼 수와 데이터형이 같아야 합니다.

또한 password의 경우, 암호화해서 저장하기 때문에 다음과 같은 공격방법으로 바로 비밀번호가 온전히 공개되는 건 아니지만 여러 보안에 문제점이 발생합니다.



### Boolean SQL injection

DB로 부터 특정한 값이나 데이터를 전달 받지 않고 단순히 참과 거짓 정보만 알 수 있을 때 사용합니다.

> 이번 공격의 예시는 MySQL에 제한된 공격 방식입니다.
>
> 다른 DB도 같은 방식으로 공격이 가능합니다.

``` sql
select *
from User
where id='{id}'
and password='{password}'
```



id 값으로 다음과 같은 공격을 시도합니다.

```sql
rkdalstjd9' and 
ascii(substr(
	select name 
	from information_schema.tables 
	where table_type='base table' 
	limit 0,1
),1,1) > 100 --
```



아래와 같은 쿼리가 완성되고 이를 통해 테이블들의 이름을 알아낼 수 있습니다.

``` sql
select *
from User
where id='rkdalstjd9' and 
ascii(substr(
	select name 
	from information_schema.tables 
	where table_type='base table' 
	limit 0,1
),1,1) > 100 --'and password='{password}'
```



`rkdalstjd9` 이라는 id는 미리 생성해논 상태에서 substr의 위치와 비교값 100을 바꿔가면서 공격하면 테이블의 전체 이름을 알아낼 수 있습니다.



## SQL INJECTION 대응방안

### 입력 값 검증

사용자의 입력 값에 대한 검증이 필요합니다.

이 때 화이트리스트 기반으로 검증을 합니다. 

블랙리스트 기반으로 검증하게 되면 수많은 차단리스트를 등록해야하고 하나라도 빠지면 보안에 실패하기 때문입니다.

키워드를 치환하는 방법을 사용합니다.

예를 들어 SELECT를 다른 의미로 치환하여 공격을 방지합니다.



### Prepared Statement 구문사용

사용자의 입력 값이 쿼리문의 파라미터로 들어가기 전에 DBMS가 미리 컴파일하여 실행하지 않고 대기합니다.

그 후 사용자의 입력 값이 들어와도 단순히 문자열로 인식하기 때문에 공격을 방어할 수 있습니다.



### Error Message 노출 금지

데이터베이스 에러 발생 시 테이블 명, 컬럼 명 등이 노출 될 수 있기 때문에 해당 메세지가 노출 되지 않도록 별도의 메세지 박스를 사용합니다.





## 레퍼런스

https://noirstar.tistory.com/264



## 질문할 사항



## 추가 공부할 키워드

