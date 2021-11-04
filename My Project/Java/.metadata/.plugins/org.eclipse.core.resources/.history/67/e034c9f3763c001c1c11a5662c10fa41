import java.util.Scanner;
	
public class OpenChallenge {
	public static void main(String[] args) {
		int playerNum;
		String lastWord = "아버지";
		Scanner in = new Scanner(System.in);
		System.out.print("게임에 참가하는 인원은 몇명입니까>>");
		playerNum = in.nextInt();
		Player[] players = new Player[playerNum];
		
		for(int i=0; i<playerNum;i++) {
			System.out.print("참가자의 이름을 입력하세요>>");
			String name = in.next();
			players[i] = new Player(name);
		}
		
		System.out.println("시작하는 단어는 아버지입니다.");
		while(true)
			for(int i=0; i<playerNum; i++) {
				String name = players[i].name;
				System.out.print(name + ">>");
				players[i].sayWord(in.next());
				if(players[i].succeed(lastWord) == true) {
					lastWord = players[i].word;
				}
				else {
					System.out.println(name + "이 졌습니다.");
					System.exit(0);
				}
					
			}
		}
		
	}
