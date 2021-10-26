import java.util.*;
public class Solve_03 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("정수를 입력하시요>> ");
		int n = sc.nextInt();
		
		for(int i=0; i<n; i++) {
			for(int k=0; k<n-i;k++) {
				System.out.print("*");
			}
			System.out.println(" ");
		}
		sc.close();
	}
}
