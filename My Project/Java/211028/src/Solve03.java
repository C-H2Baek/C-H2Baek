
public class Solve03 {

	public static void main(String[] args) {
		int[] arr = {10, 20, 30, 40, 50};
		int sum = 0;
		
		// �ڵ� ���Ժκ�
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		
		System.out.println("sum = "+sum);
	}
}