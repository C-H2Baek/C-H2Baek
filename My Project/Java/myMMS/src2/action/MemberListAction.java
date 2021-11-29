package action;

import java.util.Scanner;
import util.MemberDB;
import svc.MemberListService;
import util.ConsoleUtil;

public class MemberListAction implements Action {
    @Override
    public void execute(Scanner sc, MemberDB DB) {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        MemberListService memberListService = new MemberListService();

        boolean listSuccess = memberListService.isEmptyMember(DB);
        consoleUtil.printMemberList(DB, listSuccess);
    }
}