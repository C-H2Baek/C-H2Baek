
public class Solve08 {

	public static void main(String[] args) {
		int[] answer = {1,1,2,2,2,3,3,3,3,4,4,4,4,4 };
		int[] counter = new int[4];

		for (int i = 0; i < answer.length; i++) {
			counter[answer[i] - 1]++;
			//answer[0] = 1�̹Ƿ� counter[1-1] = counter[0] = 0 -> 1
			//answer[1] = 4�̹Ƿ� counter[4-1] = counter[3] = 0 -> 1
			//answer[2] = 4�̹Ƿ� counter[4-1] = counter[3] = 1 -> 2
		}

		for (int i = 0; i < counter.length; i++) {
			System.out.print(counter[i]);
			
			for (int j = 0; j < counter[i]; j++) 
				System.out.print("*");				//������ ��� ������ ������ŭ * ���
			
			System.out.println();
		}
	}
}