package svc;

import java.util.ArrayList;
import util.MemberDB;
import vo.Member;

public class MemberSearchService {
    public Member searchMemberById(String searchValue, MemberDB DB) {
        Member member = null;
        if (DB.getDB().containsKey(Integer.parseInt(searchValue))) {
            member = DB.getDB().get(Integer.parseInt(searchValue));
        }
        return member;
    }
    public ArrayList<Member> searchMemberByName(String searchValue, MemberDB DB){
        ArrayList<Member> searchMemberList = new ArrayList<>();
        for (Member member : DB.getDB().values()) {
            if (member.getName().equals(searchValue)) {
                searchMemberList.add(member);
            }
        }
        return searchMemberList;
    }
}