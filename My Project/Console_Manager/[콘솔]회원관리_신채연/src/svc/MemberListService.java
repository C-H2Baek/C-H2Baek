package svc;

import ui.MemberUI;
import vo.Member;

public class MemberListService {
	public Member[] getMemberArray() {
		return MemberUI.memberArray;
	}
}
