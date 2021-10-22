import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol05_MakeTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int a, b, c;
        while (true) {
            try {
                System.out.print("enter three side lengths : ");
                a = sc.nextInt();
                b = sc.nextInt();
                c = sc.nextInt();
                if (a < 0 || b < 0 || c < 0) {
                    System.out.println("wrong number!");
                } else if ((a + b > c) && (b + c > a) && (c + a > b)) {
                    System.out.println("It is triangle");
                } else {
                    System.out.println("It is not triangle");
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
