import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol09_PointInCircle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        float x0, y0, r, x, y;
        while (true) {
            try {
                System.out.print("enter the circle's center with x-cord, y-cord and radius : ");
                x0 = sc.nextFloat();
                y0 = sc.nextFloat();
                r = sc.nextFloat();
                if (r < 0) {
                    System.out.println("wrong number!");
                    continue;
                }
                System.out.print("enter the x-cord and y-cord to judge : ");
                x = sc.nextFloat();
                y = sc.nextFloat();
                if ((x - x0) * (x - x0) + (y - y0) * (y - y0) <= r * r) {
                    System.out.printf("point (%.3f, %.3f) is in circle.\n", x, y);
                } else {
                    System.out.printf("point (%.3f, %.3f) is not in circle.\n", x, y);
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}