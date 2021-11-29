/*����ó���� ����: 
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
			System.out.println("=====ȸ�������� ����=====");
			System.out.println("1. ȸ�� ����");
			System.out.println("2. ȸ�� ��� ����");
			System.out.println("3. ȸ�� ���� ����");
			System.out.println("4. ȸ�� ���� ����");
			System.out.println("5. ȸ�� ���� �˻�");
			System.out.println("6. ���α׷� ����");
			System.out.println("�޴� ��ȣ: ");
			
			//�߰�: menu�� ���� [1-6]�� ��� ���, InputMismatchException �߻��� ��쿡 ���� ����ó��
			//�ڵ� ����ȭ�� ���� [1-6]������ ��� ��쵵 InputMismatchException���� ó���ϵ��� �Ͽ����� ���ܹ߻������� �ٸ��Ƿ� ���� ��� ������ ����
			try {
				menu = sc.nextInt();
				if(menu<1 || menu>6) {
					throw new InputMismatchException();
				}
			}
			catch(InputMismatchException e) {
				sc.nextLine();
				System.out.println("1-6 ������ ������ �ٽ� �Է��Ͻÿ�.");
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
				System.out.println("���α׷� ����");
				break;
			}
			//�߰�: stop==false �߰��Ͽ� case 6�� ���, �����ϴ� ���� ��¾��� �ٷ� ����
			if (action != null  && stop==false) {
				memberController.processRequest(sc, action);
			}

		} while (!stop);
	}
}
