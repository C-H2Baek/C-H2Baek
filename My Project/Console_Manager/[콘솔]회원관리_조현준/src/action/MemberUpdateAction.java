package action;

import java.util.Scanner;
import util.ConsoleUtil;
import svc.MemberUpdateService;
import util.MemberDB;
import vo.Member;

public class MemberUpdateAction implements Action {
    @Override
    public void execute(Scanner sc, MemberDB DB) throws Exception {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        int id = consoleUtil.getId("수정할 ");
        MemberUpdateService memberUpdateService = new MemberUpdateService();

        Member oldMember = memberUpdateService.getOldMember(id, DB);
        Member newMember = consoleUtil.getNewMember(oldMember, sc);

        memberUpdateService.updateMember(newMember, DB);
        consoleUtil.printUpdateMessage(newMember.getId());
    }
}