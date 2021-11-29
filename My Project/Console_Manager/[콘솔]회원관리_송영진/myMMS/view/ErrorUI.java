package view;

public class ErrorUI {
    public static void keepContinue() {
        System.out.print("WARNING: wrong input! keep continue?(Y/N): ");
    }

    public static void notIntError1() {
        System.out.print("WARNING: you should enter int: ");
    }

    public static void notIntError2() {
        System.out.print("WARNING: INPUT--->!!INT!!<---: ");
    }

    public static void intRangeError(int n, int m) {
        System.out.printf("WARNING: you should enter int in %d~%d: ", n, m);
    }

    public static void idExistError(int id) {
        System.out.println("ERROR: id " + id + " already exist");
    }

    public static void idNotFoundError(int id) {
        System.out.println("ERROR: id " + id + " not exist");
    }

    public static void userInterrupt() {
        System.out.println("ERROR: you interrupted input");
    }
}
