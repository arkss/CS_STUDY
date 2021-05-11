# Proxy



## Proxy 란?

"대리"





근데 너무 많다!

스프링 프록시, 네트워크 프록시 ,, ...



## 프록시 서버

대신 처리하는 서버



클라이언트와 서버 사이에 위치



클라이언트와 서버 간의 중계 서버로 통신을 대리 수행하는 서버

캐시 보안 트래픽 분산등 장점을 가짐



### 포워드 프록시

일반적인 프록시는 포워드 프록시를 말함!

- 인터넷 속도 향상??

- 외국 접속?

- IP 추적 방지 위해 프록시??





특징

- 캐싱
  - 클라이언트가 요청한 내용을 캐싱
    - 여러 클라이언트가 같은 내용을 요청한다면?
    - 전송 시간 절약
    - 불필요한 외부 전송 X
    - 외부 요청 감소함에 따라 네트워크 병목현상 감소
- 익명성
  - 클라이언트가 서버로 보낸 요청을 감춤
    - 포워드 프록시가 서버에 정보를 전달하기에 익명성 보장 가능(서버가 받는 요청 IP 는 프록시의 IP)







### 리버스 프록시

서버와 인터넷 사이에 존재하는 서버



특징

- 캐싱
- 보안
  - 서버 정보를 클라이언트로부터 숨길 수 있음
    - 클라이언트 입장에서 서버는 리버스 프록시를 보고 있음
    - 실제 서버의 IP가 노출되지 않음

- 로드 밸런싱 (Optional)



### 로드 밸런싱

**부하 분산**

서버가 해야할 작업을 분산



**쓰는 이유는?**

사용자가 증가? 스케일 업해서 소화 가능

사용자가 더 증가한다면? 스케일 업의 한계가 있다.

비용적인 측면, 하드웨어적 측면, ....

**스케일 아웃!!!**





####  종류

OSI 7계층 기준으로 어떤 것을 나누는 지에 따라 로드 밸런서 종류가 달라짐

- L2
  - MAC 주소 기반으로 
- L3
  - IP 주소 기반으로
- L4
  - 전송 계층 : IP 와 포트 레벨에서 로드 밸런싱
    - 특정 사이트로 접근 시 서버 A와 서버 B로 나눠줌
- L7
  - 응용 계층 : User Request 기반으로 로드 밸런싱
    - /category, /search 등 url, 요청 방법, 쿼리 파라미터에 따라 로드 밸런싱을 진행







### 프록시 서버 통한 무중단 배포

- EC2 서버 통해서 NGINX를 프록시 서버로 사용

- 사용자는 NGINX 만 볼 수 있음

- NGINX가 8081 포트를 가리키고 있고, 새로운 서버는 8082 포트에 띄움
  - 기존 요청은 8081로, 
  - 배포가 끝나면 8082 포트로!
  - 오류가 있었다면 다시 8081로 포트만 돌리면 된다.
