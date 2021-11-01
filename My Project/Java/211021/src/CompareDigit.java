import java.util.Scanner;

public class CompareDigit {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.print("2�ڸ��� �� �Է��ϼ���(10~99)>>");
	        
	        int a=sc.nextInt();
	        
	        int b,c;
	        
	        b = a%10; //�����ڸ�
	        c = a/10; //�����ڸ�
	        
	        System.out.println("�����ڸ� " + c + "�����ڸ� " + b);
	        if (b==c) {
	        	System.out.println("�� ���ܴ�");
	        }
	        else {
	        	System.out.println("�ٸ��ܴ�");
	        }
			sc.close();     
	    }
			
	}
	
}
