# 09. gRPC란?

> google Remote Procedure Call

구글에서 개발한 RPC 프레임워크라고 할 수 있습니다.





## RPC는 뭐지?

RPC(원격 프로시저 호출)는 Remoet Procedure Call 로 프로세스 간 통신 기법 중 하나입니다.

다른 프로세스에 있는 함수를 호출할 때, 같은 프로세스 내에 있는 것처럼 호출할 수 있습니다.

이는 플랫폼에 제약이 사라지기 때문에 분산 시스템 기법에 효과적이라고 합니다.



### 등장 배경

- 기능별로 여러 서버로 분산시키는 server-client model 형태를 채택하게 되고,
- 프로세스간 통신 방법에서 소켓의 경우 통신 관련 장애, 데이터 처리를 개발자가 모두 하게 되는 어려움
  - 데이터에 따라 포맷팅, 장애 처리, ~~

이에 따라 RPC 가 등장합니다.

**네트워크로 연결된 서버 상의 프로시저를 원격으로 호출하는 기능입니다.** 









## 레퍼런스

- https://brownbears.tistory.com/512
- https://medium.com/naver-cloud-platform/nbp-%EA%B8%B0%EC%88%A0-%EA%B2%BD%ED%97%98-%EC%8B%9C%EB%8C%80%EC%9D%98-%ED%9D%90%EB%A6%84-grpc-%EA%B9%8A%EA%B2%8C-%ED%8C%8C%EA%B3%A0%EB%93%A4%EA%B8%B0-1-39e97cb3460
- 