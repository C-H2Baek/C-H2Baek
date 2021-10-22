import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol03_ChangeMoney {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int[] degree = { 50000, 10000, 1000, 100, 50, 10, 1 };
        int price;
        while (true) {
            try {
                System.out.print("enter the price : ");
                price = sc.nextInt();
                if (price < 0) {
                    System.out.println("wrong number!");
                } else {
                    for (int i : degree) {
                        System.out.println(i + " : " + price / i);
                        price %= i;
                    }
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
