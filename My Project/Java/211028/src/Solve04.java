
public class Solve04 {

	public static void main(String[] args) {
		int [][] arr = {
				{ 5, 5, 5, 5, 5},
				{10,10,10,10,10},
				{20,20,20,20,20},
				{30,30,30,30,30}
		};
		
		int total = 0;
		float avg = 0;
		
		//코드 삽입부분
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				total += arr[i][j];
			}
		}
			avg = (float)total / (arr.length * arr[0].length);
				
		//System.out.println("1차원배열값:" + arr.length + " 2차원배열값:" + arr[0].length);
		System.out.println("total="+total);
		System.out.println("avarage="+avg);
		
	} // end of main
}	  // end of class
