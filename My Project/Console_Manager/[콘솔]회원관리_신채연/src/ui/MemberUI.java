/*예외처리한 파일: 
 * ui/MemberUI,
 * action/MemberSearchAction, MemberUpdateAction
 * svc/MemberSearchService
 * util/ConsoleUtil
*/

package ui;

import java.util.Scanner;
import java.util.InputMismatchException;

import action.Action;
import action.MemberDeleteAction;
import action.MemberListAction;
import action.MemberUpdateAction;
import action.MemberRegistAction;
import action.MemberSearchAction;
import controller.MemberController;
import vo.Member;

public class MemberUI {
	// static
	public static Member[] memberArray = new Member[0];

	public static void main(String[] args) {

		MemberController memberController = new MemberController();
		boolean stop = false;
		Scanner sc = new Scanner(System.in);
		Action action = null;
		int menu = 0;
		do {
			System.out.println("=====회원데이터 관리=====");
			System.out.println("1. 회원 가입");
			System.out.println("2. 회원 목록 보기");
			System.out.println("3. 회원 정보 수정");
			System.out.println("4. 회원 정보 삭제");
			System.out.println("5. 회원 정보 검색");
			System.out.println("6. 프로그램 종료");
			System.out.println("메뉴 번호: ");
			
			//추가: menu의 범위 [1-6]를 벗어난 경우, InputMismatchException 발생한 경우에 대한 예외처리
			//코드 간결화를 위해 [1-6]범위를 벗어난 경우도 InputMismatchException으로 처리하도록 하였으나 예외발생사유가 다르므로 좋은 방법 같지는 않음
			try {
				menu = sc.nextInt();
				if(menu<1 || menu>6) {
					throw new InputMismatchException();
				}
			}
			catch(InputMismatchException e) {
				sc.nextLine();
				System.out.println("1-6 범위의 정수를 다시 입력하시오.");
				continue;
			}

			switch (menu) {
			case 1:
				action = new MemberRegistAction(); // upcasting
				break;
			case 2:
				action = new MemberListAction();
				break;
			case 3:
				action = new MemberUpdateAction();
				break;
			case 4:
				action = new MemberDeleteAction();
				break;
			case 5:
				action = new MemberSearchAction();
				break;
			case 6:
				stop = true;
				System.out.println("프로그램 종료");
				break;
			}
			//추가: stop==false 추가하여 case 6인 경우, 실행하던 구문 출력없이 바로 종료
			if (action != null  && stop==false) {
				memberController.processRequest(sc, action);
			}

		} while (!stop);
	}
}
