package view;

public class ErrorUI {
    public static void keepContinue() {
        System.out.print("wrong input! keep continue?(Y/N): ");
    }

    public static void notIntError1() {
        System.out.print("you should enter int: ");
    }

    public static void notIntError2() {
        System.out.print("INPUT--->!!INT!!<---: ");
    }

    public static void intRangeError(int n, int m) {
        System.out.printf("you should enter int in %d~%d: ", n, m);
    }

    public static void idExistError(int id) {
        System.out.println("ID: " + id + " already exist");
    }

    public static void idNotFoundError(int id) {
        System.out.println("ID: " + id + " not exist");
    }
}
