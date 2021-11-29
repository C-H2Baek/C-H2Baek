package newanagement;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.Scanner;


public class DAO {

	ArrayList<DTO> md = new ArrayList<DTO>();
	Scanner sc = new Scanner(System.in);
	String id, pw, name;
	int age;
//	void MemberJoinDAO(){
//		md.add(new DTO("gg", "gg", "gg", 12));
//	}
	
	// ȸ������
	void selectMember() {
		Iterator<DTO> itr = md.iterator();
		
		while(itr.hasNext()) {
			// toString�� ���
			System.out.print(itr.next() + " ");
		}
	}
	
	// ȸ�� ����
	void MemberJoin() {
		System.out.print("ID�Է� : ");  id = sc.nextLine();
		System.out.print("PW�Է� : ");  pw = sc.nextLine();
		System.out.print("�̸� �Է� : "); name = sc.nextLine();
		System.out.print("���� �Է� : "); age = sc.nextInt(); sc.nextLine();
		
		if(idChk(id) == false) {
			System.out.print("�ߺ��� ���̵� �Դϴ�\n");
		}
		else if(idChk(id) == true) {
			md.add(new DTO(id, pw, name, age));
			System.out.print("ȸ�������� �Ϸ�Ǿ����ϴ�\n");
		}
	}

	// �ߺ� üũ
	private boolean idChk(String id) {
		boolean chk = true;
		for(int i = 0; i < md.size(); i++) {
			if(id.equals(md.get(i).getId())) {
				chk = false;
			}
		}
		return chk;
	}
	
	// ȸ�� �˻� _ ���̵� �Է��ϸ� ������
	void search() {
		System.out.print("ID �Է� : ");
		id = sc.nextLine();
		for(int i = 0; i < md.size(); i++) {
			if(id.equals(md.get(i).getId())) {
				System.out.print(md.get(i));
			}
		}
	}
	
	// ȸ������ ����
	void reInfo() {
		System.out.print("ID �Է� : ");
		id = sc.nextLine();
		System.out.print("�̸� ���� : 1 , ���� ���� : 2");
		int type = Integer.parseInt(sc.nextLine());
		
		switch(type) {
		case 1:
			System.out.print("������ �̸� �Է�  :");
			String newName = sc.nextLine();
			for(int i = 0; i < md.size(); i++) {
				if(id.equals(md.get(i).getId())) {
					md.get(i).setName(newName);
					System.out.print("���� �Ϸ�");
				}
			}
			break;
		case 2:
			System.out.print("������ ���� �Է�  :");
			int newAge = sc.nextInt();
			sc.nextLine();
			for(int i = 0; i < md.size(); i++) {
				if(id.equals(md.get(i).getId())) {
					md.get(i).setAge(newAge);;
					System.out.print("���� �Ϸ�");
				}
			}
			break;
		}
	}
	
	// ȸ�� Ż��
	void removeMember() {
		System.out.print("ID �Է� : ");
		id = sc.nextLine();
		
		for(int i = 0; i < md.size(); i++) {
			if(id.equals(md.get(i).getId())) {
				System.out.print("���� Ż���Ͻðڽ��ϱ� : ?(Y/N)");
				String answer = sc.nextLine();
				if(answer.equalsIgnoreCase("n")) {
					System.out.print("Ż�� ����մϴ�");
				}
				else if(answer.equalsIgnoreCase("y")) {
					System.out.print(md.get(i).getId() + "���� Ż��Ǿ����ϴ�");
					md.remove(i);
				}
			}
		}
	
	}
	
	// ȸ�� �����ϱ� (�̸� ������ �����ϱ�)
	void sortMember() {
		
		Comparator<DTO> a = new Comparator<DTO>() {

			@Override
			public int compare(DTO other1, DTO other2) {
				return other1.getName().compareTo(other2.getName());
			}
		};
		Collections.sort(md, a);
		
		System.out.println(md);
	}
}


