package newanagement;


import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		
		DAO dao = new DAO();
		Scanner sc = new Scanner(System.in);
		int menu;
		
		do {
			System.out.print("1. ȸ������ |\n2. ȸ�� ���  |\n3. ȸ���˻�  |\n4. ȸ�� ���� ����  |\n5. ȸ�� ����  |\n6. ȸ�� Ż�� |\n0.����\n ����>>> ");
			
			menu = Integer.parseInt(sc.nextLine());
			
			switch(menu) {
			case 1:
				// ȸ�� ����
				dao.MemberJoin();
				break;
			case 2:
				dao.selectMember();
				break;
			case 3:
				dao.search();
				break;
			case 4:
				dao.reInfo();
				break;
			case 5:
				dao.sortMember();
				break;
			case 6:
				dao.removeMember();
				break;
			
			}
		}while(menu != 0);
		System.out.print("���α׷��� �����մϴ�");
		sc.close();
	}
}


