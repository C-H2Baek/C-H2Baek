package util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

import vo.Member;

public class MemberElementList {
    private final ArrayList<String> element = new ArrayList<>(Arrays.asList("아이디", "이름", "나이", "전화번호", "주소", "이메일", "취미"));
    private final InputMismatchCheck num = new InputMismatchCheck();

    ArrayList<String> getElement() {
        return element;
    }

    Object getMemberElement(String element, Member member) {
        switch (element) {
            case "아이디":
                return member.getId();
            case "나이":
                return member.getAge();
            case "전화번호":
                return member.getTel();
            case "주소":
                return member.getAddr();
            case "이메일":
                return member.getEmail();
            case "취미":
                return member.getHobby();
            case "이름":
                return member.getName();
            default:
                return null;
        }
    }

    void setMemberElement(String element, Object obj, Member member) {
        if (obj instanceof Scanner) {     //obj 타입검사
            if (element.equals("아이디")) {
                obj = num.Check("ID");
            } else if (element.equals("나이")) {
                obj = num.Check("AGE");
            } else {
                obj = ((Scanner) obj).next();
            }
        }
        switch (element) {
            case "아이디":
                member.setId((Integer) obj);
                break;
            case "나이":
                member.setAge((Integer) obj);
                break;
            case "전화번호":
                member.setTel((String) obj);
                break;
            case "주소":
                member.setAddr((String) obj);
                break;
            case "이메일":
                member.setEmail((String) obj);
                break;
            case "취미":
                member.setHobby((String) obj);
                break;
            case "이름":
                member.setName((String) obj);
                break;
        }
    }

    ArrayList<String> checkList(String element) {
        ArrayList<String> newList = new ArrayList<>(Arrays.asList(element.split(" ")));

        for (String check : newList) {
            if (newList.contains("아이디")) {
                System.out.println("[!]ID는 수정 불가");
                newList = null;
                break;
            } else if (!this.element.contains(check)) {
                System.out.println("[!]수정 항목을 정확히 입력하세요");
                newList = null;
                break;
            }
        }
        return repetRemove(newList);
    }

    private ArrayList<String> repetRemove(ArrayList<String> arrayList) { //중복 제거
        if (arrayList == null) return null;
        ArrayList<String> resultList = new ArrayList<>();

        for (String result : arrayList) {
            if (!resultList.contains(result)) {
                resultList.add(result);
            }
        }
        return resultList;
    }
}