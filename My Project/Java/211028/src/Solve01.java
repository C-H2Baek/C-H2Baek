
public class Solve01 {

	public static void main(String[] args) {
		
		int[] arr[]; 			// O
		int[] arr2 = {1,2,3,}; 		// O (끝에 , 있어도 OK)
		int[] arr3 = new int[5]; 		// O
		//int[] arr4 = new int[5]{1,2,3,4,5}; 	// X ({} 안에 있는 데이터의 개수에 의해 자동으로 크기가 결정되므로 [5]와 같이 크기를 지정할 수 없음)
		//int arr5[5]; 				// X (배열 선언 시 크기 지정 불가) -> int[] arr = new arr[5]; 와 같이 객체를 생성하며 크기 지정 가능
		int[] arr6[] = new int[3][];		// O

	}
}
