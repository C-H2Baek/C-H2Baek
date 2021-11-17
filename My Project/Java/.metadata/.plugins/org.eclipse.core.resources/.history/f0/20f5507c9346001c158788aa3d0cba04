/* 	부모 생성자의 호출 : Super
   	자바에서는 자식 객체를 생성하면, 부모 객체를 먼저 생성한 후 , 자식 객체가 그 다음에 생성
   	
 */

public class SuperEx {
	String name;
	int price;
	
	public SuperEx (String name, int price) {
		this.name = name;
		this.price = price;
	}
	public void Print() {
		System.out.println("책의 이름과 가격 : " + name + " " + price);
	}
public static class ChildBook extends SuperEx{
	ChildBook (){
		super("나의 라임오렌지 나무", 10000);
	}
	
	public static void main (String[] args) {
		ChildBook Child = new ChildBook();
		System.out.print("[구현 결과 2] : ");
		Child.Print();
	}
}
}

