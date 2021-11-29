package controller;

class Runner {
    public static void main(String[] args) {
        Controller main = new Controller();
        main.initialize();
        Validate.validRun(main);
    }
}
