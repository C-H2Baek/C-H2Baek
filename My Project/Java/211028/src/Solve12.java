import java.util.Scanner;

public class Solve12 {

	public static void main(String[] args) {
		String[] words = { "chair" , "computer" , "integer" , "gorgeous"};
		String[] meanings = { "의자" , "컴퓨터" , "정수" , "멋있는"};
		int count = 0;
		
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < words.length; i++) {
			char[] question = words[i].toCharArray(); // String을 char[]로 변환
		
			System.out.printf("Q%d. %s의 뜻은?" , i + 1, new String(question));
			String answer = sc.nextLine();
			// trim() answer의 좌우 공백을 제거한 후, equals로 word[i]와 비교
			if (meanings[i].contentEquals(answer.trim())) {
				System.out.printf("정답입니다.%n%n");
				count++;
			}
			else
				System.out.printf("틀렸습니다. 정답은  %s입니다. %n%n" , meanings[i]);
		}
		System.out.printf("전체  %s 문제 중 %s 문제 맞추셨습니다." , words.length, count);
		sc.close();
	}
		
}
