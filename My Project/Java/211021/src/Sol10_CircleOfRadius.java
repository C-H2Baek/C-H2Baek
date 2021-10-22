import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol10_CircleOfRadius {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        float x1, y1, r1, x2, y2, r2;
        while (true) {
            try {
                System.out.print("enter first circle's center with x-cord, y-cord and radius : ");
                x1 = sc.nextFloat();
                y1 = sc.nextFloat();
                r1 = sc.nextFloat();
                if (r1 < 0) {
                    System.out.println("wrong number!");
                    continue;
                }
                System.out.print("enter second circle's center with x-cord, y-cord and radius : ");
                x2 = sc.nextFloat();
                y2 = sc.nextFloat();
                r2 = sc.nextFloat();
                if (r2 < 0) {
                    System.out.println("wrong number!");
                    continue;
                }
                if ((r1 + r2) * (r1 + r2) > (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) {
                    System.out.println("two circle have two intersect points");
                } else if ((r1 + r2) * (r1 + r2) == (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) {
                    System.out.println("two circle have one intersect point");
                } else {
                    System.out.println("two circle have no intersect point");
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}