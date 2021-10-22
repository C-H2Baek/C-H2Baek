
public class LogicalOperator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 비교연산
		System.out.println('a' > 'b');
		System.out.println(3 >= 2);
		System.out.println(-1 < 0);
		System.out.println(3.45 <= 2);
		System.out.println(3 == 2);
		System.out.println(3 != 2);
		System.out.println(!(3 !=2));
		
		// 비교 연산과 논리 연산 복합
		System.out.println((3 > 2) && (3 > 4));   //  AND 연산자 모두가 1이어야 1  (0: False , 1: True)
		System.out.println((3 != 2) || (-1 > 0)); //  OR  연산자 둘중 하나가 1이면 1
		System.out.println((3 != 2) ^ (-1 > 0));  //  XOR 연산자 

	}

}
