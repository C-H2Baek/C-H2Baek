import java.util.Scanner;

public class Solve06 {

	public static void main(String[] args) {
		// ū �ݾ��� ������ �켱������ �Ž��� �ش�.
		Scanner scanner = new Scanner(System.in);
		int[] coinUnit = {500, 100, 50, 10};
		
		System.out.println("�� �׼��� �Է��ϼ��� : ");
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
			// �ڵ� ���Ժκ�
		}
		System.out.println("50000�� : " + coin50000);
		System.out.println("10000�� : " + coin10000);
		System.out.println("5000�� : " + coin5000);
		System.out.println("1000�� : " + coin1000);
		System.out.println("500�� : " + coin500);
		System.out.println("100�� : " + coin100);
		System.out.println("50�� : " + coin50);
		System.out.println("10�� : " + coin10);
		scanner.close();
	}
}
