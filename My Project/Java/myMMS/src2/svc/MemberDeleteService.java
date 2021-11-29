package svc;

import util.MemberDB;

public class MemberDeleteService {
    public boolean deleteMember(int id, MemberDB DB) {
        boolean deleteSuccess = true;
        if (DB.getDB().containsKey(id)) {
            DB.getDB().remove(id);
        } else {
            deleteSuccess = false;
        }
        return deleteSuccess;
    }
}