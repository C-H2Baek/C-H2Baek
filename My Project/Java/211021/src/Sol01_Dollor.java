import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol01_Dollor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int won;
        while (true) {
            try {
                System.out.print("enter cash[won] : ");
                won = sc.nextInt();
                System.out.printf("%d won is $%.3f\n", won, won / 1000.0);
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}