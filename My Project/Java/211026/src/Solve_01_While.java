
public class Solve_01_While {

	public static void main(String[] args) {
		int sum = 0 , i=0;
		while(i<100) {
			sum= sum + i;
			i+=2;
			System.out.println(i);
		}
		System.out.println(sum);
	}
}
