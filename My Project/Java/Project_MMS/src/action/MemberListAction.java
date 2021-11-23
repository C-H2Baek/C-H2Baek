package action;

import java.util.Scanner;
import svc.MemberListService;
import util.ConsoleUtil;
import vo.Member;

public class MemberListAction implements Action {
	
	@Override
	public void execute(Scanner scan) {
		// TODO Auto-generated method stub
		ConsoleUtil consoleUtil = new ConsoleUtil();
		MemberListService memberListService = new MemberListService();
		Member[] memberArray = memberListService.getMemberArray();
		consoleUtil.printMemberList(memberArray);
	}
}

