import java.util.Scanner;

public class Solve_04 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("�ҹ��� �˹ٺ� �ϳ� �Է��Ͻÿ� >> ");
		String s = sc.next();
		char c = s.charAt(0);
		
			for(int i = 0; i<=c-'a'; i++) {
				for(char k = 'a'; k<= c-i; k++) {
					System.out.print(k);
				}
				System.out.println();
			}
		sc.close();

	}

}
