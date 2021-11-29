package action;

import java.util.ArrayList;
import java.util.Scanner;
import util.ConsoleUtil;
import util.MemberDB;
import vo.Member;
import vo.SearchData;
import svc.MemberSearchService;

public class MemberSearchAction implements Action {
    @Override
    public void execute(Scanner sc, MemberDB DB) {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        MemberSearchService memberSearchService = new MemberSearchService();
        SearchData searchData = consoleUtil.getSearchData(sc);

        if (searchData.getSearchCondition().equals("아이디")) {
            Member member = memberSearchService.searchMemberById(searchData.getSearchValue(), DB);
            consoleUtil.printSearchMember(member, searchData.getSearchValue());
        } else if (searchData.getSearchCondition().equals("이름")) {
            ArrayList<Member> memberList = memberSearchService.searchMemberByName(searchData.getSearchValue(), DB);
            consoleUtil.printSearchMemberList(memberList, searchData.getSearchValue());
        }
    }
}