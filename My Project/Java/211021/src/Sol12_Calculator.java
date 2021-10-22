import java.util.InputMismatchException;
import java.util.Scanner;

public class Sol12_Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int a, b;
        String op;
        while (true) {
            try {
                System.out.print("calculate : ");
                a = sc.nextInt();
                op = sc.next();
                b = sc.nextInt();
                if (op.equals("+")) { // if-else statement
                    System.out.println(a + " " + op + " " + b + " = " + (a + b));
                } else if (op.equals("-")) {
                    System.out.println(a + " " + op + " " + b + " = " + (a - b));
                } else if (op.equals("*")) {
                    System.out.println(a + " " + op + " " + b + " = " + (a * b));
                } else if (op.equals("/")) {
                    if (b == 0) {
                        System.out.println(a + " " + op + " " + b + " = INF");
                    } else {
                        System.out.println(a + " " + op + " " + b + " = " + ((double) a / b));
                    }
                } else {
                    System.out.println("asdfas" + op + "asdf");
                    System.out.println("wrong operator!");
                }
                switch (op) { // switch statement
                case "+":
                    System.out.println(a + " " + op + " " + b + " = " + (a + b));
                    break;
                case "-":
                    System.out.println(a + " " + op + " " + b + " = " + (a - b));
                    break;
                case "*":
                    System.out.println(a + " " + op + " " + b + " = " + (a * b));
                    break;
                case "/":
                    switch (b) {
                    case 0:
                        System.out.println(a + " " + op + " " + b + " = INF");
                        break;
                    default:
                        System.out.println(a + " " + op + " " + b + " = " + ((double) a / b));
                    }
                    break;
                default:
                    System.out.println("wrong operator!");
                }
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
