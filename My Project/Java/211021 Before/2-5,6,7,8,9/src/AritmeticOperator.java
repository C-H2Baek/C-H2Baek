import java.util.Scanner;

public class AritmeticOperator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("정수를 입력하세요: ");
		
		int time = scanner.nextInt();			// 정수 입력
		int second = time % 60;					// 60으로 나눈 나머지는 초
		int minute = (time / 60) % 60;			// 초 60 나누면 분
		int hour = (time / 60) / 60;			// 분 60 나누면 시
		
		System.out.print(time + " Second is ");
		System.out.print(hour + " Hour ");
		System.out.print(minute + " Minute ");
		System.out.print(second + " Second. ");
		scanner.close();
	}

}
