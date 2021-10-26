
public class Solve_10 {

	public static void main(String[] args) {
		
		int array [][]=new int[4][4];
		int x; int y; int n=0;
		
		while(n<10) {//0_9
		x=(int)(Math.random()*4);
		y=(int)(Math.random()*4);
		
		if(array[x][y]==0) {
			array[x][y] = (int)(Math.random()*10+1);
			n++;
		}		
		}
		
		for(int i=0; i<array.length;i++) {
			for(int k=0; k<array[i].length;k++) {
				System.out.print(array[i][k]+ " ");
			}
			System.out.println(" ");
		}
	}
}
