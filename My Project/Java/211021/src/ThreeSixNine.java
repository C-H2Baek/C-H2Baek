import java.util.Scanner;
public class ThreeSixNine {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("1~99 사이의 정수를 입력하세요)>>");
		int x = sc.nextInt();
				
		int a = x % 10;
		int b = x / 10;
		
		System.out.print("일의 자리수 : " + a);
		System.out.print(" 십의 자리수 : " + b);
		
		sc.close();
			
	}

		
	}
	
