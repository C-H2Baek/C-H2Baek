import java.util.*;
public class Solve_05 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("���� ���� 10���� �Է��Ͻÿ� >> ");
		
		
		int n[] = new int[10];
		for(int i=0; i<10; i++) {
			n[i] = sc.nextInt();
		}
		
		System.out.print("3�� ����� ");
		for(int i=0; i<10; i++) {
			if(n[i]%3==0)  
				System.out.print(n[i] + " ");
				else continue;
			
			}
		sc.close();
		}

	}



