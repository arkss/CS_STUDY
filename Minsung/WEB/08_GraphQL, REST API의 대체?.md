# [WEB] GraphQL, REST API의 대체?

## GraphQL이란

`GraphQL` 는 Graph Query Language로 facebook에서 개발한 쿼리 언어입니다.

`GraphQL` 은 기존의 REST API의 단점들을 보안하기 위해 나온 통신 규약으로 REST API와 많이 비교됩니다.

REST API의 어떠한 문제점들을 보안하는지 알아봅시다.





## REST API의 한계

REST API는 간단한 서비스에는 문제가 없지만 서비스와 복잡해질수록 `Over-Fetching` 과 `Under-Fetching` 문제가 발생할 수 있습니다.

또한 여러 환경에 맞춰 API를 제공해야하는 것도 쉽지 않은 일입니다.

따라서 각 환경에 맞추다보니 비슷한 역할을 하지만 Endpoint가 다른 API가 많이 개발됩니다.



### Over-Fetching

`Over-Fetching`은 클라이언트의 요구사항보다 더 많은 데이터를 반환하는 경우를 말합니다.

예를 들어 생각해봅시다.

서버 개발자는 User의 여러 정보를 반환하는 API를 만들었습니다.

클라이언트는 User의 name 필드만 필요해도 API를 호출해야하고 불필요한 데이터가 많이 넘어오게 됩니다.



### Under-Fetching

`Under-Fetching`은 클라이언트에서 원하는 데이터들을 위해 여러 API를 호출하는 것을 말합니다.





## GraphQL을 통한 해결

`GraphQL`은 이러한 단점들을 모두 해결하였습니다.

하나의 Endpoint를 생성하고 클라이언트에게 필요한 데이터를 직접 쿼리를 통해 호출하게끔 하는 방식입니다.

예를 들어 위 `Over-Fetching` 같은 문제는 아래와 같은 쿼리로 필요한 데이터만 조회할 수 있습니다.

```graphql
query {
	user(user_id: 1) {
		username
	}
}
```



마찬가지로 `Under-Fetching` 도 하나의 query에 여러 데이터를 호출하여 해결할 수 있습니다.





## GraphQL의 장단점

REST API의 문제점을 해결하기 위해 등장하였다고 해서 `GraphQL`이 REST API보다 좋다는 건 아닙니다.

실제로 아직까지 현업에서는 REST API를 더 많이 사용하고 있습니다.

`GraphQL`의 장단점을 알아봅시다.



### 장점

#### 하나의 Endpoint

위에서도 언급했듯이 `GraphQL`은 하나의 Endpoint를 갖습니다.

클라이언트 입장에서도 한 군데로만 요청을 보내면 되고 여러 API를 신경쓰지 않아도 됩니다.

![img](https://owin2828.github.io/img/web/web_13_1.png)



#### 최적화된 데이터

마찬가지로 위에서 언급했던 내용으로서 `Over-Fetching` 와 `Under-Fetching` 등의 문제가 발생하지 않아 필요한 데이터만, 한 번의 요청으로 가져올 수 있습니다.



#### 환경에 종속적이지 않은 API

IOS, Android 와 같은 다른 기종에 대해 별도의 API를 개발할 필요가 없습니다.





### 단점

#### 캐싱

하나의 Endpoint를 사용하기 때문에 HTTP에 제공하는 캐싱 전략을 그대로 사용하는 것이 불가능합니다.

따라서 `GraphQL`만의 캐싱 방법이 필요합니다.



#### 파일 업로드

 `GraphQL`은 아직 파일 업로드에 대해서 구체적인 구현 방법이 정의되어 있지 않습니다.

따라서 개발자 스스로 해결해야합니다.

그렇기 때문에 업로드만을 위한 분리된 API를 개발하기도 합니다.





## 마무리

`GraphQL` 에 대해서 설명을 하다보니 자연스럽게 REST API와 비교하는 내용이 많았습니다.

비록 `GraphQL` 이 REST API의 문제점을 극복하기 위해 등장했다고는 하나 아직까지는 REST API가 더 많이 쓰이고 있습니다.

둘의 장단점이 명확하니 상황에 맞춰 적절한 통신 규약을 선택하는게 중요합니다.

