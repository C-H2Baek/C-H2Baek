import java.util.Scanner;
public class ThreeSixNine {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("1~99 ������ ������ �Է��ϼ���)>>");
		int x = sc.nextInt();
				
		int a = x % 10;
		int b = x / 10;
		
		System.out.print("���� �ڸ��� : " + a);
		System.out.print(" ���� �ڸ��� : " + b);
		
		sc.close();
			
	}

		
	}
	
