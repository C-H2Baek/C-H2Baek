import java.util.Scanner;

public class RockRaperScissors {

	public static void main(String[] args) {
        System.out.println("���������� �����Դϴ�. ����, ����, �� �߿��� �Է��ϼ���");
        Scanner sc = new Scanner(System.in);
        System.out.print("ö�� >> ");
        String cs = sc.next();
        System.out.print("���� >> ");
        String yh = sc.next();
        
        if(cs.equals("����")&&yh.equals("��")) {
        	System.out.println("ö���� �̰��");
        }
        else if(cs.equals("����")&&yh.equals("����")) {
        	System.out.println("ö���� �̰��");
        }
        else if(cs.equals("��")&&yh.equals("����")) {
        	System.out.println("ö���� �̰��");
        }
        else if(cs.equals(yh)) {
        	System.out.println("����");
        }
        else {
        	System.out.println("ö���� ���ܴ�");
        }
        sc.close();
		
	}

}
