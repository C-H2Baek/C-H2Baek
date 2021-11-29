package svc;

import util.MemberDB;
import vo.Member;

public class MemberRegistService {
    public boolean registMember(Member newMember, MemberDB DB) {
        boolean registSuccess = true;
        if (!DB.getDB().containsKey(newMember.getId())) {
            DB.getDB().put(newMember.getId(), newMember);
        } else {
            registSuccess = false;
        }
        return registSuccess;
    }
}