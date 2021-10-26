
public class Solve_07 {

	public static void main(String[] args) {
	
	int armt [] = new int [10];
	
	for(int i=0; i<10; i++) {
		int k= (int)(Math.random()*10+1);
		armt[i] = k;
	}

	int sum = 0;
	
	for(int i=0; i<10; i++) {
		sum = sum + armt[i];
	}
	System.out.print("·£´ýÇÑ ¼ýÀÚµé: ");
	
	for(int i=0; i<armt.length; i++) {
		System.out.print(armt[i]+ " ");
	}
	System.out.println(" ");
	System.out.println("Æò±ÕÀº " + (double)sum/10);
	}

}
