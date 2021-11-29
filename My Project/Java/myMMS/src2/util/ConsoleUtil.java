package util;

import vo.Member;
import vo.SearchData;
import java.util.*;

public class ConsoleUtil {
    private final InputMismatchCheck num = new InputMismatchCheck();

    public Member getNewMember(Scanner sc) {
        Member newMember = new Member();
        MemberElementList list = new MemberElementList();

        System.out.println("========== new 회원 정보 등록 ==========");
        for (String element : list.getElement()) {
            System.out.print("new 회원 " + element + " : ");
            list.setMemberElement(element, sc, newMember);
        }
        return newMember;
    }

    public Member getNewMember(Member oldMember, Scanner sc) {
        if (oldMember == null) throw new NullPointerException();
        Member member = new Member();
        MemberElementList list = new MemberElementList();
        ArrayList<String> updateList = null;

        System.out.println("========== new 회원 정보 수정 ==========");
        System.out.println(oldMember);
        sc.nextLine();
        while (updateList == null) {    //수정 항목 체크 while문
            System.out.print("수정 항목 입력(공백으로 구분) : ");
            String element = sc.nextLine();
            updateList = list.checkList(element);
        }
        for (String element : list.getElement()) {   //수정 항목 업데이트
            if (updateList.contains(element)) {
                System.out.print("old 회원 " + element + " : ");
                System.out.println(list.getMemberElement(element, oldMember));
                System.out.print("new 회원 " + element + " : ");
                list.setMemberElement(element, sc, member);
            } else {
                list.setMemberElement(element, list.getMemberElement(element, oldMember), member);
            }
        }
        return member;
    }

    public SearchData getSearchData(Scanner sc) {
        System.out.println("========== 검색 조건 선택 ==========");
        System.out.print("아이디 or 이름\n검색 조건 입력 : ");
        String searchCondition = sc.next();
        String searchValue = null;
        if (searchCondition.equals("아이디")) {
            System.out.print("검색 할 아이디 : ");
            searchValue = String.valueOf(num.Check("ID"));
        } else if (searchCondition.equals("이름")) {
            System.out.print("검색 할 이름 : ");
            searchValue = sc.next();
        } else {
            System.out.println("[!] '아이디' 또는 '이름'으로만 검색 가능 합니다");
        }
        SearchData searchData = new SearchData();
        searchData.setSearchCondition(searchCondition);
        searchData.setSearchValue(searchValue);
        return searchData;
    }

    public void printMemberList(MemberDB DB, boolean listSuccess) {
        if (listSuccess) {
            for (Member member : DB.getDB().values()) {
                System.out.println(member);
            }
        } else {
            System.out.println("[!] 현재 회원 정보가 없습니다.");
        }
    }

    public void printSearchMember(Member member, String value) {
        if (member != null) {
            System.out.println(value + "으로 검색 한 결과\n" + member);
        } else {
            System.out.println("[!]" + value + " 검색 결과가 없습니다.");
        }
    }

    public void printSearchMemberList(ArrayList<Member> memberList, String value) {
        if (memberList.size() == 0) {
            System.out.println("[!]" + value + " 검색 결과가 없습니다.");
        } else {
            System.out.println(value + " 으로 검색 한 결과");
            for (Member member : memberList) {
                System.out.println(member);
            }
        }
    }

    public void printRegistMessage(int id, boolean registSuccess) {
        if (!registSuccess) System.out.println("* " + id + " 회원 등록 실패 *");
        else System.out.println("* " + id + " 회원 등록 성공 *");
    }

    public void printUpdateMessage(int id) {
        System.out.println("* " + id + " 회원 정보 수정 성공 *");
    }

    public void printDeleteMessage(int id, boolean deleteSuccess) {
        if (!deleteSuccess) System.out.println("* " + id + " 회원 정보 삭제 실패 *");
        else System.out.println("* " + id + " 회원 정보 삭제 성공 *");
    }

    public int getId(String msgKind) {
        System.out.print(msgKind + " 아이디 : ");
        return num.Check("ID");
    }
}