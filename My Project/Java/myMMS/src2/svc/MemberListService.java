package svc;

import util.MemberDB;

public class MemberListService {
    public boolean isEmptyMember(MemberDB DB) {
        return !DB.getDB().isEmpty();
    }
}