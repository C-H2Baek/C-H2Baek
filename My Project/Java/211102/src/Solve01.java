class Song{
	private String title;
	private String artist;
	private String album;
	private String composer[];
	private int year;
	private int track;
	Song(){
		title = "���� ����";
		artist = "���� ����";
		album = "�ٹ� ����";
		composer = new String[] {"�۰ ����"};
		year = 0;
		track = 0;
	}
	/* �뷡�� ��Ÿ���� Song�̶�� Ŭ������ �����϶�. Song Ŭ������ ������ ���� �ʵ带 ���´�.
	 - �뷡�� ������ ��Ÿ���� title
	 - ������ ��Ÿ���� artist
	 - �뷡�� ���� �ٹ� ������ ��Ÿ���� album
	 - �뷡�� �۰�� ��Ÿ���� composer, �۰�� ���� �� ���� �� �ִ�.
	 - �뷡�� ��ǥ�� ������ ��Ÿ���� year
	 - �뷡�� ���� �ٹ������� Ʈ�� ��ȣ�� ��Ÿ���� track
	�����ڴ� �⺻ �����ڿ� ��� �ʵ带 �ʱ�ȭ�ϴ� �����ڸ� �ۼ��ϰ�, �뷡�� ������ ����ϴ� show() �޼ҵ嵵 �ۼ��϶�. 
	ABBA�� "Dancing Queen" �뷡�� Song ��ü�� �����ϰ� show()�� �̿��Ͽ� �� �뷡�� ������ ����ϴ� ���α׷��� �ۼ��϶�.
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
		System.out.println("����:" + title);
		System.out.println("����:" + artist);
		System.out.println("�ٹ�:" + album);
		System.out.println("�۰:");
		for(String compo : composer) {
			System.out.print(compo+"");
		}
		System.out.println();
		System.out.println("��ǥ�� ����:" + year);
		System.out.println("Ʈ����ȣ:" + track);
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

