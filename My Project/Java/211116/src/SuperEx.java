/* 	�θ� �������� ȣ�� : Super
   	�ڹٿ����� �ڽ� ��ü�� �����ϸ�, �θ� ��ü�� ���� ������ �� , �ڽ� ��ü�� �� ������ ����
   	
 */

public class SuperEx {
	String name;
	int price;
	
	public SuperEx (String name, int price) {
		this.name = name;
		this.price = price;
	}
	public void Print() {
		System.out.println("å�� �̸��� ���� : " + name + " " + price);
	}
public static class ChildBook extends SuperEx{
	ChildBook (){
		super("���� ���ӿ����� ����", 10000);
	}
	
	public static void main (String[] args) {
		ChildBook Child = new ChildBook();
		System.out.print("[���� ��� 2] : ");
		Child.Print();
	}
}
}

