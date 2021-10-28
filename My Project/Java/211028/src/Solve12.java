import java.util.Scanner;

public class Solve12 {

	public static void main(String[] args) {
		String[] words = { "chair" , "computer" , "integer" , "gorgeous"};
		String[] meanings = { "����" , "��ǻ��" , "����" , "���ִ�"};
		int count = 0;
		
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < words.length; i++) {
			char[] question = words[i].toCharArray(); // String�� char[]�� ��ȯ
		
			System.out.printf("Q%d. %s�� ����?" , i + 1, new String(question));
			String answer = sc.nextLine();
			// trim() answer�� �¿� ������ ������ ��, equals�� word[i]�� ��
			if (meanings[i].contentEquals(answer.trim())) {
				System.out.printf("�����Դϴ�.%n%n");
				count++;
			}
			else
				System.out.printf("Ʋ�Ƚ��ϴ�. ������  %s�Դϴ�. %n%n" , meanings[i]);
		}
		System.out.printf("��ü  %s ���� �� %s ���� ���߼̽��ϴ�." , words.length, count);
		sc.close();
	}
		
}
