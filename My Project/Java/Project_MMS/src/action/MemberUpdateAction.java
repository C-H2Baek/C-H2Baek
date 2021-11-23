package action;

import java.util.Scanner;
import svc.MemberUpdateService;
import util.ConsoleUtil;
import vo.Member;

public class MemberUpdateAction implements Action {
	
	@Override
	public void execute(Scanner scan) {
		// TODO auto-generated method stub
		
		ConsoleUtil consoleutil = new ConsoleUtil();
		int id = consoleutil.getId("¼öÁ¤ÇÔ",scan);
		MemberUpdateService memberUpdateService = new MemberUpdateService();
		Member oldMember = memberUpdateService.getOldMember(id);
		Member newMember = consoleutil.getNewMember(oldMember, scan);
		boolean updateSuccess = memberUpdateService.updateMember(newMember);
			if(updateSuccess) {
				consoleutil.printUpdateSuccessMessage(newMember.getId());
			}else {
				consoleutil.printUpdateFailMessage(newMember.getId());
			}
	}
}
