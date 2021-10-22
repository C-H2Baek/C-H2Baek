import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol11_GetASeason {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int month;
        while (true) {
            try {
                System.out.printf("enter the month(1~12) : ");
                month = sc.nextInt();
                if (month < 1 || month > 12) {
                    System.out.println("worng number!");
                } else {
                    if (month == 12) { // using if-else statement
                        System.out.println("Winter");
                    } else if (month >= 9) {
                        System.out.println("Fall");
                    } else if (month >= 6) {
                        System.out.println("Summer");
                    } else if (month >= 3) {
                        System.out.println("Spring");
                    } else {
                        System.out.println("Winter");
                    }
                    switch (month % 12 / 3) { // using switch statement
                    case 0:
                        System.out.println("Winter");
                        break;
                    case 1:
                        System.out.println("Spring");
                        break;
                    case 2:
                        System.out.println("Summer");
                        break;
                    case 3:
                        System.out.println("Fall");
                        break;
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
