# [WEB] stateful vs stateless

## Stateful

`Stateful` 은 세션 정보를 서버에 저장하고 세션의 state에 따라 응답하는 것을 말합니다.

대표적으로 `Stateful` 구조를 따르는 프로토콜은 TCP 입니다.

TCP는 송신자와 수신자가 3-way handshaking을 통해 연결을 맺습니다.

그 후 window size나 sequence number 등 각종 정보를 계속 유지한 체로 통신을 이어갑니다.





## Stateless

`Stateless` 은 서버가 세션 정보를 저장하지 않아 세션의 state에 상관없이 응답하는 것을 말합니다.

서버는 단순히 요청에 대한 응답만 하며 세션관리는 클라이언트에 의해 이루어집니다.

대신 서버는 필요에 따라 외부 DB에 저장하여 관리할 수 있습니다.

대표적으로 `Stateless` 구조를 따르는 프로토콜은 UDP, HTTP 입니다.

둘 모두 TCP처럼 handshaking을 하지 않고 단순히 데이터를 보내기만 합니다.





## Stateful vs Stateless

최신 웹서비스 구조는 모두 `Stateless` 를 사용하고 있습니다.

각각의 장단점이 있지만 가장 큰 이유는 바로 **Scaling** 입니다.



`Stateful` 의 경우 서버가 세션을 저장하고 있기 때문에 만약 Scale out 할 시 새로운 서버에는 저장되어 있지 않습니다.

따라서 이에 대한 새로운 대응책이 필요합니다.

![img](https://blog.kakaocdn.net/dn/bNtOsJ/btqzC14OCRf/d9FxSIR0PkgVzrqQu0S2X0/img.png)



하지만 `Stateless` 의 경우에는 다릅니다.

서버가 클라이언트의 세션을 관리하지 않으므로 Scale out 시에도 문제가 되지 않습니다.



![img](https://blog.kakaocdn.net/dn/K6F9X/btqzCqdwXax/PvudfGUQvnLhJK1qsXNek0/img.png)





## 레퍼런스

https://5equal0.tistory.com/entry/StatefulStateless-Stateful-vs-Stateless-%EC%84%9C%EB%B9%84%EC%8A%A4%EC%99%80-HTTP-%EB%B0%8F-REST



## 질문할 사항



## 추가 공부할 키워드

