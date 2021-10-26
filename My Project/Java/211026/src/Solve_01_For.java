
public class Solve_01_For {

	public static void main(String[] args) {
		int sum = 0;
		for(int i=0; i<100; i=i+2) {
			sum= sum+i;
			System.out.println(i);
		}
		System.out.println(sum);
	}
}
