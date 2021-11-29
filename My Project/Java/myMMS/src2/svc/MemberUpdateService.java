package svc;

import util.MemberDB;
import vo.Member;

public class MemberUpdateService {
    public Member getOldMember(int id, MemberDB DB) {
        Member oldMember = null;
        if (DB.getDB().containsKey(id)) {
            oldMember = DB.getDB().get(id);
        }
        return oldMember;
    }

    public void updateMember(Member newMember, MemberDB DB) {
        DB.getDB().replace(newMember.getId(), newMember);
    }
}