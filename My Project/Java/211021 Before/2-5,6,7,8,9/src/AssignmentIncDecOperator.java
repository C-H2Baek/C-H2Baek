
public class AssignmentIncDecOperator {

	public static void main(String[] args) {
		int a=3, b=3, c=3;
		// 대입 연산자 사례
		a += 3;	// a=a+3
		b *= 3; // b=b*3
		c %= 2; // c=c%2
		System.out.println("a=" + a + ", b=" + b + ", c=" + c);
		// TODO Auto-generated method stub
		
		int d=3;
		// 증감 연산자 사례
		a = d++;
		System.out.println("a=" + a + ", d=" + d);
		a = ++d;
		System.out.println("a=" + a + ", d=" + d);
		a = d--;
		System.out.println("a=" + a + ", d=" + d);
		a = --d;
		System.out.println("a=" + a + ", d=" + d);
		
		int opr = 4;
		System.out.println(opr++);
		int f = 4;
		System.out.println(++f);
		
	}
}


