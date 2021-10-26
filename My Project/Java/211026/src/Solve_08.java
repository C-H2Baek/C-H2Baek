import java.util.*;

public class Solve_08 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("정수 개수 >> ");
		int num = sc.nextInt();
		
		int array[] = new int[num];
		for(int i=0; i<array.length;i++) {
			int n= (int)(Math.random()*100+1);
			int check=0;
			for(int k=0; k<array.length;k++) {
				if(n == array[k]) {
					check = 1;
					break;
				}
			}
			if(check==1) {
				i--;
				continue;
			}
			else array[i] =n;
		}
		for(int i=0; i<array.length;i++) {
			System.out.print(array[i]+ " ");
			if(i%9==0 && i !=0)
				System.out.println(" ");
		}
		sc.close();
	}
}
