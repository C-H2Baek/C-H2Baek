package util;

import java.util.InputMismatchException;
import java.util.Scanner;
import vo.SearchData;
import vo.Member;

//�߰�: Exception�� ��ӹ޾� ��������� ���� ����� ������
class idBoundException extends Exception {
	private static final long serialVersionUID = 1L;//����ȭ��?

	public idBoundException() {
	}

	public idBoundException(String msg) {
		super(msg);
	}
}

public class ConsoleUtil {

	public Member getNewMember(Scanner scan) throws idBoundException, InputMismatchException {

		Member newMember = new Member();
		System.out.println("=====�� ȸ�� ���� ���=====");

		// �߰�: �Է¹��� ���̵� 0 ������ ��, InputMismatchException �߻��ϴ� ��� ����ó�� //��������� ���� ������
		int id = 0;
		while (true) {
			try {
				System.out.print("ȸ�� ���̵�: ");
				id = scan.nextInt();
				if (id < 1) {
					throw new idBoundException("1�̻� ���� �Է��Ͻÿ�.");
				}
				break;
			} catch (InputMismatchException e) {
				scan.nextLine();
				System.out.println("������ �Է��Ͻÿ�.");
				continue;
			} catch (idBoundException e) {
				System.out.println(e.getMessage());
				continue;
			}
		}

		System.out.print("ȸ���̸�: ");
		String name = scan.next();
		System.out.print("ȸ���̸���: ");
		String email = scan.next();
		System.out.print("ȸ���ּ�: ");
		String addr = scan.next();
		System.out.print("ȸ�����: ");
		String hobby = scan.next();
		System.out.print("ȸ����ȭ��ȣ: ");
		String tel = scan.next();

		// �߰�: InputMismatchException �߻��ϴ� ��� ����ó��
		int age = 0;
		while (true) {
			try {
				System.out.print("ȸ������: ");
				age = scan.nextInt();
				break;
			} catch (InputMismatchException e) {
				scan.nextLine();
				System.out.println("������ �Է��Ͻÿ�.");
				continue;
			}
		}

		newMember.setId(id);
		newMember.setName(name);
		newMember.setEmail(email);
		newMember.setAddr(addr);
		newMember.setHobby(hobby);
		newMember.setTel(tel);
		newMember.setAge(age);

		return newMember;
	}

	public void printRegistSuccessMessage(int id) {
		System.out.println(id + "ȸ�� ��� ����");
	}

	public void printRegistFailMessage(int id) {
		System.out.println(id + " ȸ�� ��� ����");
	}

	public void printMemberList(Member[] memberArray) {
		if (memberArray.length == 0) {
			System.out.println("�߰��� ȸ�� ������ �����ϴ�.");
		} else {
			for (int i = 0; i < memberArray.length; i++) {
				System.out.println(memberArray[i]);
			}
		}
	}

	public int getId(String msgKind, Scanner scan) throws InputMismatchException{
		
		//�߰�: InputMismatchException �߻��ϴ� ��� ����ó��
		int res;
		while(true) {
			try {
				System.out.print(msgKind + "���̵�: ");
				res = scan.nextInt();
				break;
			} catch(InputMismatchException e) {
				scan.nextLine();
				System.out.println("������ �Է��Ͻÿ�.");
				continue;
			}
		}
		return res;
	}

	// ȸ�� ����: getNewMember(Scanner scan) �޼ҵ� �����ε�
	public Member getNewMember(Member oldMember, Scanner scan) {
		Member member = new Member();
		System.out.println("=====�� ȸ�� ���� ����=====");
		System.out.println("=====������ �ʿ���� �׸��� '/'�� �Է��Ͻÿ�.");	
		System.out.println("ȸ�� ���̵�: " + oldMember.getId());
		System.out.println("���� �̸�: " + oldMember.getName());
		System.out.print("�� ȸ�� �̸�: ");
		String name = scan.next();
		System.out.println("���� �̸���: " + oldMember.getEmail());
		System.out.print("�� ȸ�� �̸���: ");
		String email = scan.next();
		System.out.println("���� �ּ�: " + oldMember.getAddr());
		System.out.print("�� ȸ�� �ּ�: ");
		String addr = scan.next();
		System.out.println("���� ���: " + oldMember.getHobby());
		System.out.print("�� ȸ�� ���: ");
		String hobby = scan.next();
		System.out.println("���� ��ȭ��ȣ: " + oldMember.getTel());
		System.out.print("�� ȸ�� ��ȭ��ȣ: ");
		String tel = scan.next();
		System.out.println("���� ����: " + oldMember.getAge());
		System.out.println("�� ȸ�� ����: ");
		String age = scan.next();
		
		//�߰�: ������Ʈ ������ �ʴ� �׸��� ���� '/'�� �Է��ϵ��� ��.
		member.setId(oldMember.getId());
		member.setName((name.equals("/"))? oldMember.getName():name);
		member.setEmail((email.equals("/"))? oldMember.getEmail():email);
		member.setAddr((addr.equals("/"))? oldMember.getAddr():addr);
		member.setHobby((hobby.equals("/"))? oldMember.getHobby():hobby);
		member.setTel((tel.equals("/"))? oldMember.getTel():tel);
		member.setAge((age.equals("/"))? oldMember.getAge():Integer.parseInt(age));

		return member;
	}

	public void printUpdateSuccessMessage(int id) {
		System.out.println(id + "ȸ�� ���� ���� ����");
	}

	public void printUpdateFailMessage(int id) {
		System.out.println(id + "ȸ�� ���� ���� ����");
	}

	public void printDeleteSuccessMessage(int id) {
		System.out.println(id + "ȸ�� ���� ���� ����");
	}

	public void printDeleteFailMessage(int id) {
		System.out.println(id + "ȸ�� ���� ���� ����");
	}

	public SearchData getSearchData(Scanner scan) {
		System.out.println("�˻� ������ �����Ͻÿ�.");
		System.out.println("1. ���̵�");
		System.out.println("2. �̸�");
		System.out.println("�˻� ����: ");
		String searchCondition = scan.next();
		String searchValue = null;

		if (searchCondition.equals("���̵�")) {
			System.out.print("�˻��� ���̵�: ");
			searchValue = scan.next();
		} else if (searchCondition.equals("�̸�")) {
			System.out.print("�˻��� �̸�: ");
			searchValue = scan.next();
		}

		SearchData searchData = new SearchData();
		searchData.setSearchCondition(searchCondition);
		searchData.setSearchValue(searchValue);

		return searchData;
	}

	public void printSearchMember(Member member) {
		if (member == null) {
			System.out.println("�˻��� ����� �����ϴ�.");
		} else {
			System.out.println(member.getId() + "���� �˻��� ���");
			System.out.println(member);
		}
	}

	public void printSearchMemberArray(Member[] memberArray) {
		if (memberArray == null) {
			System.out.println("�̸����� �˻��� ����� �����ϴ�.");
		} else {
			System.out.println("�̸����� �˻��� ��� ");
			for (int i = 0; i < memberArray.length; i++) {
				System.out.println(memberArray[i]);
			}
		}
	}
}
