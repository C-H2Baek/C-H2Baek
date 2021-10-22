import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol07_OnRetantacle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int x, y;
        while (true) {
            try {
                System.out.print("enter the cordinate(x, y) : ");
                x = sc.nextInt();
                y = sc.nextInt();
                if (100 <= x && x <= 200 && 100 <= y && y <= 200) {
                    System.out.printf("(%d, %d) is in rectangle\n", x, y);
                } else {
                    System.out.printf("(%d, %d) is not in rectangle\n", x, y);
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
