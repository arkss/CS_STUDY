# 06. TCP/IP 4계층

## 1. TCP/IP 4계층

### TCP/IP 4계층이란?

**TCP/IP 4계층** 은 OSI 7계층을 기반으로 만들어진 모델입니다.

OSI 7계층이 개념적인 모델이었다면 TCP/IP 4계층은 실무적으로 이용될 수 있도록 단순화된 모형입니다.

> TCP/IP란 통상 IP 프로토콜 위에 TCP 프로토콜이 놓이게 되므로 이와 같이 명명합니다.



### TCP/IP 4계층의 각 계층

![](/Users/rkdalstjd9/Desktop/CS_STUDY/Minsung/images/network/06_TCP_IP_계층.png)





#### 4. 응용 계층

* Application Layer, OSI 7계층의 세션 계층, 표현 계층, 응용 계층

* TCP/UDP 기반의 응용 프로그램을 구현할 때 사용
* 데이터 단위 : data / message

* 프로토콜 : FTP, HTTP, SSH



#### 3. 전송 계층

* Transport Layer, OSI 7계층의 전송 계층
* 호스트 간의 자료 송수신에 사용

* 데이터 단위 : segment

* 프로토콜 : TCP, UDP
* 전송 주소 : Port



#### 2. 인터넷 계층

* Internet Layer, OSI 7계층의 네트워크 계층

* 데이터 전송을 위한 논리적 주소 지정 및 경로 지정
* 데이터 단위 : Packet

* 프로토콜 : IP, ARP, RARP
* 전송 주소 : IP



#### 1. 네트워크 액세스 계층

* Network Access Layer or Network Interface Layer, OSI 7계층의 물리계층과 데이터 링크 계층

* 실제 데이터인 프레임을 송수신
* 데이터 단위 : Frame
* 프로토콜 : Ethernet, PPP
* 전송 주소 : MAC



 




## 레퍼런스

https://hahahoho5915.tistory.com/15

https://www.joinc.co.kr/w/Site/Network_Programing/Documents/IntroTCPIP