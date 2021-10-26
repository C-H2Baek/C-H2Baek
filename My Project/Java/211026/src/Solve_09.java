
public class Solve_09 {

	public static void main(String[] args) {

		int n [][] = new int[4][4];
		
		for(int i=0; i<n.length;i++) {
			for(int k=0; k<n[i].length;k++) {
				n[i][k] = (int)(Math.random()*10+1);
			}
		}
		
		for(int i=0; i<n.length;i++) {
			for(int k=0; k<n[i].length;k++) {
				System.out.print(n[i][k] + " ");
			}
			System.out.println(" ");
		}
	}

}
