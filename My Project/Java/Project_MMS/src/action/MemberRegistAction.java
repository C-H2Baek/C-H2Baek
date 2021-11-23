package action;

import java.util.Scanner;
import svc.MemberRegistService;
import util.ConsoleUtil;
import vo.Member;

public class MemberRegistAction implements Action {
	
	@Override
	public void execute(Scanner scan)throws Exception{
		// TODO Auto-generated method stub
		ConsoleUtil consoleUtil = new ConsoleUtil();
		Member newMember = consoleUtil.getNewMember(scan);
		
		//비즈니스 로직은 Service 클래스에서 처리함
		MemberRegistService memberRegistService = new MemberRegistService();
		boolean registSuccess = memberRegistService.registMember(newMember);
		
		if(registSuccess) {
			consoleUtil.printRegistSuccessMessage(newMember.getId());
		}
		else {
			consoleUtil.printRegistFailMessage(newMember.getId());
		}
	}
}
