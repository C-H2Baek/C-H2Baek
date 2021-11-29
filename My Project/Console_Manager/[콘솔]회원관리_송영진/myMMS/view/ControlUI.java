package view;

public class ControlUI {
    public static void inputData(String key) {
        System.out.print("enter " + key + ": ");
    }

    public static void inputNewData(String key) {
        System.out.print("new " + key + ": ");
    }

    public static void outputData(String key, String value) {
        System.out.println(key + " before: " + value);
    }

    public static void output(String text) {
        System.out.print(text);
    }

    public static void registerInit() {
        System.out.println("=====new member register=====");
    }

    public static void registerSuccess() {
        System.out.println("register success!");
    }

    public static void showInit() {
        System.out.println("=====showing data=====");
    }

    public static void updateInit() {
        System.out.println("=====update member information=====");
    }

    public static void updateSuccess() {
        System.out.println("update success!");
    }

    public static void deleteInit() {
        System.out.println("=====delete member information=====");
    }

    public static void deleteSuccess() {
        System.out.println("delete success!");
    }

    public static void searchInit() {
        System.out.println("=====search member information=====");
    }

    public static void searchSelect() {
        System.out.print("which to search?(1: id, 2: name, 3: email, 4: address, 5: hobby, 6: tel, 7: age): ");
    }

    public static void searchNotFound() {
        System.out.println("search data not found");
    }

    public static void searchSuccess() {
        System.out.println("search success!");
    }

    public static void clearInit() {
        System.out.println("=====clear member information=====");
    }
}