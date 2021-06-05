# 08. GraphQL, REST

Server 에 대해서 요청을 보냈을 때, 이에 맞는 응답을 보내줘야합니다. 

그 방식들의 종류에 대해서 알아봅시다.



## REST

> REpresentational State Transfer 

자원의 표현에 의한 상태 전달

모든 자원을 하나의 endpoint 에 연결해두고, 각 endpoint 는 자원과 관련된 내용만 관리하는 방법론입니다.

HTTP Method을 통해서 CRUD 작업에 대해서 매핑시켜 요청을 보내게 됩니다.

```
GET /posts :조회
POST /posts :생성
PATCH /posts/{id} :수정
DELETE /posts/{id} :삭제
```



### 장점

- REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍쳐 스타일이다.
  - HTTP 프로토콜을 사용하므로 REST API 사용을 위한 인프라를 구축할 필요가 없다.
  - HTTP 표준프로토콜을 따르는 모든 플랫폼에서 호환된다. (범용성)
- REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.
- 서버와 클라이언트의 역할을 명확하게 분리한다.





### 단점

가장 큰 단점은 표준이 존재하지 않는다는 점입니다. 



~~(하지만, 각자 팀에서 CRUD 기반으로 RESTful 하게 작성을 하게 됩니다.)~~



## GraphQL

> Graph Query Language

RESTful 하게 작성하던 API 에선 조금 다른 정보에 대한 접근에 각각 endpoint 를 구현해야했습니다.
(같은 GET 요청에 대해선 같은 결과를 기대하기 때문입니다.)

또한, 지금 당장 필요한 정보가 user의 name 일 때 `GET /users/2` 로 요청할 경우 필요없는 정보까지 받게 됩니다. 이러한 낭비를 **Over-Fetching** 이라고 합니다.

반대로, 한 페이지를 구성하는 정보를 보여주기 위해서 여러 가지 API 를 호출해서 정보를 보여줘야 할 때,

- GET /users/1
- GET /orders
- GET /notifications
- ....

이렇게 여러 API 를 호출하는 것을 **Under-Fetching** 이라고 합니다.



### 가장 큰 차이점

- GraphQL API 는 주로 전체 API를 위해서 하나의 Endpoint 를 사용합니다.
  - 클라이언트가 직접 필요한 정보를 쿼리를 작성하여 요청합니다.

```javascript
const GET_USER = gql`
  query {
    user(id: "123") {
      name
			email
			posts {
				content
			}
    }
  }
`

const { loading, error, data } = useQuery(GET_USER)
```

이를 통해서, over-fetching 문제와, under-fetching 문제를 해결할 수 있습니다. 원하는 정보를 쿼리를 통해서 작성하면 끝입니다. 원하는 user



GraphQL 서버에서는 쿼리가 실행될 때마다 타입 시스템에 기초하여 쿼리의 유효성을 검사하게 됩니다.

```javascript
type User{
  id: ID!
  name: String
  email: String
	//  ...
}
```





### 장단점

- REST 에 비해서 HTTP 요청 횟수를 줄일 수 있습니다.
- Over, Under Fetching 문제 해결



#### 단점

- File 전송 등 Text 만으로 하기 힘든 내용은 처리하기 복잡합니다.
- 재귀적인 쿼리를 주의해야 합니다.
  - 일반적으로 쿼리의 max depth를 지정하게 됩니다.
- 캐싱이 어렵습니다.















## 레퍼런스

- https://velog.io/@djaxornwkd12/REST-API-vs-GraphQL-%EC%B0%A8%EC%9D%B4%EC%A0%90-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0
- 



## 질문할 사항

- GraphQL 캐싱