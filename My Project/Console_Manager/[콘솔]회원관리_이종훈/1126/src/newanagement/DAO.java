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
	
	// 회원보기
	void selectMember() {
		Iterator<DTO> itr = md.iterator();
		
		while(itr.hasNext()) {
			// toString을 출력
			System.out.print(itr.next() + " ");
		}
	}
	
	// 회원 가입
	void MemberJoin() {
		System.out.print("ID입력 : ");  id = sc.nextLine();
		System.out.print("PW입력 : ");  pw = sc.nextLine();
		System.out.print("이름 입력 : "); name = sc.nextLine();
		System.out.print("나이 입력 : "); age = sc.nextInt(); sc.nextLine();
		
		if(idChk(id) == false) {
			System.out.print("중복된 아이디 입니다\n");
		}
		else if(idChk(id) == true) {
			md.add(new DTO(id, pw, name, age));
			System.out.print("회원가입이 완료되었습니다\n");
		}
	}

	// 중복 체크
	private boolean idChk(String id) {
		boolean chk = true;
		for(int i = 0; i < md.size(); i++) {
			if(id.equals(md.get(i).getId())) {
				chk = false;
			}
		}
		return chk;
	}
	
	// 회원 검색 _ 아이디 입력하면 나오게
	void search() {
		System.out.print("ID 입력 : ");
		id = sc.nextLine();
		for(int i = 0; i < md.size(); i++) {
			if(id.equals(md.get(i).getId())) {
				System.out.print(md.get(i));
			}
		}
	}
	
	// 회원정보 수정
	void reInfo() {
		System.out.print("ID 입력 : ");
		id = sc.nextLine();
		System.out.print("이름 수정 : 1 , 나이 수정 : 2");
		int type = Integer.parseInt(sc.nextLine());
		
		switch(type) {
		case 1:
			System.out.print("수정할 이름 입력  :");
			String newName = sc.nextLine();
			for(int i = 0; i < md.size(); i++) {
				if(id.equals(md.get(i).getId())) {
					md.get(i).setName(newName);
					System.out.print("변경 완료");
				}
			}
			break;
		case 2:
			System.out.print("수정할 나이 입력  :");
			int newAge = sc.nextInt();
			sc.nextLine();
			for(int i = 0; i < md.size(); i++) {
				if(id.equals(md.get(i).getId())) {
					md.get(i).setAge(newAge);;
					System.out.print("변경 완료");
				}
			}
			break;
		}
	}
	
	// 회원 탈퇴
	void removeMember() {
		System.out.print("ID 입력 : ");
		id = sc.nextLine();
		
		for(int i = 0; i < md.size(); i++) {
			if(id.equals(md.get(i).getId())) {
				System.out.print("정말 탈퇴하시겠습니까 : ?(Y/N)");
				String answer = sc.nextLine();
				if(answer.equalsIgnoreCase("n")) {
					System.out.print("탈퇴를 취소합니다");
				}
				else if(answer.equalsIgnoreCase("y")) {
					System.out.print(md.get(i).getId() + "계정 탈퇴되었습니다");
					md.remove(i);
				}
			}
		}
	
	}
	
	// 회원 정렬하기 (이름 순으로 정렬하기)
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


