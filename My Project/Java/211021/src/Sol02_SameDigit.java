import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol02_SameDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int num;
        while (true) {
            try {
                System.out.print("enter two digit number(10~99) : ");
                num = sc.nextInt();
                if (num < 10 || num > 100) {
                    System.out.println("wrong number!");
                } else if (num / 10 == num % 10) {
                    System.out.println("two digits are same!");
                } else {
                    System.out.println("two digits are different!");
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
