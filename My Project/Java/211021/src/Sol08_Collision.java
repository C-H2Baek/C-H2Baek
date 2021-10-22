import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol08_Collision {
    public static void sort(int smaller, int bigger) {
        int temp;
        if (bigger < smaller) {
            temp = bigger;
            bigger = smaller;
            smaller = temp;
        }
    }

    public static boolean inRect(int x1, int y1, int x2, int y2) {
        if (((100 <= x1 && x1 < 200) || (100 < x2 && x2 <= 200))
                && ((100 <= y1 && y1 < 200) || (100 < y2 && y2 <= 200))) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING ELSE TO QUIT!");
        int x1, y1, x2, y2;
        while (true) {
            try {
                System.out.print("enter first point's x-cord and y-cord : ");
                x1 = sc.nextInt();
                y1 = sc.nextInt();
                System.out.print("enter second point's x-cord and y-cord : ");
                x2 = sc.nextInt();
                y2 = sc.nextInt();
                sort(x1, x2);
                sort(y1, y2);
                if (inRect(x1, y1, x2, y2)) {
                    System.out.println("They are overlapped");
                } else {
                    System.out.println("They are not overlapped");
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
