package action;

import java.util.Scanner;
import svc.MemberUpdateService;
import util.ConsoleUtil;
import vo.Member;

public class MemberUpdateAction implements Action {
	int count = 0;
	@Override
	public void execute(Scanner scan) {
		ConsoleUtil consoleUtil = new ConsoleUtil();
		int id = consoleUtil.getId("수정할 ", scan);
		MemberUpdateService memberUpdateService = new MemberUpdateService();
		Member oldMember = memberUpdateService.getOldMember(id);
		
		//추가: 아이디 입력이 세번 실패한 경우 시작메뉴로 돌아감.
		count++;
		if(count==3) {
			System.out.println("3번의 시도가 실패했습니다. 시작메뉴로 돌아갑니다.");
			return;
		}
		//추가: 입력받은 id값이 데이터베이스에 존재하지 않을 경우 재입력 받을 수 있도록 함
		if(oldMember!=null) {
			Member newMember = consoleUtil.getNewMember(oldMember, scan);
	
			boolean updateSuccess = memberUpdateService.updateMember(newMember);
	
			if (updateSuccess) {
				consoleUtil.printUpdateSuccessMessage(newMember.getId());
			} 
			else {
				consoleUtil.printDeleteFailMessage(newMember.getId());
			}
		}
		//추가: 없는 아이디 입력하여 아이디 입력으로 다시 돌아감.
		else {
			System.out.println("없는 아이디입니다. 다시 입력하시오. "+count+"번 실패.");
			execute(scan);
		}
	}
}
