package action;

import java.util.Scanner;
import util.ConsoleUtil;
import svc.MemberDeleteService;
import util.MemberDB;

public class MemberDeleteAction implements Action {
    @Override
    public void execute(Scanner sc, MemberDB DB) {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        int id = consoleUtil.getId("삭제할");
        MemberDeleteService memberDeleteService = new MemberDeleteService();

        boolean deleteSuccess = memberDeleteService.deleteMember(id, DB);
        consoleUtil.printDeleteMessage(id, deleteSuccess);
    }
}