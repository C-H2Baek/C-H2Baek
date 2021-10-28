
public class Solve07 {

	public static void main(String args[]) {
		
		if (args.length != 1) {
			System.out.println("USAGE: practice");
			System.exit(0);
		}

		// 문자열을 숫자로 변환
		// 입력한 값이 숫자가 아닐 경우 예외 발생
		int money = Integer.parseInt(args[0]);

		System.out.println("money =" + money);
		
		
		int[] coinUnit = { 500, 100, 50, 10 }; // 동전의 단위
		int[] coin = { 5, 5, 5, 5 }; // 단위별 동전의 개수

		for (int i = 0; i < coinUnit.length; i++) {
			int coinNum = 0;
			
			coinNum = money / coinUnit[i];
			
			if (coin[i] >= coinNum)
				coin[i] -= coinNum;
			else {
				coinNum = coin[i];
				coin[i] = 0;
			}
			
			money -= coinNum * coinUnit[i];

			System.out.println(coinUnit[i] + "원 : " + coinNum);
		}

		if (money > 0) {
			System.out.println("거스름돈이 부족합니다.");
			System.exit(0); // 프로그램 종료
		}

		System.out.println("= 남은 동전의 개수 =");

		for (int i = 0; i < coinUnit.length; i++) {
			System.out.println(coinUnit[i] + " :" + coin[i]);
		}
	}
}