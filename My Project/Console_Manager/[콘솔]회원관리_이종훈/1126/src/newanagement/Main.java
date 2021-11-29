package newanagement;


import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		
		DAO dao = new DAO();
		Scanner sc = new Scanner(System.in);
		int menu;
		
		do {
			System.out.print("1. 회원가입 |\n2. 회원 목록  |\n3. 회원검색  |\n4. 회원 정보 수정  |\n5. 회원 정렬  |\n6. 회원 탈퇴 |\n0.종료\n 선택>>> ");
			
			menu = Integer.parseInt(sc.nextLine());
			
			switch(menu) {
			case 1:
				// 회원 가입
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
		System.out.print("프로그램을 종료합니다");
		sc.close();
	}
}


