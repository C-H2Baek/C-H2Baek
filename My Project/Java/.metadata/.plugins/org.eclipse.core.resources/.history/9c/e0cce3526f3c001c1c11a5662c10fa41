class Solve04 {
	public static void main(String args[]) { 
		Student s = new Student();  
		s.name = "È«±æµ¿"; 
		s.ban = 1; 
		s.no = 1; 
		s.kor = 100; 
		s.eng = 60; 
		s.math = 76;
		
		System.out.println("ÀÌ¸§ :"+s.name); 
		System.out.println("ÃÑÁ¡ :"+s.getTotal());  
		System.out.println("Æò±Õ :"+s.getAverage());
	}
}
class Student { 
	String name;
	int ban;
	int no;
	int kor;
	int eng;
	int math;
	
	public int getTotal() {
		return kor + eng + math;
	}

	public float getAverage(){
		return  Math.round(getTotal() / 3f * 100)/100f;
	}  
}