import java.util.Scanner;

public class Solve06 {

	public static void main(String[] args) {
		// 큰 금액의 동전을 우선적으로 거슬러 준다.
		Scanner scanner = new Scanner(System.in);
		int[] coinUnit = {500, 100, 50, 10};
		
		System.out.println("돈 액수를 입력하세요 : ");
		int money = scanner.nextInt();
		int coin50000 = 0;
		int coin10000 = 0;
		int coin5000 = 0;
		int coin1000 = 0;
		int coin500 = 0;
		int coin100 = 0;
		int coin50 = 0;
		int coin10 = 0;
				
		System.out.println("money="+money);
				
		for(int i=0; i<coinUnit.length; i++) {
			coin50000 = money / 50000;
			coin10000 = money % 50000 / 10000;
			coin5000  = money % 10000 / 5000;
			coin1000  = money % 5000  / 1000;
			coin500   = money % 1000  / 500;
			coin100   = money % 500   / 100;
			coin50    = money % 100   / 50;
			coin10    = money % 50    / 10;
			// 코드 삽입부분
		}
		System.out.println("50000원 : " + coin50000);
		System.out.println("10000원 : " + coin10000);
		System.out.println("5000원 : " + coin5000);
		System.out.println("1000원 : " + coin1000);
		System.out.println("500원 : " + coin500);
		System.out.println("100원 : " + coin100);
		System.out.println("50원 : " + coin50);
		System.out.println("10원 : " + coin10);
		scanner.close();
	}
}
