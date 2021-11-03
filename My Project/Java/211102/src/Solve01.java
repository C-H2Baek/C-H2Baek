class Song{
	private String title;
	private String artist;
	private String album;
	private String composer[];
	private int year;
	private int track;
	Song(){
		title = "제목 없음";
		artist = "가수 없음";
		album = "앨범 없음";
		composer = new String[] {"작곡가 없음"};
		year = 0;
		track = 0;
	}
	/* 노래를 나타내는 Song이라는 클래스를 설계하라. Song 클래스는 다음과 같은 필드를 갖는다.
	 - 노래의 제목을 나타내는 title
	 - 가수를 나타내는 artist
	 - 노래가 속한 앨범 제목을 나타내는 album
	 - 노래의 작곡가를 나타내는 composer, 작곡가는 여러 명 있을 수 있다.
	 - 노래가 발표된 연도를 나타내는 year
	 - 노래가 속한 앨범에서의 트랙 번호를 나타내는 track
	생성자는 기본 생성자와 모든 필드를 초기화하는 생성자를 작성하고, 노래의 정보를 출력하는 show() 메소드도 작성하라. 
	ABBA의 "Dancing Queen" 노래를 Song 객체로 생성하고 show()를 이용하여 이 노래의 정보를 출력하는 프로그램을 작성하라.
	 */
	Song(String tit, String art, String alb, String[] com, int y, int tr){
		title = tit;
		artist = art;
		album = alb;
		composer = com;
		year = y;
		track = tr;
	}
	void show() {															
		System.out.println("제목:" + title);
		System.out.println("가수:" + artist);
		System.out.println("앨범:" + album);
		System.out.println("작곡가:");
		for(String compo : composer) {
			System.out.print(compo+"");
		}
		System.out.println();
		System.out.println("발표된 연도:" + year);
		System.out.println("트랙번호:" + track);
	}
}
public class Solve01{
	
	public static void main(String[] args) {
		Song s1 = new Song();
		s1.show();
		System.out.println();
		String array[]= {"adele","abc","efg"};
		Song s2 = new Song("Make You Fell My Love", "Adele" , "19" , array , 2008 , 9);
		s2.show();
	}
}

