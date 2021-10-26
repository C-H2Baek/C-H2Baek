
public class Solve_01_DoWhile {

	public static void main(String[] args) {
		
		int sum=0, i=0;
		
		do {
			sum=sum+i;
			i+=2;
			System.out.println(i);
		}
		while(i<100);
		System.out.println(sum);
	}

}
