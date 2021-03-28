# SOLID : 객체지향 프로그래밍 5가지 원칙

객체지향 프로그래밍엔 5가지 원칙이 있습니다.

각 원칙에 대해서 이해해봅시다.







## 1. 단일 책임 원칙 (SRP, Single Responsibility Principle)

> 객체는 단 하나의 책임만 가져야 한다.

- **책임이란?**

  - 객체에 책임을 할당할 때는 어떤 객체보다도 작업을 잘 할 수 있는 객체에 책임을 할당해야 합니다.

- 설계 원칙을 학습하는 이유?

  - 예측하지 못한 변경사항이 발생하더라도 
    유연하고 확장성이 있도록 시스템 구조를 설계하기 위해서!

- **좋은 설계란?**

  - 기본적으로 시스템에 새로운 요구사항이나 변경이 있을 때 
    가능한 한 영향 받는 부분을 줄이도록 하는 것입니다.

    **-> 객체가 변해야 하는 이유는 단 1개! 책임은 하나만 있기 때문!**



### 책임 분리

한 클래스에 하나의 책임만 수행하도록 만들어야합니다.

책임을 많이 지게 될 수록 코드끼리 강하게 결합될 가능성이 높아집니다.

*객체지향 프로그래밍의 낮은 결합도를 지향하기 어려워집니다.*





## 2. 개방 폐쇄의 원칙 (OCP, Open Closed Principle)

> 기존의 코드를 변경하지 않으면서 기능을 추가할 수 있도록 설계가 되어야 한다.

클래스는 확장에는 열려있고, 변경에는 닫혀있어야 합니다.
기존 요소의 수정이 아닌, 기존 요소를 확장하여 재사용한다!

설계의 기본이라고 할 수 있습니다.









## 3. 리스코프 치환 원칙 (LSP, LIskov substitution Principle)

> 자식 클래스는 부모 클래스에서 가능한 행위는 모두 가능해야 합니다.

*이전 장에서 스택의 구현에 있어 Array 상속이 아닌 위임으로 구현해야하는 이유는 LSP 원칙을 지키지 못하기 때문!*







## 4. 인터페이스 분리 원칙 (Interface Segregation Principle)

> 자신이 사용하지 않는 인터페이스는 구현하지 않는다.
> 인터페이스를 클라이언트에 특화되도록 분리시켜야 한다.

*자신과 관련없는 메소드는 구현하지 말자!*

SRP 와 유사한 성격을 띄고 있습니다.

사용하지 않는 기능(인터페이스)에는 영향을 받지 말아야 하는 원칙입니다.

스마트폰을 기준으로, 전화, 인터넷, 사진 촬영 등 다양한 기능을 사용할 수 있습니다. 하지만 전화를 할 때 다른 기능에서 필요한 동작을 하지 않습니다. 따라서 서로 완전히 독립된 인터페이스로 구현하여 서로 영향을 받지 않도록 설계를 해야합니다.





## 5. 의존 역전 원칙 (DIP, Dependency Inversion Principle)

> 클라이언트는 추상화(인터페이스)에 의존해야 하며, 구체화(구현된 클래스)에 의존해선 안된다.

의존 관계를 맺을 때 변화하기 쉬운 것보다는 변화가 없는 것에 의존해야 합니다.

클래스간 의존 관계는 한 클래스가 기능을 수행하려 할 때 다른 클래스의 서비스가 필요한 경우 의존 관계에 있다고 할 수 있습니다.

변하기 어려운 것?

- 추상 클래스
- 인터페이스

가 이에 해당합니다.



DIP를 만족시키기 위해선 **의존성 주입(Dependency Injection)이 유용하게 사용됩니다.**

- 클래스 외부에서 의존되는 것을 대상 객체의 인스턴스 변수에 주입

https://gmlwjd9405.github.io/2018/07/05/oop-solid.html 에서 참조한 코드입니다.

```java
public class Kid {
	private Toy toy;
	public void setToy(Toy toy){ this.toy = toy; }
	public void play(){ System.out.println(toy.toString()); }
}

public class Robot extends Toy {
	public String toString() { return "Robot"; }
}

public class Lego extends Toy {
	public String toString() { return "Lego"; }
}
```

```java
public class Main {
  public static void main(String[] args) {
    Kid k = Kid();
    Toy t = new Robot();
    k.setToy(t); // robot toy 로 set
    k.play();

    Toy t = new Lego();
    k.setToy(t);// lego toy 로 set
    k.play();
  }
}

```

기존 코드에 영향 없이 장난감을 바꿀 수 있습니다.









## 레퍼런스

- https://gmlwjd9405.github.io/2018/07/05/oop-solid.html





## 질문할 사항

- 





## 추가 공부할 키워드







