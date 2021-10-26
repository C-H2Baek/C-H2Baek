
public class NestedLoop_Gugudan {

	public static void main(String[] args) {
/*		
		for(int i=1; i<10; i++) {
			System.out.println("===" + i +"´Ü===" + '\n');
			for(int j=1; j<10; j++) {
				System.out.print(i + "*" + j + "=" + i*j);
				System.out.print('\n');
			}
			System.out.println();
		}	
*/

		for(int i=1; i<10; i++) {
			for(int j=1; j<10; j++) {
				System.out.print(j + "*" + i + "=" + i*j);
				System.out.print('\t');
			}
			System.out.println();
		}
	}
}