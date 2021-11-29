package util;

import java.util.InputMismatchException;
import java.util.Scanner;
import vo.SearchData;
import vo.Member;

//추가: Exception을 상속받아 사용자정의 예외 만들기 연습용
class idBoundException extends Exception {
	private static final long serialVersionUID = 1L;//직렬화란?

	public idBoundException() {
	}

	public idBoundException(String msg) {
		super(msg);
	}
}

public class ConsoleUtil {

	public Member getNewMember(Scanner scan) throws idBoundException, InputMismatchException {

		Member newMember = new Member();
		System.out.println("=====새 회원 정보 등록=====");

		// 추가: 입력받은 아이디가 0 이하일 때, InputMismatchException 발생하는 경우 예외처리 //사용자정의 예외 연습용
		int id = 0;
		while (true) {
			try {
				System.out.print("회원 아이디: ");
				id = scan.nextInt();
				if (id < 1) {
					throw new idBoundException("1이상 정수 입력하시오.");
				}
				break;
			} catch (InputMismatchException e) {
				scan.nextLine();
				System.out.println("정수를 입력하시오.");
				continue;
			} catch (idBoundException e) {
				System.out.println(e.getMessage());
				continue;
			}
		}

		System.out.print("회원이름: ");
		String name = scan.next();
		System.out.print("회원이메일: ");
		String email = scan.next();
		System.out.print("회원주소: ");
		String addr = scan.next();
		System.out.print("회원취미: ");
		String hobby = scan.next();
		System.out.print("회원전화번호: ");
		String tel = scan.next();

		// 추가: InputMismatchException 발생하는 경우 예외처리
		int age = 0;
		while (true) {
			try {
				System.out.print("회원나이: ");
				age = scan.nextInt();
				break;
			} catch (InputMismatchException e) {
				scan.nextLine();
				System.out.println("정수를 입력하시오.");
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
		System.out.println(id + "회원 등록 성공");
	}

	public void printRegistFailMessage(int id) {
		System.out.println(id + " 회원 등록 실패");
	}

	public void printMemberList(Member[] memberArray) {
		if (memberArray.length == 0) {
			System.out.println("추가된 회원 정보가 없습니다.");
		} else {
			for (int i = 0; i < memberArray.length; i++) {
				System.out.println(memberArray[i]);
			}
		}
	}

	public int getId(String msgKind, Scanner scan) throws InputMismatchException{
		
		//추가: InputMismatchException 발생하는 경우 예외처리
		int res;
		while(true) {
			try {
				System.out.print(msgKind + "아이디: ");
				res = scan.nextInt();
				break;
			} catch(InputMismatchException e) {
				scan.nextLine();
				System.out.println("정수를 입력하시오.");
				continue;
			}
		}
		return res;
	}

	// 회원 수정: getNewMember(Scanner scan) 메소드 오버로딩
	public Member getNewMember(Member oldMember, Scanner scan) {
		Member member = new Member();
		System.out.println("=====새 회원 정보 수정=====");
		System.out.println("=====수정이 필요없는 항목은 '/'를 입력하시오.");	
		System.out.println("회원 아이디: " + oldMember.getId());
		System.out.println("이전 이름: " + oldMember.getName());
		System.out.print("새 회원 이름: ");
		String name = scan.next();
		System.out.println("이전 이메일: " + oldMember.getEmail());
		System.out.print("새 회원 이메일: ");
		String email = scan.next();
		System.out.println("이전 주소: " + oldMember.getAddr());
		System.out.print("새 회원 주소: ");
		String addr = scan.next();
		System.out.println("이전 취미: " + oldMember.getHobby());
		System.out.print("새 회원 취미: ");
		String hobby = scan.next();
		System.out.println("이전 전화번호: " + oldMember.getTel());
		System.out.print("새 회원 전화번호: ");
		String tel = scan.next();
		System.out.println("이전 나이: " + oldMember.getAge());
		System.out.println("새 회원 나이: ");
		String age = scan.next();
		
		//추가: 업데이트 원하지 않는 항목의 값은 '/'로 입력하도록 함.
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
		System.out.println(id + "회원 정보 수정 성공");
	}

	public void printUpdateFailMessage(int id) {
		System.out.println(id + "회원 정보 수정 실패");
	}

	public void printDeleteSuccessMessage(int id) {
		System.out.println(id + "회원 정보 삭제 성공");
	}

	public void printDeleteFailMessage(int id) {
		System.out.println(id + "회원 정보 삭제 실패");
	}

	public SearchData getSearchData(Scanner scan) {
		System.out.println("검색 조건을 선택하시오.");
		System.out.println("1. 아이디");
		System.out.println("2. 이름");
		System.out.println("검색 조건: ");
		String searchCondition = scan.next();
		String searchValue = null;

		if (searchCondition.equals("아이디")) {
			System.out.print("검색할 아이디: ");
			searchValue = scan.next();
		} else if (searchCondition.equals("이름")) {
			System.out.print("검색할 이름: ");
			searchValue = scan.next();
		}

		SearchData searchData = new SearchData();
		searchData.setSearchCondition(searchCondition);
		searchData.setSearchValue(searchValue);

		return searchData;
	}

	public void printSearchMember(Member member) {
		if (member == null) {
			System.out.println("검색한 결과가 없습니다.");
		} else {
			System.out.println(member.getId() + "으로 검색한 결과");
			System.out.println(member);
		}
	}

	public void printSearchMemberArray(Member[] memberArray) {
		if (memberArray == null) {
			System.out.println("이름으로 검색한 결과가 없습니다.");
		} else {
			System.out.println("이름으로 검색한 결과 ");
			for (int i = 0; i < memberArray.length; i++) {
				System.out.println(memberArray[i]);
			}
		}
	}
}
