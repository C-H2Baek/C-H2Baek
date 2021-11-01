class Solve02 {
	public static void main(String args[]) {
		SutdaCard card1 = new SutdaCard(3, false);
		SutdaCard card2 = new SutdaCard();
		System.out.println(card1.info());
		System.out.println(card2.info());
	}
}

class SutdaCard { 
	int num;
	boolean isKwang;

	public SutdaCard(){
		this(1, true); //SutdaCard(1,true)를 호출한다.
	}

	public SutdaCard(int num, boolean isKwang){
		this.num = num;
		this.isKwang = isKwang;
	}

	public String info(){
		return num + (isKwang ? "K" : "");
	}
}

