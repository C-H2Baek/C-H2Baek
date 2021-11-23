package action;

import java.util.Scanner;
import svc.MemberDeleteService;
import util.ConsoleUtil;

public class MemberDeleteAction implements Action {
	ConsoleUtil consoleUtil = new ConsoleUtil();
	
	@Override
	public void execute(Scanner scan)throws Exception{
		int id = consoleUtil.getId("ªË¡¶«“" , scan);
		MemberDeleteService memberDeleteService = new MemberDeleteService();
		boolean deleteSuccess = memberDeleteService.deleteMember(id);
		
		if(deleteSuccess) {
			consoleUtil.printDeleteSuccessMessage(id);
		}
		else {
			consoleUtil.printDeleteFailMessage(id);
		}
	}
}
