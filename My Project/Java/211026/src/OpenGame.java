import java.util.Random;
import java.util.Scanner;

public class OpenGame {

	public static void main(String[] args) {
		
		int i=0;
		int num;
		Random r = new Random();
		Scanner s = new Scanner(System.in);
		int x = r.nextInt(100);
		
		
		do {
			System.out.println("Choose Number : (0~100)");
			num = s.nextInt();
		
			if (x>num) {
				System.out.println("UP");
			}
			else if (x<num) {
				System.out.println("DOWN");
			}
			i++;
			System.out.print("Number of Attempts : " + i + '\n');
			
		}
		
		while (x!=num); {
		System.out.println("Correct! Number of Attempts is :" + i);
		
		System.out.println("Continue? Y or N");
		String t = s.next();
		if(t.equals("N")) {
			System.out.println("STOP");
//			break;
			
		
			s.close();
		}
		}
	}
}
