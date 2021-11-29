package action;

import java.util.Scanner;
import svc.MemberDeleteService;
import util.ConsoleUtil;

public class MemberDeleteAction implements Action {
	
	@Override
	public void execute(Scanner scan) throws Exception{
		ConsoleUtil consoleUtil = new ConsoleUtil();
		int id = consoleUtil.getId("������ ", scan);
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
