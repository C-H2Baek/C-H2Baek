import java.util.*;

public class OpenGame2 {

	public static void main(String[] args) {
	
	Scanner sc = new Scanner(System.in);
	Random r = new Random();
	
	while(true) {
		
		int n=1;
		int max=100;
		int min=0;
		
		int k = r.nextInt(100);
		
		System.out.println("Choose Number");
		System.out.println("0-100");
		
		while(true) {
			System.out.print(n+" >> ");
			int num = sc.nextInt();
			if(num>k) {
				max = num;
				System.out.println("DOWN");
				System.out.println(min + "-" +max);
			}
			else if (num < k) {
				min = num;
				System.out.println("UP");
				System.out.println(min+"-"+max);
			}
			else if (num==k) {
				System.out.println("Correct");
				break;
			}
			n++;
		}
		
		System.out.println("Conuinue? (Y/N)");
		String s = sc.next();
		if(s.equals("N")) {
			System.out.println("Done");
			break;
		}
		sc.close();
	}
}
}