package action;

import java.util.Scanner;
import svc.MemberSearchService;
import util.ConsoleUtil;
import vo.Member;
import vo.SearchData;

public class MemberSearchAction implements Action {
	@Override
	public void execute(Scanner scan) {
		ConsoleUtil consoleUtil = new ConsoleUtil();
		SearchData searchData = consoleUtil.getSearchData(scan);
		MemberSearchService memberSearchService = new MemberSearchService();

		if (searchData.getSearchCondition().equals("아이디")) {
			Member member = memberSearchService.searchMemberById(searchData.getSearchValue());
			consoleUtil.printSearchMember(member);

		} 
		else if (searchData.getSearchCondition().equals("이름")) {
			Member[] memberArray = memberSearchService.searchMemberByName(searchData.getSearchValue());
			consoleUtil.printSearchMemberArray(memberArray);
		} 
		//추가: 아이디, 이름 외의 값을 입력한 경우 다시 입력받음.
		else {
			System.out.print("다시 ");
			consoleUtil.getSearchData(scan);
		}
	}
}
