package util;

import java.util.HashMap;

import vo.Member;

public class MemberDB {
    private final HashMap<Integer, Member> DB = new HashMap<>();

    public HashMap<Integer, Member> getDB() {
        return DB;
    }
}