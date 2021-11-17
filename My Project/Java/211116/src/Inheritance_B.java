/* 
자바 (JAVA) - 상속(Inheritance) 클래스 상속, 부모 생성자의 호출

자바에는 상속(Inheritance)이라는 개념이 존재한다
쉽게 말해 부모 클래스(상위 클래스)와 자식 클래스(하위 클래스)가 있으며, 자식 클래스는 부모 클래스를 선택해서,
그 부모의 맴버를 상속받아 그대로 쓸 수 있게 된다.

상속을 하는 이유는 간단하다. 이미 마련되어 있던 클래스를 재사용해서 만들 수 있기 때문에 효율적이고, 시간을 줄인다.
상속을 하더라도 자식 클래스가 부모의 모든 것들을 물려받는 것은 아니다

● 부모 클래스의 private 접근 제한을 갖는 필드 및 메소드는 자식이 물려 받을 수 없다.
● 부모와 자식 클래스가 서로 다른 패키지에 있다면, 부모의 default 접근 제한을 갖는 필드 및 메소드도 
   자식이 물려받을 수 없다. ( default 접근 제한은 '같은 패키지에 있는 클래스'만 접근이 가능하게 하는 접근 제한자.
● 그 이외의 경우는 모두 상속의 대상이 된다.

클래스 상속

상속받고자 하는 자식 클래스명 옆에 extends 키워드를 붙이고, 상속할 부모 클래스명을 적는다.
자바는 다중 상속을 허용하지 않으므로, extends 뒤에는 하나의 부모 클래스만 와야 한다.

*/

public class Inheritance_B{
	String name;
	int price;

public void Print() {
	System.out.println("책의 이름과 가격 : " + name + " " + price);
}

public static class ChildBook extends Inheritance_B{
	ChildBook (String name, int price){
		this.name = name;
		this.price = price;
	}
}
public static void main (String[] args) {
	ChildBook Child = new ChildBook("나의 라임오렌지 나무", 10000);
	System.out.print("[구현 결과 1]");
	Child.Print();
	}
}

 /* ChildBook 클래스가 ParentBook의 필드와 메소드를 상속
	ChildBook 클래스 내에 따로 필드나 메소드가 선언되어 있지 않아도,
	생성자의 this.name 선언이나, main 메소드의 Child.Print()가 컴파일 에러가 나지 않는다.
 */






















