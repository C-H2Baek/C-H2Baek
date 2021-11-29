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
		int id = consoleUtil.getId("������ ", scan);
		MemberUpdateService memberUpdateService = new MemberUpdateService();
		Member oldMember = memberUpdateService.getOldMember(id);
		
		//�߰�: ���̵� �Է��� ���� ������ ��� ���۸޴��� ���ư�.
		count++;
		if(count==3) {
			System.out.println("3���� �õ��� �����߽��ϴ�. ���۸޴��� ���ư��ϴ�.");
			return;
		}
		//�߰�: �Է¹��� id���� �����ͺ��̽��� �������� ���� ��� ���Է� ���� �� �ֵ��� ��
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
		//�߰�: ���� ���̵� �Է��Ͽ� ���̵� �Է����� �ٽ� ���ư�.
		else {
			System.out.println("���� ���̵��Դϴ�. �ٽ� �Է��Ͻÿ�. "+count+"�� ����.");
			execute(scan);
		}
	}
}
