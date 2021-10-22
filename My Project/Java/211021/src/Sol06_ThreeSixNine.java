import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol06_ThreeSixNine {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int num;
        while (true) {
            try {
                System.out.print("enter the number in 1~99 : ");
                num = sc.nextInt();
                if (num < 1 || num > 99) {
                    System.out.println("wong number!");
                } else if ((num / 10 != 0 && num / 10 % 3 == 0) || num % 10 % 3 == 0) {
                    System.out.println("clap");
                } else {
                    System.out.println(num);
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
