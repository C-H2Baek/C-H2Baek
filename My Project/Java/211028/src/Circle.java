import java.util.Scanner;

public class Circle {
	
	int radius;
	String name;
	
	public Circle() {}
	
	public double getArea() {
		return 3.14*radius*radius;

	}
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Circle pizza;
		pizza = new Circle();
		System.out.print("Input Circle's Radius");
		pizza.radius = scanner.nextInt();
		pizza.name = "JAVA Pizza";
		double area = pizza.getArea();
		System.out.println(pizza.name + " 면적은 " + area);
		
		Circle donut = new Circle();
		donut.radius = scanner.nextInt();
		donut.name = "JAVA Donut";
		area = donut.getArea();
		System.out.println(donut.name + " 면적은 " + area);
		scanner.close();
		
	}
}
