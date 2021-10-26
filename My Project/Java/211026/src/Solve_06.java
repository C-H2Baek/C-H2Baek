import java.util.*;

public class Solve_06 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("금액을 입력하세요 >> ");
		int money = sc.nextInt();
		
		int [] unit = {50000,10000,1000,500,100,50,10,1};
		
		for(int i=0; i<unit.length;i++) {
			System.out.printf("%d원 짜리: %d개  " , unit[i],money/unit[i] );
			
			money = money - money/unit[i]*unit[i];
			System.out.println(" ");
		}
		sc.close();
		

	}

}
