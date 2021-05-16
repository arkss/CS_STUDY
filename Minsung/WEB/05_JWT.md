# [WEB] Authentication (2) JWT

저번 포스팅에 이어 이번엔 인증하는 두 번째 방법, JWT에 대해서 알아보겠습니다.

[[WEB] Authentication (1) 세션과 쿠키](https://ssungkang.tistory.com/entry/WEB-Authentication-1-%EC%84%B8%EC%85%98%EA%B3%BC-%EC%BF%A0%ED%82%A4)



## JWT 란

JWT란 Json Web Token의 줄임말로 json 형태의 token입니다.

JWT을 만들기 위해서는 `header`, `payload`, `verify signature` 총 3가지가 필요합니다.

그리고 3개를 `.` 으로 조합하여 아래와 같은 형태로 만들어집니다.

``` 
header.payload.verify_signature
```

 

### header

header는 일반적으로 token의 타입과 signing 알고리즘이 포함됩니다.

``` json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

그 후 JSON은 Base64Url로 인코딩 됩니다.



### payload

payload는 추가적인 데이터를 넣을 수 있습니다.

``` json
{
  "name": "minsung"
}
```

그 후 JSON은 Base64Url로 인코딩 됩니다.

signing된 JWT는 변조로부터 보호되지만 누구나 읽을 수 있습니다.

따라서 별도의 암호화가 없다면 payload에 보안 상 중요한 값은 넣지 않습니다.



### verify signature

verify signature을 생성하기 위해 인코딩된 header, 인코딩된 payload, secret이 필요합니다.

예를 들어 signing 알고리즘이 `HS256` 인 경우에는 아래와 같이 생성됩니다.

``` json
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```



verify signature은 메세지가 변조되지 않았음을 확인하는데 사용됩니다.



아래 사이트에서 직접 JWT를 만들어 볼 수 있습니다.

https://jwt.io/#debugger-io





## JWT를 이용한 인증

![image-20210516223138588](/Users/rkdalstjd9/Library/Application Support/typora-user-images/image-20210516223138588.png)

1. 클라이언트에서 인증서버로 권한을 요청합니다. 다양한 방법이 있겠지만 일반적으로 올바른 아이디와 패스워드를 입력하여 인증을 받을 수 있습니다.
2. 인증서버에서 JWT를 생성하여 클라이언트에게 반환합니다.
3. 클라이언트는 JWT를 사용하여 보호된 리소스들에 접근할 수 있습니다.







## JWT의 장단점

### 장점

* 인증에 필요한 모든 정보를 토큰 자체가 포함하기 때문에 별도의 인증 저장소가 필요 없습니다.
* 다른 token들에 비해 크기가 작아 트래픽에 대한 부담이 낮습니다.
* expired 기능을 내장하고 있습니다.
* 수평 스케일링에 용이합니다.
* micro service 환경에서 중앙집중식 인증서버에서 벗어나 개별 micro service에서 해결할 수 있습니다.

### 단점

* JWT를 클라이언트에 저장하여 사용하기 때문에 DB에서 값이 바뀌더라도 JWT에 바로 적용할 수 없습니다.

* payload에 데이터가 많아지면 JWT의 크기가 커집니다.
* JWT는 거의 모든 요청에 전송되므로 트래픽 크기에 영향을 미칠 수 있습니다.
* 한 번 발급한 JWT는 값을 수정하거나 폐기가 불가능합니다.
* 기본적으로 암호화하지 않기 때문에 정보가 노출 될 수 있습니다.





## Refresh Token

`Refresh Token` 은 JWT의 단점들을 극복하기 위해 나온 개념입니다.

https://tansfil.tistory.com/59





## 레퍼런스





## 질문할 사항



## 추가 공부할 키워드

* 암호와 Signing의 차이
* 클라이언트에서 JWT를 잘 관리하는 방법