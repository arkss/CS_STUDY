# 03. CORS

## 01. SOP와 CORS

SOP는 Same-Origin Policy의 줄임말로서 같은 출처에서만 리소스를 공유하도록 한다는 정책입니다.

하지만 웹에서 다른 출처에 있는 리소스를 가져와서 사용하는 일은 비일비재 하기 때문에 무작정 막는 것만이 상책이 아닙니다.

따라서 예외를 허용하기로 했는데 그 중 하나가 CORS 정책을 지킨 리소스 요청입니다.



CORS란 Cross-Origin Resource Sharing의  줄임말로 한국어로 교차 출처 리소스 공유입니다.

여기서 Origin은 서버의 위치를 의미합니다. 서버의 위치라고 함은 protocol과 host, port 번호를 합친 것을 말합니다.



### 왜 다른 출처를 막는가

웹은 보안에 취약한 환경입니다.

브라우저의 개발자 도구만 봐도 알 수 있는 정보가 상당히 많습니다.

이런 환경에서 서로 다른 출처의 어플리케이션이 서로 통신하는데 아무런 제약을 두지 않는다면 CSRF, XSS 등 여러 공격에 쉽게 노출되게 됩니다.



### 판단은 브라우저에서

따라서 같은 출처인지 아닌지를 판단해야 하는데 이 판단은 브라우저에서 이루어집니다.

만약 CORS 정책을 위반하는 리소스 요청을 하더라도 서버는 정상적으로 응답하고 이후 브라우저가 응답을  보고 CORS 정책에 위반되는지를 판단해 버릴지 말지를 결정합니다.

그렇기 때문에 브라우저를 통하지 않고 서버끼리 통신을 할 때는 이 정책이 적용되지 않습니다.



## 02. CORS의 동작 원리

어플리케이션이 다른 리소스에 요청을 할 때 HTTP 헤더 `Origin` 필드에 요청을 보내는 출처를 함께 보냅니다. 

서버는 응답 시, HTTP 헤더 `Access-Control-Allow-Origin` 필드에 접근이 허용된 출처들을 내려줍니다.

브라우저는 두 필드를 비교하여 CORS 정책에 위배되는지를 확인합니다.

> request Origin을 어떻게 기억하고 있지?



이는 기본적인 흐름으로 크게 세 가지 시나리오에 따라 더 구체적으로 나눠집니다.



### Preflight Request

`Preflight` 방식은 웹 어플리케이션을 개발할 때 가장 일반적입니다.

브라우저는 요청을 한 번에 보내지 않고 `Preflight` (예비요청) 와 본 요청을 나눠서 보냅니다.

`Preflight` 시에 `OPTIONS` 메서드가 사용되어 본 요청을 하기 전 서버와의 통신이 안전한지 확인합니다.



만약 `Preflight` 에서 CORS를 위배하게 된다면 본 요청은 보내지 않게 됩니다.



### Simple Request

이는 별도의 예비요청없이 바로 본 요청을 보내는 방식입니다.

하지만 마음대로 예비요청을 생략할 수는 없고 아래와 같은 특수한 조건이 필요합니다.

1. 요청의 메소드는 `GET`, `HEAD`, `POST` 중 하나여야 한다.
2. `Accept`, `Accept-Language`, `Content-Language`, `Content-Type`, `DPR`, `Downlink`, `Save-Data`, `Viewport-Width`, `Width`를 제외한 헤더를 사용하면 안된다.
3. 만약 `Content-Type`를 사용하는 경우에는 `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`만 허용된다.

2,3번 조건을 충족시키기가 까다롭습니다.

 `Preflight Request` 방식과는 예비요청이 없다는 점이 다를 뿐 CORS 관점에서는 동일합니다.



### Credentialed Request

다른 출처 간 통신에서 보안을 강화하는 방법으로 인증된 요청을 사용합니다.

브라우저가 기본적으로 제공하는 API 요청은 쿠키 정보나 인증과 관련된 헤더를 요청에 담지 않습니다.

따라서 `credentials` 옵션을 사용하여 헤더에 쿠키와 인증과 관련된 헤더를 담을 수 있습니다.

1. same-origin : default 값으로 같은 출처 간 요청에만 인증 정보를 담을 수 있습니다.
2. include : 모든 요청에 인증 정보를 담을 수 있다.
3. omit : 모든 요청에 인증 정보를 담지 않는다.



## 03. CORS를 해결할 수 있는 방법

### Access-Control-Allow-Origin

위에서도 언급했지만 `Access-Control-Allow-Origin` 필드는 응답 시 허용하는 Origin을 명시합니다.

`*` 을 사용하여 모든 요청을 허용할 수 도 있지만 이는 보안 상 문제가 있기 때문에 정확한 Origin을 명시하는걸 추천합니다.



### Proxy

https://ssungkang.tistory.com/entry/react-react-create-app%EC%9D%98-Proxy



## 레퍼런스

* https://evan-moon.github.io/2020/05/21/about-cors/#credentialed-request

  

## 질문할 사항



## 추가 공부할 키워드

* CSRF, XSS 등 웹 취약점 공격